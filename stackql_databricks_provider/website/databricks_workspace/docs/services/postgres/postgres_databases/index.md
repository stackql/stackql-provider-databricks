---
title: postgres_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_databases
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

Creates, updates, deletes, gets or lists a <code>postgres_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_databases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_databases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the database. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;"
  },
  {
    "name": "database_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the database was created."
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The branch containing this database. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The desired state of the Database.",
    "children": [
      {
        "name": "role",
        "type": "string",
        "description": ""
      },
      {
        "name": "postgres_database",
        "type": "string",
        "description": "The name of the Postgres database. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS Required when creating the Database. To rename, pass a valid postgres identifier when updating the Database."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The observed state of the Database.",
    "children": [
      {
        "name": "database_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "postgres_database",
        "type": "string",
        "description": "The name of the Postgres database."
      },
      {
        "name": "role",
        "type": "string",
        "description": "The name of the role that owns the database. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the database was last updated."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Databases.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-database"><code>database</code></a></td>
    <td><a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-replace_existing"><code>replace_existing</code></a></td>
    <td>Create a Database.</td>
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
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Branch where this Database will be created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-database_id">
    <td><CopyableCode code="database_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Database, which will become the final component of the database's resource name. This ID becomes the database name in postgres. This value should be 4-63 characters, and only use characters available in DNS names, as defined by RFC-1123 If database_id is not specified in the request, it is generated automatically.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of Databases. Requests first page if absent.</td>
</tr>
<tr id="parameter-replace_existing">
    <td><CopyableCode code="replace_existing" /></td>
    <td><code>boolean</code></td>
    <td>If true, update the database if it already exists instead of returning an error.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List Databases.

```sql
SELECT
name,
database_id,
create_time,
parent,
spec,
status,
update_time
FROM databricks_workspace.postgres.postgres_databases
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
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

Create a Database.

```sql
INSERT INTO databricks_workspace.postgres.postgres_databases (
database,
parent,
deployment_name,
database_id,
replace_existing
)
SELECT 
'{{ database }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}',
'{{ database_id }}',
'{{ replace_existing }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_databases
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the postgres_databases resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_databases resource.
    - name: database
      description: |
        The desired specification of a Database.
      value:
        create_time: "{{ create_time }}"
        database_id: "{{ database_id }}"
        name: "{{ name }}"
        parent: "{{ parent }}"
        spec:
          role: "{{ role }}"
          postgres_database: "{{ postgres_database }}"
        status:
          database_id: "{{ database_id }}"
          postgres_database: "{{ postgres_database }}"
          role: "{{ role }}"
        update_time: "{{ update_time }}"
    - name: database_id
      value: "{{ database_id }}"
      description: The ID to use for the Database, which will become the final component of the database's resource name. This ID becomes the database name in postgres. This value should be 4-63 characters, and only use characters available in DNS names, as defined by RFC-1123 If database_id is not specified in the request, it is generated automatically.
      description: The ID to use for the Database, which will become the final component of the database's resource name. This ID becomes the database name in postgres. This value should be 4-63 characters, and only use characters available in DNS names, as defined by RFC-1123 If database_id is not specified in the request, it is generated automatically.
    - name: replace_existing
      value: {{ replace_existing }}
      description: If true, update the database if it already exists instead of returning an error.
      description: If true, update the database if it already exists instead of returning an error.
`}</CodeBlock>

</TabItem>
</Tabs>
