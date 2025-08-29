--- 
title: model_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - model_permissions
  - machinelearning
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

Creates, updates, deletes, gets or lists a <code>model_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_permissions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getpermissions"
    values={[
        { label: 'getpermissions', value: 'getpermissions' }
    ]}
>
<TabItem value="getpermissions">

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
    <td><CopyableCode code="object_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="access_control_list" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
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
    <td><a href="#getpermissions"><CopyableCode code="getpermissions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the permissions of a registered model. Registered models can inherit permissions from their root object.</td>
</tr>
<tr>
    <td><a href="#updatepermissions"><CopyableCode code="updatepermissions" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the permissions on a registered model. Registered models can inherit permissions from their root object.</td>
</tr>
<tr>
    <td><a href="#setpermissions"><CopyableCode code="setpermissions" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct permissions if none are specified. Objects can inherit permissions from their root object.</td>
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
    defaultValue="getpermissions"
    values={[
        { label: 'getpermissions', value: 'getpermissions' }
    ]}
>
<TabItem value="getpermissions">

Gets the permissions of a registered model. Registered models can inherit permissions from their root object.

```sql
SELECT
object_id,
access_control_list,
object_type
FROM databricks_workspace.machinelearning.model_permissions
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updatepermissions"
    values={[
        { label: 'updatepermissions', value: 'updatepermissions' }
    ]}
>
<TabItem value="updatepermissions">

Updates the permissions on a registered model. Registered models can inherit permissions from their root object.

```sql
UPDATE databricks_workspace.machinelearning.model_permissions
SET 
data__access_control_list = '{{ access_control_list }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
object_id,
access_control_list,
object_type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="setpermissions"
    values={[
        { label: 'setpermissions', value: 'setpermissions' }
    ]}
>
<TabItem value="setpermissions">

Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct permissions if none are specified. Objects can inherit permissions from their root object.

```sql
REPLACE databricks_workspace.machinelearning.model_permissions
SET 
data__access_control_list = '{{ access_control_list }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
object_id,
access_control_list,
object_type;
```
</TabItem>
</Tabs>
