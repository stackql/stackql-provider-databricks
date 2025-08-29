--- 
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runs
  - workflows
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

Creates, updates, deletes, gets or lists a <code>job_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workflows.job_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listruns"
    values={[
        { label: 'listruns', value: 'listruns' },
        { label: 'getrun', value: 'getrun' }
    ]}
>
<TabItem value="listruns">

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
    <td><CopyableCode code="job_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="job_run_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="original_attempt_run_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="attempt_number" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cleanup_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_instance" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="end_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="execution_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="git_source" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_more" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="job_clusters" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="job_parameters" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="number_in_job" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="overriding_parameters" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="queue_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="repair_history" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_page_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="setup_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger_info" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getrun">

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
    <td><CopyableCode code="job_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="job_run_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="original_attempt_run_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="attempt_number" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cleanup_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_instance" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="end_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="execution_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="git_source" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_more" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="job_clusters" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="job_parameters" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="next_page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="number_in_job" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="overriding_parameters" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="queue_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="repair_history" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_page_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="setup_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger_info" /></td>
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
    <td><a href="#listruns"><CopyableCode code="listruns" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>List runs in descending order by start time.</td>
</tr>
<tr>
    <td><a href="#getrun"><CopyableCode code="getrun" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves the metadata of a run.</td>
</tr>
<tr>
    <td><a href="#deleterun"><CopyableCode code="deleterun" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a non-active run. Returns an error if the run is active.</td>
</tr>
<tr>
    <td><a href="#cancelallruns"><CopyableCode code="cancelallruns" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs from being started.</td>
</tr>
<tr>
    <td><a href="#cancelrun"><CopyableCode code="cancelrun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when this request completes.</td>
</tr>
<tr>
    <td><a href="#exportrun"><CopyableCode code="exportrun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Export and retrieve the job run task.</td>
</tr>
<tr>
    <td><a href="#repairrun"><CopyableCode code="repairrun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job and task settings, and can be viewed in the history for the original job run.</td>
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
    defaultValue="listruns"
    values={[
        { label: 'listruns', value: 'listruns' },
        { label: 'getrun', value: 'getrun' }
    ]}
>
<TabItem value="listruns">

List runs in descending order by start time.

```sql
SELECT
job_id,
job_run_id,
original_attempt_run_id,
run_id,
creator_user_name,
run_name,
attempt_number,
cleanup_duration,
cluster_instance,
cluster_spec,
description,
end_time,
execution_duration,
git_source,
has_more,
job_clusters,
job_parameters,
number_in_job,
overriding_parameters,
queue_duration,
repair_history,
run_duration,
run_page_url,
run_type,
schedule,
setup_duration,
start_time,
state,
status,
tasks,
trigger,
trigger_info
FROM databricks_workspace.workflows.job_runs
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getrun">

Retrieves the metadata of a run.

```sql
SELECT
job_id,
job_run_id,
original_attempt_run_id,
run_id,
creator_user_name,
run_name,
attempt_number,
cleanup_duration,
cluster_instance,
cluster_spec,
description,
end_time,
execution_duration,
git_source,
has_more,
job_clusters,
job_parameters,
next_page_token,
number_in_job,
overriding_parameters,
queue_duration,
repair_history,
run_duration,
run_page_url,
run_type,
schedule,
setup_duration,
start_time,
state,
status,
tasks,
trigger,
trigger_info
FROM databricks_workspace.workflows.job_runs
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deleterun"
    values={[
        { label: 'deleterun', value: 'deleterun' }
    ]}
>
<TabItem value="deleterun">

Deletes a non-active run. Returns an error if the run is active.

```sql
DELETE FROM databricks_workspace.workflows.job_runs
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancelallruns"
    values={[
        { label: 'cancelallruns', value: 'cancelallruns' },
        { label: 'cancelrun', value: 'cancelrun' },
        { label: 'exportrun', value: 'exportrun' },
        { label: 'repairrun', value: 'repairrun' }
    ]}
>
<TabItem value="cancelallruns">

Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new runs from being started.

```sql
EXEC databricks_workspace.workflows.job_runs.cancelallruns 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"job_id": {{ job_id }}, 
"all_queued_runs": {{ all_queued_runs }}
}';
```
</TabItem>
<TabItem value="cancelrun">

Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when this request completes.

```sql
EXEC databricks_workspace.workflows.job_runs.cancelrun 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}"
}';
```
</TabItem>
<TabItem value="exportrun">

Export and retrieve the job run task.

```sql
EXEC databricks_workspace.workflows.job_runs.exportrun 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
<TabItem value="repairrun">

Re-run one or more tasks. Tasks are re-run as part of the original job run. They use the current job and task settings, and can be viewed in the history for the original job run.

```sql
EXEC databricks_workspace.workflows.job_runs.repairrun 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_id": "{{ run_id }}", 
"latest_repair_id": {{ latest_repair_id }}, 
"rerun_tasks": {{ rerun_tasks }}, 
"rerun_all_failed_tasks": "{{ rerun_all_failed_tasks }}", 
"rerun_dependent_tasks": {{ rerun_dependent_tasks }}, 
"job_parameters": "{{ job_parameters }}", 
"pipeline_params": "{{ pipeline_params }}"
}';
```
</TabItem>
</Tabs>
