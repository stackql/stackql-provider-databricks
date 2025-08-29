--- 
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
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

Creates, updates, deletes, gets or lists a <code>models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.models" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="searchmodels"
    values={[
        { label: 'searchmodels', value: 'searchmodels' },
        { label: 'listmodels', value: 'listmodels' },
        { label: 'getmodel', value: 'getmodel' }
    ]}
>
<TabItem value="searchmodels">

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
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="latest_versions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="listmodels">

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
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="latest_versions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getmodel">

Model details were returned successfully.

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
    <td><CopyableCode code="registered_model_databricks" /></td>
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
    <td><a href="#searchmodels"><CopyableCode code="searchmodels" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Search for registered models based on the specified</td>
</tr>
<tr>
    <td><a href="#listmodels"><CopyableCode code="listmodels" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists all available registered models, up to the limit specified in</td>
</tr>
<tr>
    <td><a href="#getmodel"><CopyableCode code="getmodel" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get the details of a model. This is a Databricks workspace version of the</td>
</tr>
<tr>
    <td><a href="#createmodel"><CopyableCode code="createmodel" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new registered model with the name specified in the request body.</td>
</tr>
<tr>
    <td><a href="#updatemodel"><CopyableCode code="updatemodel" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a registered model.</td>
</tr>
<tr>
    <td><a href="#deletemodel"><CopyableCode code="deletemodel" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a registered model.</td>
</tr>
<tr>
    <td><a href="#renamemodel"><CopyableCode code="renamemodel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Renames a registered model.</td>
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
    defaultValue="searchmodels"
    values={[
        { label: 'searchmodels', value: 'searchmodels' },
        { label: 'listmodels', value: 'listmodels' },
        { label: 'getmodel', value: 'getmodel' }
    ]}
>
<TabItem value="searchmodels">

Search for registered models based on the specified

```sql
SELECT
name,
user_id,
creation_timestamp,
description,
last_updated_timestamp,
latest_versions,
tags
FROM databricks_workspace.machinelearning.models
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listmodels">

Lists all available registered models, up to the limit specified in

```sql
SELECT
name,
user_id,
creation_timestamp,
description,
last_updated_timestamp,
latest_versions,
tags
FROM databricks_workspace.machinelearning.models
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getmodel">

Get the details of a model. This is a Databricks workspace version of the

```sql
SELECT
registered_model_databricks
FROM databricks_workspace.machinelearning.models
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createmodel"
    values={[
        { label: 'createmodel', value: 'createmodel' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createmodel">

Creates a new registered model with the name specified in the request body.

```sql
INSERT INTO databricks_workspace.machinelearning.models (
data__name,
data__description,
data__tags,
deployment_name
)
SELECT 
'{{ name }}',
'{{ description }}',
'{{ tags }}',
'{{ deployment_name }}'
RETURNING
registered_model
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: models
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the models resource.
    - name: name
      value: required
    - name: description
      value: string
    - name: tags
      value: Array of object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updatemodel"
    values={[
        { label: 'updatemodel', value: 'updatemodel' }
    ]}
>
<TabItem value="updatemodel">

Updates a registered model.

```sql
UPDATE databricks_workspace.machinelearning.models
SET 
data__name = '{{ name }}',
data__description = '{{ description }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletemodel"
    values={[
        { label: 'deletemodel', value: 'deletemodel' }
    ]}
>
<TabItem value="deletemodel">

Deletes a registered model.

```sql
DELETE FROM databricks_workspace.machinelearning.models
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="renamemodel"
    values={[
        { label: 'renamemodel', value: 'renamemodel' }
    ]}
>
<TabItem value="renamemodel">

Renames a registered model.

```sql
EXEC databricks_workspace.machinelearning.models.renamemodel 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"name": "{{ name }}", 
"new_name": "{{ new_name }}"
}';
```
</TabItem>
</Tabs>
