--- 
title: experiment_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_runs
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

Creates, updates, deletes, gets or lists an <code>experiment_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiment_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="searchruns"
    values={[
        { label: 'searchruns', value: 'searchruns' },
        { label: 'getrun', value: 'getrun' }
    ]}
>
<TabItem value="searchruns">

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
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="info" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getrun">

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
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="info" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
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
    <td><a href="#searchruns"><CopyableCode code="searchruns" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Searches for runs that satisfy expressions.</td>
</tr>
<tr>
    <td><a href="#getrun"><CopyableCode code="getrun" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the same key are logged for a run, return only the value with the latest timestamp.</td>
</tr>
<tr>
    <td><a href="#createrun"><CopyableCode code="createrun" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new run within an experiment. A run is usually a single execution of a machine learning or data ETL pipeline. MLflow uses runs to track the</td>
</tr>
<tr>
    <td><a href="#updaterun"><CopyableCode code="updaterun" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates run metadata.</td>
</tr>
<tr>
    <td><a href="#deleteruns"><CopyableCode code="deleteruns" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Bulk delete runs in an experiment that were created prior to or at the specified timestamp. Deletes at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the client code snippet on</td>
</tr>
<tr>
    <td><a href="#deleterun"><CopyableCode code="deleterun" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Marks a run for deletion.</td>
</tr>
<tr>
    <td><a href="#logbatch"><CopyableCode code="logbatch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server will respond with an error (non-200 status code).</td>
</tr>
<tr>
    <td><a href="#loginputs"><CopyableCode code="loginputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Experimental: This API may change or be removed in a future release without warning.</td>
</tr>
<tr>
    <td><a href="#logmetric"><CopyableCode code="logmetric" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Logs a metric for a run. A metric is a key-value pair (string key, float value) with an associated timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be logged multiple times.</td>
</tr>
<tr>
    <td><a href="#logmodel"><CopyableCode code="logmodel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Experimental: This API may change or be removed in a future release without warning.</td>
</tr>
<tr>
    <td><a href="#logparam"><CopyableCode code="logparam" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A param can be logged only once for a run.</td>
</tr>
<tr>
    <td><a href="#restorerun"><CopyableCode code="restorerun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Restores a deleted run.</td>
</tr>
<tr>
    <td><a href="#restoreruns"><CopyableCode code="restoreruns" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Bulk restore runs in an experiment that were deleted no earlier than the specified timestamp. Restores at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the client code snippet on</td>
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
    defaultValue="searchruns"
    values={[
        { label: 'searchruns', value: 'searchruns' },
        { label: 'getrun', value: 'getrun' }
    ]}
>
<TabItem value="searchruns">

Searches for runs that satisfy expressions.

