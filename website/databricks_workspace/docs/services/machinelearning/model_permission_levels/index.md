--- 
title: model_permission_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - model_permission_levels
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

Creates, updates, deletes, gets or lists a <code>model_permission_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_permission_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_permission_levels" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getpermissionlevels"
    values={[
        { label: 'getpermissionlevels', value: 'getpermissionlevels' }
    ]}
>
<TabItem value="getpermissionlevels">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="permission_level" /></td>
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
    <td><a href="#getpermissionlevels"><CopyableCode code="getpermissionlevels" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the permission levels that a user can have on an object.</td>
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
    defaultValue="getpermissionlevels"
    values={[
        { label: 'getpermissionlevels', value: 'getpermissionlevels' }
    ]}
>
<TabItem value="getpermissionlevels">

Gets the permission levels that a user can have on an object.

```sql
SELECT
description,
permission_level
FROM databricks_workspace.machinelearning.model_permission_levels
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>
