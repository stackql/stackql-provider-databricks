--- 
title: workspace_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_bindings
  - unitycatalog
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

Creates, updates, deletes, gets or lists a <code>workspace_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.workspace_bindings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getbindings"
    values={[
        { label: 'getbindings', value: 'getbindings' }
    ]}
>
<TabItem value="getbindings">

A list of workspace IDs that are bound to the securable

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
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="binding_type" /></td>
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
    <td><a href="#getbindings"><CopyableCode code="getbindings" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets workspace bindings of the securable. The caller must be a metastore admin or an owner of the securable.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the catalog.</td>
</tr>
<tr>
    <td><a href="#updatebindings"><CopyableCode code="updatebindings" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates workspace bindings of the securable. The caller must be a metastore admin or an owner of the securable.</td>
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
    defaultValue="getbindings"
    values={[
        { label: 'getbindings', value: 'getbindings' }
    ]}
>
<TabItem value="getbindings">

Gets workspace bindings of the securable. The caller must be a metastore admin or an owner of the securable.

```sql
SELECT
workspace_id,
binding_type
FROM databricks_workspace.unitycatalog.workspace_bindings
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'updatebindings', value: 'updatebindings' }
    ]}
>
<TabItem value="update">

Updates workspace bindings of the catalog. The caller must be a metastore admin or an owner of the catalog.

```sql
UPDATE databricks_workspace.unitycatalog.workspace_bindings
SET 
data__assign_workspaces = '{{ assign_workspaces }}',
data__unassign_workspaces = '{{ unassign_workspaces }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
workspaces;
```
</TabItem>
<TabItem value="updatebindings">

Updates workspace bindings of the securable. The caller must be a metastore admin or an owner of the securable.

```sql
UPDATE databricks_workspace.unitycatalog.workspace_bindings
SET 
data__add = '{{ add }}',
data__remove = '{{ remove }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
bindings,
next_page_token;
```
</TabItem>
</Tabs>
