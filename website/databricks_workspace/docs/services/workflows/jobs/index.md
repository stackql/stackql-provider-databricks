--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workflows.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="job_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_more" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get">

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
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="run_as_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_more" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="next_page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
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
    <td>Retrieves a list of jobs.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves the details for a single job.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create a new job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Add, update, or remove specific settings of an existing job. Use the</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Overwrite all settings for the given job. Use the</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a job.</td>
</tr>
<tr>
    <td><a href="#runnow"><CopyableCode code="runnow" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Run a job and return the</td>
</tr>
<tr>
    <td><a href="#submit"><CopyableCode code="submit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job. Runs submitted using this endpoint don’t display in the UI. Use the</td>
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
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

Retrieves a list of jobs.

```sql
SELECT
job_id,
creator_user_name,
created_time,
has_more,
settings
FROM databricks_workspace.workflows.jobs
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="get">

Retrieves the details for a single job.

```sql
SELECT
job_id,
creator_user_name,
run_as_user_name,
created_time,
has_more,
next_page_token,
settings
FROM databricks_workspace.workflows.jobs
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

Create a new job.

```sql
INSERT INTO databricks_workspace.workflows.jobs (
data__name,
data__description,
data__timeout_seconds,
data__max_concurrent_runs,
data__format,
data__edit_mode,
data__email_notifications,
data__webhook_notifications,
data__notification_settings,
data__health,
data__schedule,
data__trigger,
data__continuous,
data__tasks,
data__job_clusters,
data__git_source,
data__tags,
data__queue,
data__parameters,
data__run_as,
data__deployment,
data__environments,
data__access_control_list,
deployment_name
)
SELECT 
'{{ name }}',
'{{ description }}',
'{{ timeout_seconds }}',
'{{ max_concurrent_runs }}',
'{{ format }}',
'{{ edit_mode }}',
'{{ email_notifications }}',
'{{ webhook_notifications }}',
'{{ notification_settings }}',
'{{ health }}',
'{{ schedule }}',
'{{ trigger }}',
'{{ continuous }}',
'{{ tasks }}',
'{{ job_clusters }}',
'{{ git_source }}',
'{{ tags }}',
'{{ queue }}',
'{{ parameters }}',
'{{ run_as }}',
'{{ deployment }}',
'{{ environments }}',
'{{ access_control_list }}',
'{{ deployment_name }}'
RETURNING
job_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: jobs
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the jobs resource.
    - name: name
      value: string
    - name: description
      value: string
    - name: timeout_seconds
      value: int32
    - name: max_concurrent_runs
      value: int32
    - name: format
      value: string
    - name: edit_mode
      value: string
    - name: email_notifications
      value: object
    - name: webhook_notifications
      value: object
    - name: notification_settings
      value: object
    - name: health
      value: object
    - name: schedule
      value: object
    - name: trigger
      value: object
    - name: continuous
      value: object
    - name: tasks
      value: Array of object
    - name: job_clusters
      value: Array of object
    - name: git_source
      value: object
    - name: tags
      value: object
    - name: queue
      value: object
    - name: parameters
      value: Array of object
    - name: run_as
      value: object
    - name: deployment
      value: object
    - name: environments
      value: Array of object
    - name: access_control_list
      value: Array of object
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

Add, update, or remove specific settings of an existing job. Use the

```sql
UPDATE databricks_workspace.workflows.jobs
SET 
data__job_id = '{{ job_id }}',
data__fields_to_remove = {{ fields_to_remove }},
data__new_settings = '{{ new_settings }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="reset"
    values={[
        { label: 'reset', value: 'reset' }
    ]}
>
<TabItem value="reset">

Overwrite all settings for the given job. Use the

```sql
REPLACE databricks_workspace.workflows.jobs
SET 
data__job_id = '{{ job_id }}',
data__new_settings = '{{ new_settings }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
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

Deletes a job.

```sql
DELETE FROM databricks_workspace.workflows.jobs
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="runnow"
    values={[
        { label: 'runnow', value: 'runnow' },
        { label: 'submit', value: 'submit' }
    ]}
>
<TabItem value="runnow">

Run a job and return the

```sql
EXEC databricks_workspace.workflows.jobs.runnow 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"job_id": "{{ job_id }}", 
"idempotency_token": {{ idempotency_token }}, 
"job_parameters": "{{ job_parameters }}", 
"pipeline_params": "{{ pipeline_params }}", 
"queue": "{{ queue }}"
}';
```
</TabItem>
<TabItem value="submit">

Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job. Runs submitted using this endpoint don’t display in the UI. Use the

```sql
EXEC databricks_workspace.workflows.jobs.submit 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"run_name": "{{ run_name }}", 
"timeout_seconds": "{{ timeout_seconds }}", 
"idempotency_token": "{{ idempotency_token }}", 
"health": "{{ health }}", 
"tasks": "{{ tasks }}", 
"git_source": "{{ git_source }}", 
"webhook_notifications": "{{ webhook_notifications }}", 
"email_notifications": "{{ email_notifications }}", 
"notification_settings": "{{ notification_settings }}", 
"environments": "{{ environments }}", 
"access_control_list": "{{ access_control_list }}", 
"queue": "{{ queue }}", 
"run_as": "{{ run_as }}"
}';
```
</TabItem>
</Tabs>
