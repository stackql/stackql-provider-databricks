--- 
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - cleanrooms
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

Creates, updates, deletes, gets or lists an <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.assets" /></td></tr>
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

Request completed successfully.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="added_at" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="asset_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="foreign_table" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="foreign_table_local_details" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="notebook" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owner_collaborator_alias" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="table" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="table_local_details" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="view" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="view_local_details" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="volume_local_details" /></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC asset that is added through this method, the clean room owner must also have enough privilege on the asset to consume it. The privilege must be maintained indefinitely for the clean room to be able to access the asset. Typically, you should use a group as the clean room owner.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Update a clean room asset. For example, updating the content of a notebook; changing the shared partitions of a table; etc.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a clean room asset - unshare/remove the asset from the clean room</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Request completed successfully.

```sql
SELECT
name,
added_at,
asset_type,
foreign_table,
foreign_table_local_details,
notebook,
owner_collaborator_alias,
status,
table,
table_local_details,
view,
view_local_details,
volume_local_details
FROM databricks_workspace.cleanrooms.assets
WHERE deployment_name = '{{ deployment_name }}' -- required;
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

Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC asset that is added through this method, the clean room owner must also have enough privilege on the asset to consume it. The privilege must be maintained indefinitely for the clean room to be able to access the asset. Typically, you should use a group as the clean room owner.

```sql
INSERT INTO databricks_workspace.cleanrooms.assets (
data__name,
data__asset_type,
data__table_local_details,
data__volume_local_details,
data__view_local_details,
data__foreign_table_local_details,
data__table,
data__notebook,
data__view,
data__foreign_table,
deployment_name
)
SELECT 
'{{ name }}',
'{{ asset_type }}',
'{{ table_local_details }}',
'{{ volume_local_details }}',
'{{ view_local_details }}',
'{{ foreign_table_local_details }}',
'{{ table }}',
'{{ notebook }}',
'{{ view }}',
'{{ foreign_table }}',
'{{ deployment_name }}'
RETURNING
name,
added_at,
asset_type,
foreign_table,
foreign_table_local_details,
notebook,
owner_collaborator_alias,
status,
table,
table_local_details,
view,
view_local_details,
volume_local_details
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: assets
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the assets resource.
    - name: name
      value: string
    - name: asset_type
      value: string
    - name: table_local_details
      value: object
    - name: volume_local_details
      value: object
    - name: view_local_details
      value: object
    - name: foreign_table_local_details
      value: object
    - name: table
      value: object
    - name: notebook
      value: object
    - name: view
      value: object
    - name: foreign_table
      value: object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a clean room asset. For example, updating the content of a notebook; changing the shared partitions of a table; etc.

```sql
UPDATE databricks_workspace.cleanrooms.assets
SET 
data__name = '{{ name }}',
data__asset_type = '{{ asset_type }}',
data__table_local_details = '{{ table_local_details }}',
data__volume_local_details = '{{ volume_local_details }}',
data__view_local_details = '{{ view_local_details }}',
data__foreign_table_local_details = '{{ foreign_table_local_details }}',
data__table = '{{ table }}',
data__notebook = '{{ notebook }}',
data__view = '{{ view }}',
data__foreign_table = '{{ foreign_table }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
name,
added_at,
asset_type,
foreign_table,
foreign_table_local_details,
notebook,
owner_collaborator_alias,
status,
table,
table_local_details,
view,
view_local_details,
volume_local_details;
```
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

Delete a clean room asset - unshare/remove the asset from the clean room

```sql
DELETE FROM databricks_workspace.cleanrooms.assets
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
