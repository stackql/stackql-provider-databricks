--- 
title: warehouse_config
hide_title: false
hide_table_of_contents: false
keywords:
  - warehouse_config
  - dbsql
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>warehouse_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warehouse_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.warehouse_config" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getworkspacewarehouseconfig"
    values={[
        { label: 'getworkspacewarehouseconfig', value: 'getworkspacewarehouseconfig' }
    ]}
>
<TabItem value="getworkspacewarehouseconfig">

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
    <td><CopyableCode code="channel" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="config_param" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="data_access_config" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enabled_warehouse_types" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="global_param" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="google_service_account" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="instance_profile_arn" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="security_policy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sql_configuration_parameters" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
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
    <td><a href="#getworkspacewarehouseconfig"><CopyableCode code="getworkspacewarehouseconfig" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the workspace level configuration that is shared by all SQL warehouses in a workspace.</td>
</tr>
<tr>
    <td><a href="#setworkspacewarehouseconfig"><CopyableCode code="setworkspacewarehouseconfig" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Sets the workspace level configuration that is shared by all SQL warehouses in a workspace.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="getworkspacewarehouseconfig"
    values={[
        { label: 'getworkspacewarehouseconfig', value: 'getworkspacewarehouseconfig' }
    ]}
>
<TabItem value="getworkspacewarehouseconfig">

Gets the workspace level configuration that is shared by all SQL warehouses in a workspace.

```sql
SELECT
channel,
config_param,
data_access_config,
enabled_warehouse_types,
global_param,
google_service_account,
instance_profile_arn,
security_policy,
sql_configuration_parameters
FROM databricks_workspace.dbsql.warehouse_config
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="setworkspacewarehouseconfig"
    values={[
        { label: 'setworkspacewarehouseconfig', value: 'setworkspacewarehouseconfig' }
    ]}
>
<TabItem value="setworkspacewarehouseconfig">

Sets the workspace level configuration that is shared by all SQL warehouses in a workspace.

```sql
REPLACE databricks_workspace.dbsql.warehouse_config
SET 
data__security_policy = '{{ security_policy }}',
data__instance_profile_arn = '{{ instance_profile_arn }}',
data__google_service_account = '{{ google_service_account }}',
data__data_access_config = '{{ data_access_config }}',
data__channel = '{{ channel }}',
data__global_param = '{{ global_param }}',
data__config_param = '{{ config_param }}',
data__sql_configuration_parameters = '{{ sql_configuration_parameters }}',
data__enabled_warehouse_types = '{{ enabled_warehouse_types }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
