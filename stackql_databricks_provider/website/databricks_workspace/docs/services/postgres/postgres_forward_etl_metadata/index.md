---
title: postgres_forward_etl_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_forward_etl_metadata
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

Creates, updates, deletes, gets or lists a <code>postgres_forward_etl_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_forward_etl_metadata" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_forward_etl_metadata" /></td></tr>
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
    "name": "databases",
    "type": "array",
    "description": "List of databases with their PostgreSQL OIDs.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Database name."
      },
      {
        "name": "oid",
        "type": "integer",
        "description": "PostgreSQL database OID."
      }
    ]
  },
  {
    "name": "schemas",
    "type": "array",
    "description": "List of schemas with their PostgreSQL OIDs.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Schema name."
      },
      {
        "name": "oid",
        "type": "integer",
        "description": "PostgreSQL schema OID."
      }
    ]
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
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-tenant_id"><code>tenant_id</code></a>, <a href="#parameter-timeline_id"><code>timeline_id</code></a></td>
    <td>Get Forward ETL metadata (database and schema OIDs).</td>
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
    <td>The Branch to get metadata for. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-tenant_id">
    <td><CopyableCode code="tenant_id" /></td>
    <td><code>string</code></td>
    <td>Tenant ID (dashless UUID format).</td>
</tr>
<tr id="parameter-timeline_id">
    <td><CopyableCode code="timeline_id" /></td>
    <td><code>string</code></td>
    <td>Timeline ID (dashless UUID format).</td>
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

Get Forward ETL metadata (database and schema OIDs).

```sql
SELECT
databases,
schemas
FROM databricks_workspace.postgres.postgres_forward_etl_metadata
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND tenant_id = '{{ tenant_id }}'
AND timeline_id = '{{ timeline_id }}'
;
```
</TabItem>
</Tabs>
