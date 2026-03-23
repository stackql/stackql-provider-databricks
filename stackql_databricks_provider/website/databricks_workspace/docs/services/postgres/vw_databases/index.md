---
title: vw_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_databases
  - postgres
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_databases" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.vw_databases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The database identifier (last component of the resource path).</td>
</tr>
<tr>
    <td><CopyableCode code="project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The project identifier that owns this database.</td>
</tr>
<tr>
    <td><CopyableCode code="branch_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The branch identifier that owns this database.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Database specification including postgres_database name and owner role.</td>
</tr>
<tr>
    <td><CopyableCode code="postgres_database" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The name of the Postgres database.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The identifier of the role that owns the database (last component of the resource path).</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The project identifier to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="branch_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The branch identifier to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The Databricks workspace deployment name.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  name,
  project_id,
  branch_id,
  spec,
  postgres_database,
  role
FROM databricks_workspace.postgres.vw_databases
WHERE project_id = '{{ project_id }}'
  AND branch_id = '{{ branch_id }}'
  AND deployment_name = '{{ deployment_name }}';
```

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  SPLIT_PART(name, '/', -1) AS name,
  project_id,
  branch_id,
  spec,
  JSON_EXTRACT(status, '$.postgres_database') AS postgres_database,
  SPLIT_PART(JSON_EXTRACT(status, '$.role'), '/', -1) AS role
FROM databricks_workspace.postgres.databases
WHERE deployment_name = '{{ deployment_name }}'
AND project_id = '{{ project_id }}'
AND branch_id = '{{ branch_id }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  SPLIT_PART(name, '/', -1) AS name,
  project_id,
  branch_id,
  spec,
  (status::jsonb)->>'postgres_database' AS postgres_database,
  SPLIT_PART((status::jsonb)->>'role', '/', -1) AS role
FROM databricks_workspace.postgres.databases
WHERE deployment_name = '{{ deployment_name }}'
AND project_id = '{{ project_id }}'
AND branch_id = '{{ branch_id }}'
```

</TabItem>
</Tabs>
