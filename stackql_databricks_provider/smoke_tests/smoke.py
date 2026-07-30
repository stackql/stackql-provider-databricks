"""
Authenticated smoke tests for the StackQL Databricks providers.

Runs SELECT queries against every view defined under ``views/{account,workspace}``
and verifies that each view executes without error and returns the expected
columns. Views are the highest-value test surface because they exercise the
underlying resources, the SQL dialect wiring, and the auth config all at once.

Modes:
  local (default) - tests the locally generated provider in ``stackql-provider/``
                    via a ``file://`` registry (run after ``make providers``)
  --live          - pulls the latest published providers from the public StackQL
                    registry and tests those instead

Both modes are authenticated: set DATABRICKS_ACCOUNT_ID, DATABRICKS_CLIENT_ID
and DATABRICKS_CLIENT_SECRET (or put them in ``stackql_databricks_provider/.env``).
DATABRICKS_DEPLOYMENT_NAME is optional; when unset the workspace deployment name
is derived from ``databricks_account.provisioning.workspaces``.

Usage:
  python smoke_tests/smoke.py [--live] [--scope account|workspace|all]
                              [--view SUBSTR] [--verbose]
"""

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("pyyaml is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

PROVIDER_DIR = Path(__file__).resolve().parent.parent
VIEWS_DIR = PROVIDER_DIR / "views"
REGISTRY_DIR = PROVIDER_DIR / "stackql-provider"
QUERY_TIMEOUT_SECONDS = 240

REQUIRED_ENV = ["DATABRICKS_ACCOUNT_ID", "DATABRICKS_CLIENT_ID", "DATABRICKS_CLIENT_SECRET"]

PROVIDER_BY_SCOPE = {"account": "databricks_account", "workspace": "databricks_workspace"}

# Named ANSI-less status labels keep output greppable in CI logs.
PASS, EMPTY, FAIL, SKIP = "PASS", "EMPTY", "FAIL", "SKIP"


def load_dotenv(path):
    """Load KEY=VALUE pairs from a .env file without overriding existing env."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):]
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def find_stackql(cli_arg):
    """Resolve the stackql binary: --stackql-bin, STACKQL_BIN, repo-local, PATH."""
    candidates = []
    if cli_arg:
        candidates.append(cli_arg)
    if os.environ.get("STACKQL_BIN"):
        candidates.append(os.environ["STACKQL_BIN"])
    exe = "stackql.exe" if platform.system() == "Windows" else "stackql"
    candidates.append(str(PROVIDER_DIR / exe))
    which = shutil.which("stackql")
    if which:
        candidates.append(which)
    for c in candidates:
        if c and Path(c).exists():
            return str(Path(c).resolve())
    return None


def discover_views(views_dir, scope_filter, name_filter):
    """Yield dicts describing each view found under views/{scope}/{service}/views.yaml."""
    views = []
    for path in sorted(views_dir.glob("*/*/views.yaml")):
        scope, service = path.parent.parent.name, path.parent.name
        if scope_filter != "all" and scope != scope_filter:
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for view_name, view_def in doc.items():
            if name_filter and name_filter not in view_name:
                continue
            docs_cfg = (view_def.get("config", {}) or {}).get("docs", {}) or {}
            fields = [f["name"] for f in docs_cfg.get("fields", []) if isinstance(f, dict) and "name" in f]
            params = [p["name"] for p in docs_cfg.get("requiredParams", []) if isinstance(p, dict) and "name" in p]
            views.append(
                {
                    "scope": scope,
                    "service": service,
                    "name": view_name,
                    "fields": fields,
                    "params": params,
                }
            )
    return views


class StackQLRunner:
    def __init__(self, binary, live, verbose):
        self.binary = binary
        self.live = live
        self.verbose = verbose
        approot = PROVIDER_DIR / (".stackql-smoke-live" if live else ".stackql-smoke")
        approot.mkdir(exist_ok=True)
        self.base_args = [binary, "--approot", str(approot)]
        if not live:
            reg_path = REGISTRY_DIR.resolve().as_posix()
            reg = {
                "url": f"file://{reg_path}",
                "localDocRoot": reg_path,
                "verifyConfig": {"nopVerify": True},
            }
            self.base_args += ["--registry", json.dumps(reg)]

    def exec(self, sql, output="json"):
        """Run one statement; returns (ok, rows_or_None, message)."""
        cmd = self.base_args + ["exec", "-o", output, sql]
        if self.verbose:
            print(f"    $ stackql exec: {sql}")
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, timeout=QUERY_TIMEOUT_SECONDS
            )
        except subprocess.TimeoutExpired:
            return False, None, f"timed out after {QUERY_TIMEOUT_SECONDS}s"
        stdout, stderr = proc.stdout.strip(), proc.stderr.strip()
        err_line = next(
            (l for l in stderr.splitlines() if "error" in l.lower() and "http response" in l.lower()),
            "",
        )
        if output != "json":
            ok = proc.returncode == 0
            return ok, None, stdout if ok else (err_line or stderr or stdout)
        if stdout:
            try:
                rows = json.loads(stdout)
                if isinstance(rows, list):
                    return True, rows, ""
            except json.JSONDecodeError:
                pass
        # No parseable JSON: an empty result set or a genuine error.
        blob = (stdout + "\n" + stderr).lower()
        if proc.returncode == 0 and "error" not in blob and "cannot find" not in blob and "unauthorized" not in blob:
            return True, [], ""
        return False, None, (err_line or stderr or stdout or f"exit code {proc.returncode}")

    def pull(self, provider):
        return self.exec(f"REGISTRY PULL {provider};", output="text")


def derive_seed_params(runner, account_id):
    """Best-effort derivation of parameters needed by multi-param views."""
    seeds = {"account_id": account_id}
    if os.environ.get("DATABRICKS_DEPLOYMENT_NAME"):
        seeds["deployment_name"] = os.environ["DATABRICKS_DEPLOYMENT_NAME"]
    if os.environ.get("DATABRICKS_METASTORE_ID"):
        seeds["metastore_id"] = os.environ["DATABRICKS_METASTORE_ID"]

    if "deployment_name" not in seeds or "workspace_id" not in seeds:
        ok, rows, _ = runner.exec(
            "SELECT workspace_id, deployment_name FROM databricks_account.provisioning.workspaces "
            f"WHERE account_id = '{account_id}' AND workspace_status = 'RUNNING' LIMIT 1"
        )
        if ok and rows:
            seeds.setdefault("deployment_name", str(rows[0].get("deployment_name", "")))
            seeds.setdefault("workspace_id", str(rows[0].get("workspace_id", "")))

    if "metastore_id" not in seeds:
        ok, rows, _ = runner.exec(
            "SELECT metastore_id FROM databricks_account.catalog.metastores "
            f"WHERE account_id = '{account_id}' LIMIT 1"
        )
        if ok and rows and rows[0].get("metastore_id"):
            seeds["metastore_id"] = str(rows[0]["metastore_id"])

    return {k: v for k, v in seeds.items() if v}


def run_view_test(runner, view, seeds):
    """Execute SELECT * against one view and classify the outcome."""
    provider = PROVIDER_BY_SCOPE[view["scope"]]
    fqn = f"{provider}.{view['service']}.{view['name']}"

    missing = [p for p in view["params"] if p not in seeds]
    if missing:
        return SKIP, 0, f"no seed value for param(s): {', '.join(missing)}"

    where = " AND ".join(f"{p} = '{seeds[p]}'" for p in view["params"])
    sql = f"SELECT * FROM {fqn}"
    if where:
        sql += f" WHERE {where}"
    sql += " LIMIT 5"

    ok, rows, message = runner.exec(sql)
    if not ok:
        # Several Databricks list APIs return a bare {} when there is no data,
        # which stackql surfaces as an objectKey extraction error - that is an
        # empty result, not a provider defect.
        if "unknown key" in message:
            return EMPTY, 0, "upstream returned an empty response object"
        # Feature not licensed on this account (e.g. pricing tier) - environmental.
        if "required pricing tier" in message:
            return SKIP, 0, "feature not available on this account's pricing tier"
        return FAIL, 0, message[:300]
    if not rows:
        return EMPTY, 0, "query succeeded, zero rows returned"

    expected = set(view["fields"])
    actual = set(rows[0].keys())
    missing_cols = expected - actual
    if missing_cols:
        return FAIL, len(rows), f"missing expected column(s): {', '.join(sorted(missing_cols))}"
    return PASS, len(rows), ""


def main():
    parser = argparse.ArgumentParser(description="Databricks provider smoke tests")
    parser.add_argument("--live", action="store_true", help="test latest published providers from the public registry")
    parser.add_argument("--scope", choices=["account", "workspace", "all"], default="all")
    parser.add_argument("--view", default=None, help="only run views whose name contains this substring")
    parser.add_argument("--stackql-bin", default=None, help="path to the stackql binary")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    load_dotenv(PROVIDER_DIR / ".env")

    missing_env = [v for v in REQUIRED_ENV if not os.environ.get(v)]
    if missing_env:
        print(f"ERROR: missing required environment variable(s): {', '.join(missing_env)}", file=sys.stderr)
        print("Set them in the environment or in stackql_databricks_provider/.env", file=sys.stderr)
        return 2

    binary = find_stackql(args.stackql_bin)
    if not binary:
        print("ERROR: stackql binary not found (try 'make stackql' or set STACKQL_BIN)", file=sys.stderr)
        return 2

    if not args.live and not REGISTRY_DIR.exists():
        print(f"ERROR: local registry not found at {REGISTRY_DIR} (run 'make providers' first)", file=sys.stderr)
        return 2

    mode = "live (public registry)" if args.live else f"local ({REGISTRY_DIR})"
    print(f"Databricks provider smoke tests - mode: {mode}")
    print(f"stackql binary: {binary}")

    runner = StackQLRunner(binary, args.live, args.verbose)

    if args.live:
        for provider in ("databricks_account", "databricks_workspace"):
            ok, _, message = runner.pull(provider)
            print(f"  registry pull {provider}: {'ok' if ok else 'FAILED - ' + message[:200]}")

    account_id = os.environ["DATABRICKS_ACCOUNT_ID"]
    print("Deriving seed parameters...")
    seeds = derive_seed_params(runner, account_id)
    print(f"  seed params available: {', '.join(sorted(seeds))}")

    views = discover_views(VIEWS_DIR, args.scope, args.view)
    if not views:
        print("ERROR: no views matched the given filters", file=sys.stderr)
        return 2
    print(f"Testing {len(views)} view(s)...\n")

    results = []
    for view in views:
        fqn = f"{PROVIDER_BY_SCOPE[view['scope']]}.{view['service']}.{view['name']}"
        started = time.time()
        status, row_count, message = run_view_test(runner, view, seeds)
        elapsed = time.time() - started
        results.append((fqn, status, row_count, elapsed, message))
        note = f" ({message})" if message and status in (FAIL, SKIP) else ""
        print(f"  [{status:<5}] {fqn:<75} rows={row_count:<3} {elapsed:5.1f}s{note}")

    counts = {s: sum(1 for r in results if r[1] == s) for s in (PASS, EMPTY, FAIL, SKIP)}
    print("\n" + "=" * 70)
    print(
        f"Summary: {counts[PASS]} passed, {counts[EMPTY]} empty, "
        f"{counts[FAIL]} failed, {counts[SKIP]} skipped (of {len(results)})"
    )
    if counts[FAIL]:
        print("\nFailures:")
        for fqn, status, _, _, message in results:
            if status == FAIL:
                print(f"  {fqn}: {message}")
    print("=" * 70)
    return 1 if counts[FAIL] else 0


if __name__ == "__main__":
    sys.exit(main())
