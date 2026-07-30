---
title: clean_room_task_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - clean_room_task_runs
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
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>clean_room_task_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clean_room_task_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.clean_room_task_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="clean_room_task_runs_list_clean_room_task_runs_handler"
    values={[
        { label: 'clean_room_task_runs_list_clean_room_task_runs_handler', value: 'clean_room_task_runs_list_clean_room_task_runs_handler' }
    ]}
>
<TabItem value="clean_room_task_runs_list_clean_room_task_runs_handler">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Name of the executable."
  },
  {
    "name": "analysis_details",
    "type": "object",
    "description": "Information about the analysis run (etag, updated at)",
    "children": [
      {
        "name": "etag",
        "type": "string",
        "description": ""
      },
      {
        "name": "updated_at",
        "type": "integer",
        "description": "The timestamp of when the asset was last updated."
      }
    ]
  },
  {
    "name": "collaborator_job_run_info",
    "type": "object",
    "description": "Job run info of the task in the runner's local workspace. This field is only included in the LIST API if the task was run within the same workspace the API is being called. If the task run was in a different workspace under the same metastore, only the workspace_id is included.",
    "children": [
      {
        "name": "collaborator_alias",
        "type": "string",
        "description": ""
      },
      {
        "name": "collaborator_job_id",
        "type": "integer",
        "description": "Job ID of the task run in the collaborator's workspace."
      },
      {
        "name": "collaborator_job_run_id",
        "type": "integer",
        "description": "Job run ID of the task run in the collaborator's workspace."
      },
      {
        "name": "collaborator_task_run_id",
        "type": "integer",
        "description": "Task run ID of the task run in the collaborator's workspace."
      },
      {
        "name": "collaborator_workspace_id",
        "type": "integer",
        "description": "ID of the collaborator's workspace that triggered the task run."
      }
    ]
  },
  {
    "name": "output_info",
    "type": "object",
    "description": "Information about run output",
    "children": [
      {
        "name": "output_schema_expiration_time",
        "type": "integer",
        "description": ""
      },
      {
        "name": "output_schema_name",
        "type": "string",
        "description": "Name of the output schema associated with the clean room task run."
      }
    ]
  },
  {
    "name": "run_duration",
    "type": "integer",
    "description": "Duration of the task run, in milliseconds."
  },
  {
    "name": "shared_output_info",
    "type": "object",
    "description": "Information about shared output accessible by all collaborators. This field is only populated when enable_shared_output is true.",
    "children": [
      {
        "name": "output_schema_expiration_time",
        "type": "integer",
        "description": ""
      },
      {
        "name": "output_schema_name",
        "type": "string",
        "description": "Name of the output schema associated with the clean room task run."
      }
    ]
  },
  {
    "name": "start_time",
    "type": "integer",
    "description": "When the task run started, in epoch milliseconds."
  },
  {
    "name": "task_run_state",
    "type": "string",
    "description": "State of the task run."
  },
  {
    "name": "task_type",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (JAR, NOTEBOOK)"
  }
]} />
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
    <td><a href="#clean_room_task_runs_list_clean_room_task_runs_handler"><CopyableCode code="clean_room_task_runs_list_clean_room_task_runs_handler" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-clean_room_name"><code>clean_room_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-task_type"><code>task_type</code></a></td>
    <td>List all the historical task runs in a clean room.</td>
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
<tr id="parameter-clean_room_name">
    <td><CopyableCode code="clean_room_name" /></td>
    <td><code>string</code></td>
    <td>Name of the clean room.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Executable name.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of task runs to return. Maximum value of 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
<tr id="parameter-task_type">
    <td><CopyableCode code="task_type" /></td>
    <td><code>string</code></td>
    <td>Filter by the type of Clean Room task.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="clean_room_task_runs_list_clean_room_task_runs_handler"
    values={[
        { label: 'clean_room_task_runs_list_clean_room_task_runs_handler', value: 'clean_room_task_runs_list_clean_room_task_runs_handler' }
    ]}
>
<TabItem value="clean_room_task_runs_list_clean_room_task_runs_handler">

List all the historical task runs in a clean room.

```sql
SELECT
name,
analysis_details,
collaborator_job_run_info,
output_info,
run_duration,
shared_output_info,
start_time,
task_run_state,
task_type
FROM databricks_workspace.cleanrooms.clean_room_task_runs
WHERE clean_room_name = '{{ clean_room_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND name = '{{ name }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND task_type = '{{ task_type }}'
;
```
</TabItem>
</Tabs>
