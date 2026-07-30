---
title: postgres_forward_etl
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_forward_etl
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

Creates, updates, deletes, gets or lists a <code>postgres_forward_etl</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_forward_etl" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_forward_etl" /></td></tr>
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
    "name": "configurations",
    "type": "array",
    "description": "List of Forward ETL configurations.",
    "children": [
      {
        "name": "create_time_millis",
        "type": "integer",
        "description": "Configuration creation timestamp in milliseconds since epoch."
      },
      {
        "name": "enabled",
        "type": "boolean",
        "description": "Whether Forward ETL is enabled."
      },
      {
        "name": "pg_database_oid",
        "type": "integer",
        "description": "PostgreSQL database OID."
      },
      {
        "name": "pg_schema_oid",
        "type": "integer",
        "description": "PostgreSQL schema OID."
      },
      {
        "name": "tenant_id",
        "type": "string",
        "description": "Tenant ID (dashless UUID format)."
      },
      {
        "name": "timeline_id",
        "type": "string",
        "description": "Timeline ID (dashless UUID format)."
      },
      {
        "name": "uc_catalog_id",
        "type": "string",
        "description": "Unity Catalog catalog ID."
      },
      {
        "name": "uc_schema_id",
        "type": "string",
        "description": "Unity Catalog schema ID."
      },
      {
        "name": "update_time_millis",
        "type": "integer",
        "description": "Configuration last update timestamp in milliseconds since epoch."
      },
      {
        "name": "workspace_id",
        "type": "integer",
        "description": "Workspace ID."
      }
    ]
  },
  {
    "name": "table_mappings",
    "type": "array",
    "description": "Per-table replication mappings.",
    "children": [
      {
        "name": "enabled",
        "type": "boolean",
        "description": "Whether replication is enabled for this table."
      },
      {
        "name": "last_synced_lsn",
        "type": "string",
        "description": "Last synced LSN (Log Sequence Number) for this table."
      },
      {
        "name": "pg_table_name",
        "type": "string",
        "description": "PostgreSQL table name."
      },
      {
        "name": "pg_table_oid",
        "type": "integer",
        "description": "PostgreSQL table OID."
      },
      {
        "name": "uc_table_id",
        "type": "string",
        "description": "Unity Catalog table ID."
      },
      {
        "name": "uc_table_name",
        "type": "string",
        "description": "Unity Catalog table name."
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
    <td>Get Forward ETL configuration and status for a branch.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-pg_database_oid"><code>pg_database_oid</code></a>, <a href="#parameter-pg_schema_oid"><code>pg_schema_oid</code></a>, <a href="#parameter-tenant_id"><code>tenant_id</code></a>, <a href="#parameter-timeline_id"><code>timeline_id</code></a></td>
    <td>Disable Forward ETL for a branch.</td>
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
    <td>The Branch to disable Forward ETL for. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-pg_database_oid">
    <td><CopyableCode code="pg_database_oid" /></td>
    <td><code>integer</code></td>
    <td>PostgreSQL database OID to disable.</td>
</tr>
<tr id="parameter-pg_schema_oid">
    <td><CopyableCode code="pg_schema_oid" /></td>
    <td><code>integer</code></td>
    <td>PostgreSQL schema OID to disable.</td>
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

Get Forward ETL configuration and status for a branch.

```sql
SELECT
configurations,
table_mappings
FROM databricks_workspace.postgres.postgres_forward_etl
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND tenant_id = '{{ tenant_id }}'
AND timeline_id = '{{ timeline_id }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="disable"
    values={[
        { label: 'disable', value: 'disable' }
    ]}
>
<TabItem value="disable">

Disable Forward ETL for a branch.

```sql
DELETE FROM databricks_workspace.postgres.postgres_forward_etl
WHERE parent = '{{ parent }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND pg_database_oid = '{{ pg_database_oid }}'
AND pg_schema_oid = '{{ pg_schema_oid }}'
AND tenant_id = '{{ tenant_id }}'
AND timeline_id = '{{ timeline_id }}'
;
```
</TabItem>
</Tabs>
