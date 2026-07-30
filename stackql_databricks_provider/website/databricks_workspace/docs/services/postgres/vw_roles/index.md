---
title: vw_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_roles
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

Creates, updates, deletes, gets or lists a <code>vw_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_roles" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.vw_roles" /></td></tr>
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
    <td>The role identifier (last component of the resource path).</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the role was created.</td>
</tr>
<tr>
    <td><CopyableCode code="project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The project identifier that owns this role.</td>
</tr>
<tr>
    <td><CopyableCode code="branch_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The branch identifier that owns this role.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Role specification including identity type, auth method, and attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="bypassrls" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the role has the BYPASSRLS attribute.</td>
</tr>
<tr>
    <td><CopyableCode code="createdb" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the role has the CREATEDB attribute.</td>
</tr>
<tr>
    <td><CopyableCode code="createrole" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether the role has the CREATEROLE attribute.</td>
</tr>
<tr>
    <td><CopyableCode code="auth_method" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Authentication method used when connecting to Postgres.</td>
</tr>
<tr>
    <td><CopyableCode code="identity_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The type of Databricks identity backing this role (USER, SERVICE_PRINCIPAL, GROUP).</td>
</tr>
<tr>
    <td><CopyableCode code="membership_roles" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Standard roles this role is a member of (e.g. DATABRICKS_SUPERUSER).</td>
</tr>
<tr>
    <td><CopyableCode code="postgres_role" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The name of the underlying Postgres role.</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the role was last updated.</td>
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
  create_time,
  project_id,
  branch_id,
  spec,
  bypassrls,
  createdb,
  createrole,
  auth_method,
  identity_type,
  membership_roles,
  postgres_role,
  update_time
FROM databricks_workspace.postgres.vw_roles
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
  create_time,
  project_id,
  branch_id,
  spec,
  JSON_EXTRACT(status, '$.attributes.bypassrls') AS bypassrls,
  JSON_EXTRACT(status, '$.attributes.createdb') AS createdb,
  JSON_EXTRACT(status, '$.attributes.createrole') AS createrole,
  JSON_EXTRACT(status, '$.auth_method') AS auth_method,
  JSON_EXTRACT(status, '$.identity_type') AS identity_type,
  JSON_EXTRACT(status, '$.membership_roles') AS membership_roles,
  JSON_EXTRACT(status, '$.postgres_role') AS postgres_role,
  update_time
FROM databricks_workspace.postgres.postgres_roles
WHERE project_id = '{{ project_id }}'
AND branch_id = '{{ branch_id }}'
AND deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  SPLIT_PART(name, '/', -1) AS name,
  create_time,
  project_id,
  branch_id,
  spec,
  (status::jsonb)#>>'{attributes,bypassrls}' AS bypassrls,
  (status::jsonb)#>>'{attributes,createdb}' AS createdb,
  (status::jsonb)#>>'{attributes,createrole}' AS createrole,
  (status::jsonb)->>'auth_method' AS auth_method,
  (status::jsonb)->>'identity_type' AS identity_type,
  (status::jsonb)->>'membership_roles' AS membership_roles,
  (status::jsonb)->>'postgres_role' AS postgres_role,
  update_time
FROM databricks_workspace.postgres.postgres_roles
WHERE project_id = '{{ project_id }}'
AND branch_id = '{{ branch_id }}'
AND deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>
