---
title: postgres_forward_etl_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_forward_etl_configurations
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

Creates, updates, deletes, gets or lists a <code>postgres_forward_etl_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_forward_etl_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_forward_etl_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-pg_database_oid"><code>pg_database_oid</code></a>, <a href="#parameter-pg_schema_oid"><code>pg_schema_oid</code></a>, <a href="#parameter-tenant_id"><code>tenant_id</code></a>, <a href="#parameter-timeline_id"><code>timeline_id</code></a></td>
    <td>Hard delete a Forward ETL configuration and all associated table mappings. Unlike DisableForwardEtl,</td>
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
    <td>The Branch to delete Forward ETL configuration for. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-pg_database_oid">
    <td><CopyableCode code="pg_database_oid" /></td>
    <td><code>integer</code></td>
    <td>PostgreSQL database OID to delete configuration for.</td>
</tr>
<tr id="parameter-pg_schema_oid">
    <td><CopyableCode code="pg_schema_oid" /></td>
    <td><code>integer</code></td>
    <td>PostgreSQL schema OID to delete configuration for.</td>
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

## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Hard delete a Forward ETL configuration and all associated table mappings. Unlike DisableForwardEtl,

```sql
DELETE FROM databricks_workspace.postgres.postgres_forward_etl_configurations
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
