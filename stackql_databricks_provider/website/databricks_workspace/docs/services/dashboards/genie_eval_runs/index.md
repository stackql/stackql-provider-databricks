---
title: genie_eval_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - genie_eval_runs
  - dashboards
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

Creates, updates, deletes, gets or lists a <code>genie_eval_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="genie_eval_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.genie_eval_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "eval_run_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_timestamp",
    "type": "integer",
    "description": "Timestamp when the evaluation run was created (milliseconds since epoch)."
  },
  {
    "name": "eval_run_status",
    "type": "string",
    "description": "Current status of the evaluation run. (DONE, EVALUATION_CANCELLED, EVALUATION_FAILED, EVALUATION_TIMEOUT, NOT_STARTED, RUNNING)"
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "Timestamp when the evaluation run was last updated (milliseconds since epoch)."
  },
  {
    "name": "num_correct",
    "type": "integer",
    "description": "Number of questions answered correctly."
  },
  {
    "name": "num_done",
    "type": "integer",
    "description": "Number of questions that have been completed."
  },
  {
    "name": "num_needs_review",
    "type": "integer",
    "description": "Number of questions that need manual review."
  },
  {
    "name": "num_questions",
    "type": "integer",
    "description": "Total number of questions in the evaluation run."
  },
  {
    "name": "run_by_user",
    "type": "integer",
    "description": "User ID who initiated the evaluation run."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "eval_run_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "created_timestamp",
    "type": "integer",
    "description": "Timestamp when the evaluation run was created (milliseconds since epoch)."
  },
  {
    "name": "eval_run_status",
    "type": "string",
    "description": "Current status of the evaluation run. (DONE, EVALUATION_CANCELLED, EVALUATION_FAILED, EVALUATION_TIMEOUT, NOT_STARTED, RUNNING)"
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "Timestamp when the evaluation run was last updated (milliseconds since epoch)."
  },
  {
    "name": "num_correct",
    "type": "integer",
    "description": "Number of questions answered correctly."
  },
  {
    "name": "num_done",
    "type": "integer",
    "description": "Number of questions that have been completed."
  },
  {
    "name": "num_needs_review",
    "type": "integer",
    "description": "Number of questions that need manual review."
  },
  {
    "name": "num_questions",
    "type": "integer",
    "description": "Total number of questions in the evaluation run."
  },
  {
    "name": "run_by_user",
    "type": "integer",
    "description": "User ID who initiated the evaluation run."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-eval_run_id"><code>eval_run_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get evaluation run details.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all evaluation runs in a space.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create and run evaluations for multiple benchmark questions in a Genie space.</td>
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
<tr id="parameter-eval_run_id">
    <td><CopyableCode code="eval_run_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-space_id">
    <td><CopyableCode code="space_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the Genie space where the evaluations will be executed.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of evaluation runs to return per page</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token to get the next page of results</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get evaluation run details.

```sql
SELECT
eval_run_id,
created_timestamp,
eval_run_status,
last_updated_timestamp,
num_correct,
num_done,
num_needs_review,
num_questions,
run_by_user
FROM databricks_workspace.dashboards.genie_eval_runs
WHERE space_id = '{{ space_id }}' -- required
AND eval_run_id = '{{ eval_run_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all evaluation runs in a space.

```sql
SELECT
eval_run_id,
created_timestamp,
eval_run_status,
last_updated_timestamp,
num_correct,
num_done,
num_needs_review,
num_questions,
run_by_user
FROM databricks_workspace.dashboards.genie_eval_runs
WHERE space_id = '{{ space_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
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

Create and run evaluations for multiple benchmark questions in a Genie space.

```sql
INSERT INTO databricks_workspace.dashboards.genie_eval_runs (
benchmark_question_ids,
space_id,
deployment_name
)
SELECT 
'{{ benchmark_question_ids }}',
'{{ space_id }}',
'{{ deployment_name }}'
RETURNING
eval_run_id,
created_timestamp,
eval_run_status,
last_updated_timestamp,
num_correct,
num_done,
num_needs_review,
num_questions,
run_by_user
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: genie_eval_runs
  props:
    - name: space_id
      value: "{{ space_id }}"
      description: Required parameter for the genie_eval_runs resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the genie_eval_runs resource.
    - name: benchmark_question_ids
      value:
        - "{{ benchmark_question_ids }}"
      description: |
        List of benchmark question IDs to evaluate. These questions must exist in the specified Genie space. If none are specified, then all benchmark questions are evaluated.
`}</CodeBlock>

</TabItem>
</Tabs>
