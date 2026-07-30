---
title: feature_materialized
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_materialized
  - ml
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

Creates, updates, deletes, gets or lists a <code>feature_materialized</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_materialized" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_materialized" /></td></tr>
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
    "name": "materialized_feature_id",
    "type": "string",
    "description": "Server-assigned unique identifier for the materialized feature."
  },
  {
    "name": "feature_name",
    "type": "string",
    "description": "The full name of the feature in Unity Catalog."
  },
  {
    "name": "table_name",
    "type": "string",
    "description": "The fully qualified Unity Catalog path to the table containing the materialized feature (Delta table or Lakebase table). Output only."
  },
  {
    "name": "cron_schedule",
    "type": "string",
    "description": "The quartz cron expression that defines the schedule of the materialization pipeline. The schedule is evaluated in the UTC timezone. Hidden from GraphQL: superseded by the ``trigger`` oneof (cron_schedule_trigger), so not exposed to Catalog Explorer."
  },
  {
    "name": "cron_schedule_trigger",
    "type": "object",
    "description": "A cron-based schedule trigger for the materialization pipeline.",
    "children": [
      {
        "name": "cron_expression",
        "type": "string",
        "description": "The cron expression defining the schedule (e.g., \"0 0 * * *\" for daily at midnight)."
      }
    ]
  },
  {
    "name": "is_online",
    "type": "boolean",
    "description": "True if this is an online materialized feature. False if it is an offline materialized feature."
  },
  {
    "name": "last_materialization_time",
    "type": "string",
    "description": "The timestamp when the pipeline last ran and updated the materialized feature values. If the pipeline has not run yet, this field will be null."
  },
  {
    "name": "offline_store_config",
    "type": "object",
    "description": "Destination for writing feature values to an offline Delta table.",
    "children": [
      {
        "name": "catalog_name",
        "type": "string",
        "description": "The Unity Catalog catalog name."
      },
      {
        "name": "schema_name",
        "type": "string",
        "description": "The Unity Catalog schema name."
      },
      {
        "name": "table_name_prefix",
        "type": "string",
        "description": "Prefix for Unity Catalog table name. The materialized feature will be stored in a table with this prefix and a generated postfix."
      }
    ]
  },
  {
    "name": "online_store_config",
    "type": "object",
    "description": "Destination for writing feature values to an online Lakebase table.",
    "children": [
      {
        "name": "catalog_name",
        "type": "string",
        "description": "The Unity Catalog catalog name. This name is also used as the Lakebase logical database name. Quoting is handled by the backend where needed, do not pre-quote it."
      },
      {
        "name": "schema_name",
        "type": "string",
        "description": "The Unity Catalog schema name. This name is also used as the Lakebase schema name under the database. Quoting is handled by the backend where needed, do not pre-quote it."
      },
      {
        "name": "table_name_prefix",
        "type": "string",
        "description": "Prefix for Unity Catalog table name. The materialized feature will be stored in a Lakebase table with this prefix and a generated postfix."
      },
      {
        "name": "online_store_name",
        "type": "string",
        "description": "The name of the target online store."
      }
    ]
  },
  {
    "name": "pipeline_schedule_state",
    "type": "string",
    "description": "The schedule state of the materialization pipeline. Hidden from GraphQL: being deprecated, so not exposed to Catalog Explorer. (ACTIVE, PAUSED, SNAPSHOT)"
  },
  {
    "name": "streaming_mode",
    "type": "object",
    "description": "The Structured Streaming trigger mode used for materialization. Real-time mode (RTM) targets sub-second latency for operational workloads; micro-batch mode (MBM) favors cost efficiency for ETL and analytics workloads.",
    "children": [
      {
        "name": "freshness_target",
        "type": "string",
        "description": "The desired data freshness for feature materialization, expressed as a duration string (e.g. \"1 minute\")."
      },
      {
        "name": "mode",
        "type": "string",
        "description": "The type of streaming mode used by the materialization pipeline. (STREAMING_MODE_TYPE_MBM, STREAMING_MODE_TYPE_RTM)"
      }
    ]
  },
  {
    "name": "table_trigger",
    "type": "object",
    "description": "A trigger that fires when the upstream source table changes."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "materialized_feature_id",
    "type": "string",
    "description": "Server-assigned unique identifier for the materialized feature."
  },
  {
    "name": "feature_name",
    "type": "string",
    "description": "The full name of the feature in Unity Catalog."
  },
  {
    "name": "table_name",
    "type": "string",
    "description": "The fully qualified Unity Catalog path to the table containing the materialized feature (Delta table or Lakebase table). Output only."
  },
  {
    "name": "cron_schedule",
    "type": "string",
    "description": "The quartz cron expression that defines the schedule of the materialization pipeline. The schedule is evaluated in the UTC timezone. Hidden from GraphQL: superseded by the ``trigger`` oneof (cron_schedule_trigger), so not exposed to Catalog Explorer."
  },
  {
    "name": "cron_schedule_trigger",
    "type": "object",
    "description": "A cron-based schedule trigger for the materialization pipeline.",
    "children": [
      {
        "name": "cron_expression",
        "type": "string",
        "description": "The cron expression defining the schedule (e.g., \"0 0 * * *\" for daily at midnight)."
      }
    ]
  },
  {
    "name": "is_online",
    "type": "boolean",
    "description": "True if this is an online materialized feature. False if it is an offline materialized feature."
  },
  {
    "name": "last_materialization_time",
    "type": "string",
    "description": "The timestamp when the pipeline last ran and updated the materialized feature values. If the pipeline has not run yet, this field will be null."
  },
  {
    "name": "offline_store_config",
    "type": "object",
    "description": "Destination for writing feature values to an offline Delta table.",
    "children": [
      {
        "name": "catalog_name",
        "type": "string",
        "description": "The Unity Catalog catalog name."
      },
      {
        "name": "schema_name",
        "type": "string",
        "description": "The Unity Catalog schema name."
      },
      {
        "name": "table_name_prefix",
        "type": "string",
        "description": "Prefix for Unity Catalog table name. The materialized feature will be stored in a table with this prefix and a generated postfix."
      }
    ]
  },
  {
    "name": "online_store_config",
    "type": "object",
    "description": "Destination for writing feature values to an online Lakebase table.",
    "children": [
      {
        "name": "catalog_name",
        "type": "string",
        "description": "The Unity Catalog catalog name. This name is also used as the Lakebase logical database name. Quoting is handled by the backend where needed, do not pre-quote it."
      },
      {
        "name": "schema_name",
        "type": "string",
        "description": "The Unity Catalog schema name. This name is also used as the Lakebase schema name under the database. Quoting is handled by the backend where needed, do not pre-quote it."
      },
      {
        "name": "table_name_prefix",
        "type": "string",
        "description": "Prefix for Unity Catalog table name. The materialized feature will be stored in a Lakebase table with this prefix and a generated postfix."
      },
      {
        "name": "online_store_name",
        "type": "string",
        "description": "The name of the target online store."
      }
    ]
  },
  {
    "name": "pipeline_schedule_state",
    "type": "string",
    "description": "The schedule state of the materialization pipeline. Hidden from GraphQL: being deprecated, so not exposed to Catalog Explorer. (ACTIVE, PAUSED, SNAPSHOT)"
  },
  {
    "name": "streaming_mode",
    "type": "object",
    "description": "The Structured Streaming trigger mode used for materialization. Real-time mode (RTM) targets sub-second latency for operational workloads; micro-batch mode (MBM) favors cost efficiency for ETL and analytics workloads.",
    "children": [
      {
        "name": "freshness_target",
        "type": "string",
        "description": "The desired data freshness for feature materialization, expressed as a duration string (e.g. \"1 minute\")."
      },
      {
        "name": "mode",
        "type": "string",
        "description": "The type of streaming mode used by the materialization pipeline. (STREAMING_MODE_TYPE_MBM, STREAMING_MODE_TYPE_RTM)"
      }
    ]
  },
  {
    "name": "table_trigger",
    "type": "object",
    "description": "A trigger that fires when the upstream source table changes."
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
    <td><a href="#parameter-materialized_feature_id"><code>materialized_feature_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a materialized feature.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List materialized features.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-materialized_feature"><code>materialized_feature</code></a></td>
    <td></td>
    <td>Create a materialized feature.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-materialized_feature_id"><code>materialized_feature_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-materialized_feature"><code>materialized_feature</code></a></td>
    <td></td>
    <td>Update a materialized feature (pause/resume).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-materialized_feature_id"><code>materialized_feature_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a materialized feature.</td>
</tr>
<tr>
    <td><a href="#batch_create"><CopyableCode code="batch_create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-requests"><code>requests</code></a></td>
    <td></td>
    <td>Batch create materialized features.</td>
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
<tr id="parameter-materialized_feature_id">
    <td><CopyableCode code="materialized_feature_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the materialized feature to delete.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>Provide the materialization feature fields which should be updated. Currently, only the pipeline_state field can be updated.</td>
</tr>
<tr id="parameter-feature_name">
    <td><CopyableCode code="feature_name" /></td>
    <td><code>string</code></td>
    <td>Filter by feature name. If specified, only materialized features materialized from this feature will be returned.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of results to return. Defaults to 100 if not specified. Cannot be greater than 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page based on a previous query.</td>
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

Get a materialized feature.

```sql
SELECT
materialized_feature_id,
feature_name,
table_name,
cron_schedule,
cron_schedule_trigger,
is_online,
last_materialization_time,
offline_store_config,
online_store_config,
pipeline_schedule_state,
streaming_mode,
table_trigger
FROM databricks_workspace.ml.feature_materialized
WHERE materialized_feature_id = '{{ materialized_feature_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List materialized features.

```sql
SELECT
materialized_feature_id,
feature_name,
table_name,
cron_schedule,
cron_schedule_trigger,
is_online,
last_materialization_time,
offline_store_config,
online_store_config,
pipeline_schedule_state,
streaming_mode,
table_trigger
FROM databricks_workspace.ml.feature_materialized
WHERE deployment_name = '{{ deployment_name }}' -- required
AND feature_name = '{{ feature_name }}'
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

Create a materialized feature.

```sql
INSERT INTO databricks_workspace.ml.feature_materialized (
materialized_feature,
deployment_name
)
SELECT 
'{{ materialized_feature }}' /* required */,
'{{ deployment_name }}'
RETURNING
materialized_feature_id,
feature_name,
table_name,
cron_schedule,
cron_schedule_trigger,
is_online,
last_materialization_time,
offline_store_config,
online_store_config,
pipeline_schedule_state,
streaming_mode,
table_trigger
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_materialized
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the feature_materialized resource.
    - name: materialized_feature
      description: |
        The materialized feature to create.
      value:
        feature_name: "{{ feature_name }}"
        cron_schedule: "{{ cron_schedule }}"
        cron_schedule_trigger:
          cron_expression: "{{ cron_expression }}"
        is_online: {{ is_online }}
        last_materialization_time: "{{ last_materialization_time }}"
        materialized_feature_id: "{{ materialized_feature_id }}"
        offline_store_config:
          catalog_name: "{{ catalog_name }}"
          schema_name: "{{ schema_name }}"
          table_name_prefix: "{{ table_name_prefix }}"
        online_store_config:
          catalog_name: "{{ catalog_name }}"
          schema_name: "{{ schema_name }}"
          table_name_prefix: "{{ table_name_prefix }}"
          online_store_name: "{{ online_store_name }}"
        pipeline_schedule_state: "{{ pipeline_schedule_state }}"
        streaming_mode:
          freshness_target: "{{ freshness_target }}"
          mode: "{{ mode }}"
        table_name: "{{ table_name }}"
        table_trigger: "{{ table_trigger }}"
`}</CodeBlock>

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

Update a materialized feature (pause/resume).

```sql
UPDATE databricks_workspace.ml.feature_materialized
SET 
materialized_feature = '{{ materialized_feature }}'
WHERE 
materialized_feature_id = '{{ materialized_feature_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND materialized_feature = '{{ materialized_feature }}' --required
RETURNING
materialized_feature_id,
feature_name,
table_name,
cron_schedule,
cron_schedule_trigger,
is_online,
last_materialization_time,
offline_store_config,
online_store_config,
pipeline_schedule_state,
streaming_mode,
table_trigger;
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

Delete a materialized feature.

```sql
DELETE FROM databricks_workspace.ml.feature_materialized
WHERE materialized_feature_id = '{{ materialized_feature_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="batch_create"
    values={[
        { label: 'batch_create', value: 'batch_create' }
    ]}
>
<TabItem value="batch_create">

Batch create materialized features.

```sql
EXEC databricks_workspace.ml.feature_materialized.batch_create 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"requests": "{{ requests }}"
}'
;
```
</TabItem>
</Tabs>
