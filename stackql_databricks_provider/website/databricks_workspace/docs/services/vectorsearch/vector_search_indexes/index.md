---
title: vector_search_indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - vector_search_indexes
  - vectorsearch
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

Creates, updates, deletes, gets or lists a <code>vector_search_indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vector_search_indexes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.vector_search_indexes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="vector_search_indexes_get_auto_eval_status"
    values={[
        { label: 'vector_search_indexes_get_auto_eval_status', value: 'vector_search_indexes_get_auto_eval_status' }
    ]}
>
<TabItem value="vector_search_indexes_get_auto_eval_status">

<SchemaTable fields={[
  {
    "name": "job_id",
    "type": "string",
    "description": "Databricks Jobs job_id of the autoeval background-compute job for this index, so the UI can surface a link to the job. Unset when no autoeval job exists for the index yet."
  },
  {
    "name": "end_time_ms",
    "type": "integer",
    "description": ""
  },
  {
    "name": "latest_run",
    "type": "object",
    "description": "State of the latest autoeval run, including stage progress. Populated only while status is AUTO_EVAL_DISPLAY_STATUS_RUNNING and the running wheel has reported at least one stage update. Absent for terminal states.",
    "children": [
      {
        "name": "current_stage",
        "type": "string",
        "description": "Pipeline stage currently in progress. (AUTO_EVAL_STAGE_FEW_SHOT_QUERIES, AUTO_EVAL_STAGE_GENERATE_QUERIES, AUTO_EVAL_STAGE_GENERATE_RESULTS, AUTO_EVAL_STAGE_METRICS_COMPUTATION)"
      },
      {
        "name": "dashboard_url",
        "type": "string",
        "description": "Lakeview dashboard URL for the latest run's results."
      },
      {
        "name": "metrics_table_full_name",
        "type": "string",
        "description": "Fully qualified Delta table name where per-run metrics are persisted (``autoeval_metrics_&lt;index&gt;``)."
      },
      {
        "name": "mlflow_experiment_id",
        "type": "string",
        "description": "MLflow experiment_id used by the autoeval wheel. Stable per index. The UI uses this to construct an \"Open in MLflow\" deep link without an additional MLflow tag fetch."
      },
      {
        "name": "mlflow_run_id",
        "type": "string",
        "description": "MLflow run_id of the latest autoeval run. Per-run, latest only."
      },
      {
        "name": "overall_progress",
        "type": "number",
        "description": "Overall progress across all stages, in the range [0.0, 1.0]. Capped at 0.99 while the run is RUNNING — the bar only reaches 1.0 when status flips to AUTO_EVAL_DISPLAY_STATUS_SUCCEEDED."
      },
      {
        "name": "progress_on_current_stage",
        "type": "integer",
        "description": "Items completed within the current stage (e.g., queries generated, (query_type, reranker, phase) tuples evaluated, results saved)."
      },
      {
        "name": "results_table_full_name",
        "type": "string",
        "description": "Fully qualified Delta table name where per-query results are persisted (``autoeval_results_&lt;index&gt;``)."
      },
      {
        "name": "total_for_current_stage",
        "type": "integer",
        "description": "Total items expected within the current stage."
      }
    ]
  },
  {
    "name": "run_as_user",
    "type": "string",
    "description": "The user the latest job run was created as. Used by the UI to construct the per-run MLflow dashboard URL."
  },
  {
    "name": "state_message",
    "type": "string",
    "description": "Free-form failure copy from the underlying job. Populated only when status is AUTO_EVAL_DISPLAY_STATUS_FAILED. Capped server-side to bound payload size when the job emits long stack traces."
  },
  {
    "name": "status",
    "type": "string",
    "description": "Current display status of the latest autoeval run. (AUTO_EVAL_DISPLAY_STATUS_FAILED, AUTO_EVAL_DISPLAY_STATUS_PENDING, AUTO_EVAL_DISPLAY_STATUS_RUNNING, AUTO_EVAL_DISPLAY_STATUS_SUCCEEDED)"
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
    <td><a href="#vector_search_indexes_get_auto_eval_status"><CopyableCode code="vector_search_indexes_get_auto_eval_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns the status of the latest autoeval run for a vector index.</td>
</tr>
<tr>
    <td><a href="#run_auto_eval"><CopyableCode code="run_auto_eval" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Triggers an autoeval quality evaluation for a vector index.</td>
</tr>
<tr>
    <td><a href="#run_reranker_finetuning"><CopyableCode code="run_reranker_finetuning" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Triggers reranker finetuning for a vector index.</td>
</tr>
<tr>
    <td><a href="#update_index_budget_policy"><CopyableCode code="update_index_budget_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Update the budget policy of an index</td>
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
<tr id="parameter-index_name">
    <td><CopyableCode code="index_name" /></td>
    <td><code>string</code></td>
    <td>Name of the AI Search index</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Fully qualified index name (catalog.schema.index).</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="vector_search_indexes_get_auto_eval_status"
    values={[
        { label: 'vector_search_indexes_get_auto_eval_status', value: 'vector_search_indexes_get_auto_eval_status' }
    ]}
>
<TabItem value="vector_search_indexes_get_auto_eval_status">

Returns the status of the latest autoeval run for a vector index.

```sql
SELECT
job_id,
end_time_ms,
latest_run,
run_as_user,
state_message,
status
FROM databricks_workspace.vectorsearch.vector_search_indexes
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="run_auto_eval"
    values={[
        { label: 'run_auto_eval', value: 'run_auto_eval' },
        { label: 'run_reranker_finetuning', value: 'run_reranker_finetuning' },
        { label: 'update_index_budget_policy', value: 'update_index_budget_policy' }
    ]}
>
<TabItem value="run_auto_eval">

Triggers an autoeval quality evaluation for a vector index.

```sql
EXEC databricks_workspace.vectorsearch.vector_search_indexes.run_auto_eval 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"num_queries": {{ num_queries }}, 
"num_results": {{ num_results }}, 
"query_types": "{{ query_types }}", 
"queryset_query_column": "{{ queryset_query_column }}", 
"queryset_relevant_docs_column": "{{ queryset_relevant_docs_column }}", 
"queryset_table": "{{ queryset_table }}"
}'
;
```
</TabItem>
<TabItem value="run_reranker_finetuning">

Triggers reranker finetuning for a vector index.

```sql
EXEC databricks_workspace.vectorsearch.vector_search_indexes.run_reranker_finetuning 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"embedding_model": "{{ embedding_model }}", 
"model_name": "{{ model_name }}", 
"num_queries": {{ num_queries }}, 
"query_column": "{{ query_column }}", 
"query_table": "{{ query_table }}"
}'
;
```
</TabItem>
<TabItem value="update_index_budget_policy">

Update the budget policy of an index

```sql
EXEC databricks_workspace.vectorsearch.vector_search_indexes.update_index_budget_policy 
@index_name='{{ index_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"usage_policy_id": "{{ usage_policy_id }}"
}'
;
```
</TabItem>
</Tabs>
