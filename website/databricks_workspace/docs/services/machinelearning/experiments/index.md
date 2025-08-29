--- 
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
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

Creates, updates, deletes, gets or lists an <code>experiments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="searchexperiments"
    values={[
        { label: 'searchexperiments', value: 'searchexperiments' },
        { label: 'listexperiments', value: 'listexperiments' },
        { label: 'getexperiment', value: 'getexperiment' },
        { label: 'getbyname', value: 'getbyname' }
    ]}
>
<TabItem value="searchexperiments">

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
    <td><CopyableCode code="experiment_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="artifact_location" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_update_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle_stage" /></td>
    <td><code>string</code></td>
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
<TabItem value="listexperiments">

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
    <td><CopyableCode code="experiment_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="artifact_location" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_update_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle_stage" /></td>
    <td><code>string</code></td>
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
<TabItem value="getexperiment">

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
    <td><CopyableCode code="experiment_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="artifact_location" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_update_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle_stage" /></td>
    <td><code>string</code></td>
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
<TabItem value="getbyname">

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
    <td><CopyableCode code="experiment_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="artifact_location" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_update_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle_stage" /></td>
    <td><code>string</code></td>
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
    <td><a href="#searchexperiments"><CopyableCode code="searchexperiments" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Searches for experiments that satisfy specified search criteria.</td>
</tr>
<tr>
    <td><a href="#listexperiments"><CopyableCode code="listexperiments" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a list of all experiments.</td>
</tr>
<tr>
    <td><a href="#getexperiment"><CopyableCode code="getexperiment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets metadata for an experiment. This method works on deleted experiments.</td>
</tr>
<tr>
    <td><a href="#getbyname"><CopyableCode code="getbyname" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets metadata for an experiment.</td>
</tr>
<tr>
    <td><a href="#createexperiment"><CopyableCode code="createexperiment" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that another experiment with the same name does not already exist and fails if another experiment with the same name already exists.</td>
</tr>
<tr>
    <td><a href="#updateexperiment"><CopyableCode code="updateexperiment" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates experiment metadata.</td>
</tr>
<tr>
    <td><a href="#deleteexperiment"><CopyableCode code="deleteexperiment" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the experiment uses FileStore, artifacts associated with experiment are also deleted.</td>
</tr>
<tr>
    <td><a href="#restoreexperiment"><CopyableCode code="restoreexperiment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Restore an experiment marked for deletion. This also restores associated metadata, runs, metrics, params, and tags. If experiment uses FileStore, underlying artifacts associated with experiment are also restored.</td>
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
    defaultValue="searchexperiments"
    values={[
        { label: 'searchexperiments', value: 'searchexperiments' },
        { label: 'listexperiments', value: 'listexperiments' },
        { label: 'getexperiment', value: 'getexperiment' },
        { label: 'getbyname', value: 'getbyname' }
    ]}
>
<TabItem value="searchexperiments">

Searches for experiments that satisfy specified search criteria.

```sql
SELECT
name,
experiment_id,
artifact_location,
creation_time,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listexperiments">

Gets a list of all experiments.

```sql
SELECT
name,
experiment_id,
artifact_location,
creation_time,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getexperiment">

Gets metadata for an experiment. This method works on deleted experiments.

```sql
SELECT
name,
experiment_id,
artifact_location,
creation_time,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getbyname">

Gets metadata for an experiment.

```sql
SELECT
name,
experiment_id,
artifact_location,
creation_time,
last_update_time,
lifecycle_stage,
tags
FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createexperiment"
    values={[
        { label: 'createexperiment', value: 'createexperiment' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createexperiment">

Creates an experiment with a name. Returns the ID of the newly created experiment. Validates that another experiment with the same name does not already exist and fails if another experiment with the same name already exists.

```sql
INSERT INTO databricks_workspace.machinelearning.experiments (
data__name,
data__artifact_location,
data__tags,
deployment_name
)
SELECT 
'{{ name }}',
'{{ artifact_location }}',
'{{ tags }}',
'{{ deployment_name }}'
RETURNING
experiment_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: experiments
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the experiments resource.
    - name: name
      value: required
    - name: artifact_location
      value: string
    - name: tags
      value: Array of object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updateexperiment"
    values={[
        { label: 'updateexperiment', value: 'updateexperiment' }
    ]}
>
<TabItem value="updateexperiment">

Updates experiment metadata.

```sql
UPDATE databricks_workspace.machinelearning.experiments
SET 
data__experiment_id = '{{ experiment_id }}',
data__new_name = '{{ new_name }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deleteexperiment"
    values={[
        { label: 'deleteexperiment', value: 'deleteexperiment' }
    ]}
>
<TabItem value="deleteexperiment">

Marks an experiment and associated metadata, runs, metrics, params, and tags for deletion. If the experiment uses FileStore, artifacts associated with experiment are also deleted.

```sql
DELETE FROM databricks_workspace.machinelearning.experiments
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restoreexperiment"
    values={[
        { label: 'restoreexperiment', value: 'restoreexperiment' }
    ]}
>
<TabItem value="restoreexperiment">

Restore an experiment marked for deletion. This also restores associated metadata, runs, metrics, params, and tags. If experiment uses FileStore, underlying artifacts associated with experiment are also restored.

```sql
EXEC databricks_workspace.machinelearning.experiments.restoreexperiment 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}"
}';
```
</TabItem>
</Tabs>
