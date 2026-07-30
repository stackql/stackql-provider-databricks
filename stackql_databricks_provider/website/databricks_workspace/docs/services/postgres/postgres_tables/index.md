---
title: postgres_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_tables
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

Creates, updates, deletes, gets or lists a <code>postgres_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_tables" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_tables" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Full three-part (catalog, schema, table) name of the table."
  },
  {
    "name": "branch",
    "type": "string",
    "description": "The id of the database branch associated with the table. Of the format projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;."
  },
  {
    "name": "database",
    "type": "string",
    "description": "The project and branch scoped database to which this table belongs. Of the format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125; where database_id is the name of the logical database in Postgres."
  },
  {
    "name": "project",
    "type": "string",
    "description": "The id of the database project associated with the table. Of the format projects/&#123;project_id&#125;."
  },
  {
    "name": "table_serving_url",
    "type": "string",
    "description": "REST API URL for serving data from this table."
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a Table (non-synced database table for Autoscaling v2 Lakebase projects).</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-table"><code>table</code></a></td>
    <td></td>
    <td>Create a Table (non-synced database table for Autoscaling v2 Lakebase projects).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a Table (non-synced database table for Autoscaling v2 Lakebase projects).</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Full three-part (catalog, schema, table) name of the table.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get a Table (non-synced database table for Autoscaling v2 Lakebase projects).

```sql
SELECT
name,
branch,
database,
project,
table_serving_url
FROM databricks_workspace.postgres.postgres_tables
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a Table (non-synced database table for Autoscaling v2 Lakebase projects).

```sql
INSERT INTO databricks_workspace.postgres.postgres_tables (
table,
deployment_name
)
SELECT 
'{{ table }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
branch,
database,
project,
table_serving_url
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_tables
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_tables resource.
    - name: table
      description: |
        Table represents a non-synced database table in a Lakebase project. Unlike SyncedTable, this
        does not have a data synchronization pipeline.
      value:
        name: "{{ name }}"
        database: "{{ database }}"
        branch: "{{ branch }}"
        project: "{{ project }}"
        table_serving_url: "{{ table_serving_url }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a Table (non-synced database table for Autoscaling v2 Lakebase projects).

```sql
DELETE FROM databricks_workspace.postgres.postgres_tables
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
