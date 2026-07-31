# StackQL Databricks Provider

## What this repo is

This is a permanent fork of the [Databricks Python SDK](https://github.com/databricks/databricks-sdk-py) used to generate the `databricks_account` and `databricks_workspace` providers for [StackQL](https://github.com/stackql/stackql). The upstream SDK code (`databricks/`) is the source of truth for API operations; all provider tooling lives in `stackql_databricks_provider/`.

- Default branch: `stackql-provider` (the working branch with all StackQL-specific code)
- `main` mirrors upstream and is never modified; never open PRs against upstream
- Upstream remote: `https://github.com/databricks/databricks-sdk-py.git` (see `UPSTREAM_SYNC.md`)

## How it works

The pipeline extracts OpenAPI specs from the SDK by source introspection (parsing `self._api.do("METHOD", "/path", ...)` calls in SDK methods - no clients are instantiated, no HTTP calls made), maps operations to StackQL resources/methods/verbs via CSV inventories, then generates the final provider YAML with `@stackql/provider-utils`.

```
databricks/sdk/service/*.py            (upstream SDK - source of truth)
        | generate.py                  (introspection -> OpenAPI 3.0 specs)
openapi_generated/{account,workspace}/*.json
        | inventory_gen.py             (specs -> CSV operation inventories)
inventory/{account,workspace}/*.csv    (per-service masters + all_services.csv)
        | npm run generate-provider    (@stackql/provider-utils)
stackql-provider/src/databricks_{account,workspace}/v00.00.00000/
        | add_response_transforms.py   (post-gen response transforms)
        | merge_views.py               (inject views/ into provider specs - final step)
        | npm run generate-docs + add_doc_examples.py
website/databricks_{account,workspace}/   (docusaurus microsites)
```

Key concepts:

- **Scope split**: `AccountClient` vs `WorkspaceClient` API classes in `databricks/sdk/__init__.py` determine account vs workspace scope. The mapping is static, in `stackql_databricks_provider/registry.py` (`SERVICE_MODULES`, `ACCOUNT_API_CLASSES`).
- **CSV inventories are masters**: manual edits to `stackql_resource_name`, `stackql_method_name`, `stackql_verb`, `stackql_object_key` in the per-service CSVs are preserved by `inventory_gen.py`; only new operations are appended. `all_services.csv` per scope is regenerated from the masters and is the input to provider generation.
- **Views**: SQL views live in `stackql_databricks_provider/views/{account,workspace}/{service}/views.yaml` and are merged into `components.x-stackQL-resources` of the matching service spec by `merge_views.py` (must run last). Views are also the smoke test surface.
- **Auth**: both providers use OAuth2 client credentials with `DATABRICKS_ACCOUNT_ID`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET` (same vars as Terraform / the Databricks CLI). Local dev secrets can go in `stackql_databricks_provider/.env` (gitignored).
- **Doc microsites**: the docusaurus sites under `website/databricks_{account,workspace}` vendor the shared StackQL site config - `npm run build` (via `prebuild`) shallow-clones [stackql/docusaurus-config](https://github.com/stackql/docusaurus-config) into a gitignored `.shared-config/` and `docusaurus.config.js` calls its `createConfig` factory, with only `provider.js` (name/title) and a couple of overrides per site. The provider index page content (intro, auth, getting-started reference queries) is mastered in `docgen/provider-data/<provider>/headerContent{1,2}.txt` and spliced in by `generate-docs`.

## Workflow (Makefile)

All commands run from `stackql_databricks_provider/` in a POSIX shell (WSL on Windows):

```bash
cd stackql_databricks_provider
make help            # list all targets
make upstream-pull   # git fetch upstream && git merge upstream/main
make deps            # pip install -e ".[dev]" + npm install
make all             # specs -> inventory -> unit-test -> providers -> test-meta -> smoke -> docs -> docs-build
```

Individual steps: `make specs`, `make inventory`, `make unit-test`, `make providers`, `make test-meta`, `make smoke`, `make smoke-live`, `make docs`, `make docs-build`.

### After an upstream pull

1. Check for new service modules: `git diff HEAD~1 --name-status -- databricks/sdk/service/ | grep '^A'`
2. Register new modules in `SERVICE_MODULES` and new account-scoped API classes in `ACCOUNT_API_CLASSES` in `registry.py`. Only register modules whose API classes are wired into `AccountClient`/`WorkspaceClient` in `databricks/sdk/__init__.py`. Some modules are deliberately excluded (currently: `bundle`, `dataclassification`, `environments`, `knowledgeassistants`, `networking`, `_internal`).
3. Run `make specs inventory` and review the CSV diffs - new operations default `stackql_resource_name` to the last tag and `stackql_verb` from the HTTP verb; curate them in the per-service CSVs (e.g. lifecycle POSTs like `cancel`/`delete`-semantics operations should map to the `delete` verb, data-plane `exec` operations to `exec`).
4. `make unit-test providers smoke` to regenerate and verify.

## Testing

- **Unit tests**: `make unit-test` (pytest over `stackql_databricks_provider/tests/`) - covers the extraction/generation machinery, no network.
- **Meta-route tests**: `make test-meta` - starts a local stackql server against the generated registry and walks all services/resources/methods.
- **Smoke tests** (authenticated, hit real Databricks endpoints): `make smoke` tests the locally generated provider via a `file://` registry; `make smoke-live` pulls the latest *published* providers from the public StackQL registry and tests those. Both iterate every view under `views/`, run `SELECT *` with required params (seeded from env / derived via `databricks_account.provisioning.workspaces`), and verify the query succeeds and returns the documented columns. Implementation: `smoke_tests/smoke.py`.

## Publishing

Push the generated `stackql-provider/src/databricks_{account,workspace}` trees to `providers/src` in a feature branch of [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry). See `stackql_databricks_provider/STACKQL_PROVIDER_GENERATION.md` for the full manual workflow and example queries.

## Gotchas

- `merge_views.py` must be the final post-gen step; regenerating a provider overwrites its output including merged views and response transforms.
- The generator skips SDK methods without a `self._api.do()` call (`wait_*`, `*_and_wait` helpers) - by design.
- The SDK uses `from __future__ import annotations`; the extractor resolves string annotations against the service module namespace.
- Service-level pagination (`next_page_token`/`page_token`) is injected via `--service-config` as `x-stackQL-config` on every service. any-sdk also supports method-level `config.pagination` (operation config overrides resource, then service, then provider level - see `operation_store.go` in any-sdk). Note: pagination request tokens can only be applied as `query`, `body`, or `requestString` (full URL replace) - `path` location is not supported by any-sdk's `SetNextPage`, and relative URLs (e.g. `next_chunk_internal_link` in `sql.statement_execution`) are not resolved against the request host, so chunk-following pagination for statement results cannot be wired in the provider today; it needs an any-sdk enhancement.
- `sql.statement_execution` verb mappings: `execute` -> `insert`, `get`/`get_result_chunk` -> `select`, `cancel` -> `delete` (it is a POST on the wire, but semantically a DELETE of a running statement).
