---
title: databricks_workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/stackql-databricks-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Manage clusters, jobs, notebooks, MLflow and other Databricks workspace resources.

:::info

For Databricks account operations use the [__`databricks_account`__](https://databricks-account-provider.stackql.io/) provider.

:::

:::info[Provider Summary]

total services: __29__
total resources: __342__

:::

See also:    [[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)   

* * *   

## Installation 

```bash 
REGISTRY PULL databricks_workspace; 
```  

## Authentication  

To use the `databricks_workspace` provider, you can authenticate using one of the following methods:

### OAuth2 (Service Principal) [Default]

Set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.  

### Personal Access Token (Bearer)

Alternatively, set <CopyableCode code="DATABRICKS_TOKEN" /> to a Databricks personal access token (see <a href="https://docs.databricks.com/en/dev-tools/auth/pat.html">Databricks personal access tokens</a>), then supply the auth config when starting the shell:
```bash
export DATABRICKS_TOKEN=xxx

# Linux/Mac
AUTH='{ "databricks_workspace": { "type": "bearer", "credentialsenvvar": "DATABRICKS_TOKEN" }}'
./stackql shell --auth="${AUTH}"
```
```powershell
# PowerShell
$Auth = "{ 'databricks_workspace': { 'type': 'bearer', 'credentialsenvvar': 'DATABRICKS_TOKEN' }}"
stackql.exe shell --auth=$Auth
```

## Unity Catalog inventory

Catalogs in a workspace, with ownership and audit fields:

```sql
SELECT
  full_name,
  catalog_type,
  owner,
  comment,
  datetime(created_at/1000, 'unixepoch') AS created,
  created_by
FROM databricks_workspace.catalog.catalogs
WHERE deployment_name = '<deployment_name>';
```

Walk the catalog hierarchy - schemas and tables in a catalog:

```sql
SELECT full_name, table_type, data_source_format, owner
FROM databricks_workspace.catalog.tables
WHERE catalog_name = 'main'
AND schema_name = 'default'
AND deployment_name = '<deployment_name>';
```

## SQL statement execution - the full lifecycle

The Databricks SQL Statement Execution API maps naturally to SQL verbs - `INSERT` submits a statement, `SELECT` polls it, `DELETE` cancels it:

```sql
/* submit a statement to a SQL warehouse */
INSERT INTO databricks_workspace.sql.statement_execution (
  statement,
  warehouse_id,
  wait_timeout,
  deployment_name
)
SELECT
  'SELECT * FROM samples.nyctaxi.trips LIMIT 100',
  '<warehouse_id>',
  '0s',
  '<deployment_name>';

/* poll for status and results */
SELECT status, manifest, result
FROM databricks_workspace.sql.statement_execution
WHERE statement_id = '<statement_id>'
AND deployment_name = '<deployment_name>';

/* cancel a running statement */
DELETE FROM databricks_workspace.sql.statement_execution
WHERE statement_id = '<statement_id>'
AND deployment_name = '<deployment_name>';
```

Recent query history across SQL warehouses and serverless compute:

```sql
SELECT query_id, status, query_text, user_name
FROM databricks_workspace.sql.query_history
WHERE deployment_name = '<deployment_name>';
```

## Workspace identity

Users, their groups and entitlements, flattened with built-in views:

```sql
SELECT * FROM databricks_workspace.iam.vw_users WHERE deployment_name = '<deployment_name>';
SELECT * FROM databricks_workspace.iam.vw_user_groups WHERE deployment_name = '<deployment_name>';
SELECT * FROM databricks_workspace.iam.vw_user_entitlements WHERE deployment_name = '<deployment_name>';
SELECT * FROM databricks_workspace.iam.vw_group_members WHERE deployment_name = '<deployment_name>';
```

## Compute estate

Clusters with their state, node types and autotermination settings:

```sql
SELECT
  cluster_id,
  cluster_name,
  state,
  node_type_id,
  autotermination_minutes,
  spark_version
FROM databricks_workspace.compute.clusters
WHERE deployment_name = '<deployment_name>';
```

SQL warehouses, sized and by state:

```sql
SELECT id, name, state, cluster_size, num_clusters, auto_stop_mins
FROM databricks_workspace.sql.warehouses
WHERE deployment_name = '<deployment_name>';
```

## Workspace settings

All workspace admin settings as key/value pairs, using a built-in view:

```sql
SELECT key, value
FROM databricks_workspace.settings.vw_all_settings
WHERE deployment_name = '<deployment_name>';
```


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/agentbricks/">agentbricks</a><br />
<a href="/services/aisearch/">aisearch</a><br />
<a href="/services/apps/">apps</a><br />
<a href="/services/bundledeployments/">bundledeployments</a><br />
<a href="/services/catalog/">catalog</a><br />
<a href="/services/cleanrooms/">cleanrooms</a><br />
<a href="/services/compute/">compute</a><br />
<a href="/services/dashboards/">dashboards</a><br />
<a href="/services/database/">database</a><br />
<a href="/services/dataquality/">dataquality</a><br />
<a href="/services/files/">files</a><br />
<a href="/services/iam/">iam</a><br />
<a href="/services/iamv2/">iamv2</a><br />
<a href="/services/jobs/">jobs</a><br />
<a href="/services/marketplace/">marketplace</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/ml/">ml</a><br />
<a href="/services/oauth2/">oauth2</a><br />
<a href="/services/pipelines/">pipelines</a><br />
<a href="/services/postgres/">postgres</a><br />
<a href="/services/qualitymonitorv2/">qualitymonitorv2</a><br />
<a href="/services/serving/">serving</a><br />
<a href="/services/settings/">settings</a><br />
<a href="/services/settingsv2/">settingsv2</a><br />
<a href="/services/sharing/">sharing</a><br />
<a href="/services/sql/">sql</a><br />
<a href="/services/supervisoragents/">supervisoragents</a><br />
<a href="/services/tags/">tags</a><br />
<a href="/services/vectorsearch/">vectorsearch</a><br />
<a href="/services/workspace/">workspace</a><br />
</div>
</div>