```sql
SELECT
data,
info,
inputs
FROM databricks_workspace.machinelearning.experiment_runs
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getrun">

Gets the metadata, metrics, params, and tags for a run. In the case where multiple metrics with the same key are logged for a run, return only the value with the latest timestamp.

```sql
SELECT
data,
info,
inputs
FROM databricks_workspace.machinelearning.experiment_runs
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createrun"
    values={[
        { label: 'createrun', value: 'createrun' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createrun">

Creates a new run within an experiment. A run is usually a single execution of a machine learning or data ETL pipeline. MLflow uses runs to track the

```sql
INSERT INTO databricks_workspace.machinelearning.experiment_runs (
data__experiment_id,
data__user_id,
data__start_time,
data__tags,
deployment_name
)
SELECT 
'{{ experiment_id }}',
'{{ user_id }}',
{{ start_time }},
'{{ tags }}',
'{{ deployment_name }}'
RETURNING
run
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: experiment_runs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the experiment_runs resource.
    - name: experiment_id
      value: string
    - name: user_id
      value: string
    - name: start_time
      value: integer
    - name: tags
      value: Array of object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updaterun"
    values={[
        { label: 'updaterun', value: 'updaterun' }
    ]}
>
<TabItem value="updaterun">

Updates run metadata.

```sql
UPDATE databricks_workspace.machinelearning.experiment_runs
SET 
data__run_id = '{{ run_id }}',
data__run_uuid = '{{ run_uuid }}',
data__status = '{{ status }}',
data__end_time = {{ end_time }}
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
run_info;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deleteruns"
    values={[
        { label: 'deleteruns', value: 'deleteruns' },
        { label: 'deleterun', value: 'deleterun' }
    ]}
>
<TabItem value="deleteruns">

Bulk delete runs in an experiment that were created prior to or at the specified timestamp. Deletes at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the client code snippet on

```sql
DELETE FROM databricks_workspace.machinelearning.experiment_runs
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
<TabItem value="deleterun">

Marks a run for deletion.

```sql
DELETE FROM databricks_workspace.machinelearning.experiment_runs
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="logbatch"
    values={[
        { label: 'logbatch', value: 'logbatch' },
        { label: 'loginputs', value: 'loginputs' },
        { label: 'logmetric', value: 'logmetric' },
        { label: 'logmodel', value: 'logmodel' },
        { label: 'logparam', value: 'logparam' },
        { label: 'restorerun', value: 'restorerun' },
        { label: 'restoreruns', value: 'restoreruns' }
    ]}
>
<TabItem value="logbatch">

Logs a batch of metrics, params, and tags for a run. If any data failed to be persisted, the server will respond with an error (non-200 status code).

```sql
EXEC databricks_workspace.machinelearning.experiment_runs.logbatch 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"metrics": "{{ metrics }}", 
"params": "{{ params }}", 
"tags": "{{ tags }}"
}';
```
</TabItem>
<TabItem value="loginputs">

Experimental: This API may change or be removed in a future release without warning.

```sql
EXEC databricks_workspace.machinelearning.experiment_runs.loginputs 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"datasets": "{{ datasets }}"
}';
```
</TabItem>
<TabItem value="logmetric">

Logs a metric for a run. A metric is a key-value pair (string key, float value) with an associated timestamp. Examples include the various metrics that represent ML model accuracy. A metric can be logged multiple times.

```sql
EXEC databricks_workspace.machinelearning.experiment_runs.logmetric 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"run_uuid": "{{ run_uuid }}", 
"key": "{{ key }}", 
"value": "{{ value }}", 
"timestamp": "{{ timestamp }}", 
"step": "{{ step }}"
}';
```
</TabItem>
<TabItem value="logmodel">

Experimental: This API may change or be removed in a future release without warning.

```sql
EXEC databricks_workspace.machinelearning.experiment_runs.logmodel 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"model_json": "{{ model_json }}"
}';
```
</TabItem>
<TabItem value="logparam">

Logs a param used for a run. A param is a key-value pair (string key, string value). Examples include hyperparameters used for ML model training and constant dates and values used in an ETL pipeline. A param can be logged only once for a run.

```sql
EXEC databricks_workspace.machinelearning.experiment_runs.logparam 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"run_uuid": "{{ run_uuid }}", 
"key": "{{ key }}", 
"value": "{{ value }}"
}';
```
</TabItem>
<TabItem value="restorerun">

Restores a deleted run.

```sql
EXEC databricks_workspace.machinelearning.experiment_runs.restorerun 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}"
}';
```
</TabItem>
<TabItem value="restoreruns">

Bulk restore runs in an experiment that were deleted no earlier than the specified timestamp. Restores at most max_runs per request. To call this API from a Databricks Notebook in Python, you can use the client code snippet on

```sql
EXEC databricks_workspace.machinelearning.experiment_runs.restoreruns 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"experiment_id": "{{ experiment_id }}", 
"min_timestamp_millis": "{{ min_timestamp_millis }}", 
"max_runs": "{{ max_runs }}"
}';
```
</TabItem>
</Tabs>
