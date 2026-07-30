---
title: vw_branches
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_branches
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

Creates, updates, deletes, gets or lists a <code>vw_branches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_branches" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.vw_branches" /></td></tr>
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
    <td>The branch identifier (last component of the resource path).</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the branch was created.</td>
</tr>
<tr>
    <td><CopyableCode code="project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The project identifier that owns this branch.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Branch specification including expiry and protection settings.</td>
</tr>
<tr>
    <td><CopyableCode code="branch_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>System-assigned branch identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="current_state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Current operational state of the branch (e.g. READY, INIT).</td>
</tr>
<tr>
    <td><CopyableCode code="default" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether this is the project's default branch.</td>
</tr>
<tr>
    <td><CopyableCode code="is_protected" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the branch is protected from deletion and reset.</td>
</tr>
<tr>
    <td><CopyableCode code="logical_size_bytes" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Logical size of the branch in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="state_change_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp indicating when the current_state began.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><CopyableCode code="string" /></td>
    <td>System-generated unique ID for the branch.</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the branch was last updated.</td>
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
  create_time,
  project_id,
  spec,
  branch_id,
  current_state,
  default,
  is_protected,
  logical_size_bytes,
  state_change_time,
  uid,
  update_time
FROM databricks_workspace.postgres.vw_branches
WHERE project_id = '{{ project_id }}'
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
  create_time,
  project_id,
  spec,
  JSON_EXTRACT(status, '$.branch_id') AS branch_id,
  JSON_EXTRACT(status, '$.current_state') AS current_state,
  JSON_EXTRACT(status, '$.default') AS default,
  JSON_EXTRACT(status, '$.is_protected') AS is_protected,
  JSON_EXTRACT(status, '$.logical_size_bytes') AS logical_size_bytes,
  JSON_EXTRACT(status, '$.state_change_time') AS state_change_time,
  uid,
  update_time
FROM databricks_workspace.postgres.postgres_branches
WHERE project_id = '{{ project_id }}'
AND deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  SPLIT_PART(name, '/', -1) AS name,
  create_time,
  project_id,
  spec,
  (status::jsonb)->>'branch_id' AS branch_id,
  (status::jsonb)->>'current_state' AS current_state,
  (status::jsonb)->>'default' AS default,
  (status::jsonb)->>'is_protected' AS is_protected,
  (status::jsonb)->>'logical_size_bytes' AS logical_size_bytes,
  (status::jsonb)->>'state_change_time' AS state_change_time,
  uid,
  update_time
FROM databricks_workspace.postgres.postgres_branches
WHERE project_id = '{{ project_id }}'
AND deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>
