--- 
title: model_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - model_versions
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

Creates, updates, deletes, gets or lists a <code>model_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="searchmodelversions"
    values={[
        { label: 'searchmodelversions', value: 'searchmodelversions' },
        { label: 'getmodelversion', value: 'getmodelversion' }
    ]}
>
<TabItem value="searchmodelversions">

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
    <td><CopyableCode code="run_id" /></td>
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
    <td><CopyableCode code="current_stage" /></td>
    <td><code>string</code></td>
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
    <td><CopyableCode code="run_link" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status_message" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getmodelversion">

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
    <td><CopyableCode code="run_id" /></td>
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
    <td><CopyableCode code="current_stage" /></td>
    <td><code>string</code></td>
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
    <td><CopyableCode code="run_link" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status_message" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
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
    <td><a href="#searchmodelversions"><CopyableCode code="searchmodelversions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Searches for specific model versions based on the supplied</td>
</tr>
<tr>
    <td><a href="#getmodelversion"><CopyableCode code="getmodelversion" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a model version.</td>
</tr>
<tr>
    <td><a href="#createmodelversion"><CopyableCode code="createmodelversion" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a model version.</td>
</tr>
<tr>
    <td><a href="#updatemodelversion"><CopyableCode code="updatemodelversion" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the model version.</td>
</tr>
<tr>
    <td><a href="#deletemodelversion"><CopyableCode code="deletemodelversion" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a model version.</td>
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
    defaultValue="searchmodelversions"
    values={[
        { label: 'searchmodelversions', value: 'searchmodelversions' },
        { label: 'getmodelversion', value: 'getmodelversion' }
    ]}
>
<TabItem value="searchmodelversions">

Searches for specific model versions based on the supplied

```sql
SELECT
name,
run_id,
user_id,
creation_timestamp,
current_stage,
description,
last_updated_timestamp,
run_link,
source,
status,
status_message,
tags,
version
FROM databricks_workspace.machinelearning.model_versions
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getmodelversion">

Get a model version.

```sql
SELECT
name,
run_id,
user_id,
creation_timestamp,
current_stage,
description,
last_updated_timestamp,
run_link,
source,
status,
status_message,
tags,
version
FROM databricks_workspace.machinelearning.model_versions
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createmodelversion"
    values={[
        { label: 'createmodelversion', value: 'createmodelversion' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createmodelversion">

Creates a model version.

```sql
INSERT INTO databricks_workspace.machinelearning.model_versions (
data__name,
data__source,
data__run_id,
data__run_link,
data__description,
data__tags,
deployment_name
)
SELECT 
'{{ name }}',
'{{ source }}',
'{{ run_id }}',
'{{ run_link }}',
'{{ description }}',
'{{ tags }}',
'{{ deployment_name }}'
RETURNING
model_version
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: model_versions
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the model_versions resource.
    - name: name
      value: required
    - name: source
      value: string
    - name: run_id
      value: required
    - name: run_link
      value: string
    - name: description
      value: string
    - name: tags
      value: Array of object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updatemodelversion"
    values={[
        { label: 'updatemodelversion', value: 'updatemodelversion' }
    ]}
>
<TabItem value="updatemodelversion">

Updates the model version.

```sql
UPDATE databricks_workspace.machinelearning.model_versions
SET 
data__name = '{{ name }}',
data__version = '{{ version }}',
data__description = '{{ description }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletemodelversion"
    values={[
        { label: 'deletemodelversion', value: 'deletemodelversion' }
    ]}
>
<TabItem value="deletemodelversion">

Deletes a model version.

```sql
DELETE FROM databricks_workspace.machinelearning.model_versions
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
