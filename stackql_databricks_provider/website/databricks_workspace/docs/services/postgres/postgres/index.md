---
title: postgres
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres
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

Creates, updates, deletes, gets or lists a <code>postgres</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="postgres_list_databases"
    values={[
        { label: 'postgres_list_databases', value: 'postgres_list_databases' }
    ]}
>
<TabItem value="postgres_list_databases">

<SchemaTable fields={[
  {
    "name": "databases",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "create_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the database was created."
      },
      {
        "name": "name",
        "type": "string",
        "description": "The resource name of the database. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;"
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
            "name": "postgres_database",
            "type": "string",
            "description": ""
          },
          {
            "name": "role",
            "type": "string",
            "description": "The name of the role that owns the database. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125; To change the owner, pass valid existing Role name when updating the Database A database always has an owner."
          }
        ]
      },
      {
        "name": "status",
        "type": "object",
        "description": "The observed state of the Database.",
        "children": [
          {
            "name": "postgres_database",
            "type": "string",
            "description": ""
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
    ]
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "Pagination token to request the next page of databases."
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
    <td><a href="#postgres_list_databases"><CopyableCode code="postgres_list_databases" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Databases.</td>
</tr>
<tr>
    <td><a href="#postgres_create_database"><CopyableCode code="postgres_create_database" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-database"><code>database</code></a></td>
    <td><a href="#parameter-database_id"><code>database_id</code></a></td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="postgres_list_databases"
    values={[
        { label: 'postgres_list_databases', value: 'postgres_list_databases' }
    ]}
>
<TabItem value="postgres_list_databases">

List Databases.

```sql
SELECT
databases,
next_page_token
FROM databricks_workspace.postgres.postgres
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
    defaultValue="postgres_create_database"
    values={[
        { label: 'postgres_create_database', value: 'postgres_create_database' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="postgres_create_database">

Create a Database.

```sql
INSERT INTO databricks_workspace.postgres.postgres (
database,
parent,
deployment_name,
database_id
)
SELECT 
'{{ database }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}',
'{{ database_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the postgres resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres resource.
    - name: database
      description: |
        The desired specification of a Database.
      value:
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        parent: "{{ parent }}"
        spec:
          postgres_database: "{{ postgres_database }}"
          role: "{{ role }}"
        status:
          postgres_database: "{{ postgres_database }}"
          role: "{{ role }}"
        update_time: "{{ update_time }}"
    - name: database_id
      value: "{{ database_id }}"
      description: The ID to use for the Database, which will become the final component of the database's resource name. This ID becomes the database name in postgres. This value should be 4-63 characters, and only use characters available in DNS names, as defined by RFC-1123 If database_id is not specified in the request, it is generated automatically.
`}</CodeBlock>

</TabItem>
</Tabs>
