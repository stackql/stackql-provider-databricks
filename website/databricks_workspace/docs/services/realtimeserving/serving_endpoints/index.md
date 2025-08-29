--- 
title: serving_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_endpoints
  - realtimeserving
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

Creates, updates, deletes, gets or lists a <code>serving_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serving_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.realtimeserving.serving_endpoints" /></td></tr>
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

Serving endpoint was retrieved successfully.

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="permission_level" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="route_optimized" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
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
<TabItem value="list">

List of serving endpoints was retrieved successfully.

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ai_gateway" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated_timestamp" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves the details for a single serving endpoint.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#updateconfig"><CopyableCode code="updateconfig" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates any combination of the serving endpoint's served entities, the compute configuration of those served entities, and the endpoint's traffic config. An endpoint that already has an update in progress can not be updated until the current update completes or fails.</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Used to batch add and delete tags from a serving endpoint with a single API call.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Used to update the rate limits of a serving endpoint. NOTE: Only foundation model endpoints are currently supported. For external models, use AI Gateway to manage rate limits.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the details for a single serving endpoint.

```sql
SELECT
id,
name,
config,
creation_timestamp,
creator,
last_updated_timestamp,
permission_level,
route_optimized,
state,
tags
FROM databricks_workspace.realtimeserving.serving_endpoints
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="list">

List of serving endpoints was retrieved successfully.

```sql
SELECT
id,
name,
ai_gateway,
config,
creation_timestamp,
creator,
last_updated_timestamp,
state,
tags,
task
FROM databricks_workspace.realtimeserving.serving_endpoints
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

No description available.

```sql
INSERT INTO databricks_workspace.realtimeserving.serving_endpoints (
data__name,
data__route_optimized,
data__config,
data__tags,
data__rate_limits,
data__ai_gateway,
deployment_name
)
SELECT 
'{{ name }}',
'{{ route_optimized }}',
'{{ config }}',
'{{ tags }}',
'{{ rate_limits }}',
'{{ ai_gateway }}',
'{{ deployment_name }}'
RETURNING
id,
name,
ai_gateway,
config,
creation_timestamp,
creator,
last_updated_timestamp,
permission_level,
route_optimized,
state,
tags
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: serving_endpoints
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the serving_endpoints resource.
    - name: name
      value: required
    - name: route_optimized
      value: string
    - name: config
      value: required
    - name: tags
      value: object
    - name: rate_limits
      value: Array of object
    - name: ai_gateway
      value: Array of object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updateconfig"
    values={[
        { label: 'updateconfig', value: 'updateconfig' },
        { label: 'patch', value: 'patch' }
    ]}
>
<TabItem value="updateconfig">

Updates any combination of the serving endpoint's served entities, the compute configuration of those served entities, and the endpoint's traffic config. An endpoint that already has an update in progress can not be updated until the current update completes or fails.

```sql
UPDATE databricks_workspace.realtimeserving.serving_endpoints
SET 
data__served_entities = '{{ served_entities }}',
data__served_models = '{{ served_models }}',
data__traffic_config = '{{ traffic_config }}',
data__auto_capture_config = '{{ auto_capture_config }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
name,
config,
creation_timestamp,
creator,
last_updated_timestamp,
permission_level,
route_optimized,
state;
```
</TabItem>
<TabItem value="patch">

Used to batch add and delete tags from a serving endpoint with a single API call.

```sql
UPDATE databricks_workspace.realtimeserving.serving_endpoints
SET 
data__delete_tags = '{{ delete_tags }}',
data__add_tags = '{{ add_tags }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
key,
value;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' }
    ]}
>
<TabItem value="put">

Used to update the rate limits of a serving endpoint. NOTE: Only foundation model endpoints are currently supported. For external models, use AI Gateway to manage rate limits.

```sql
REPLACE databricks_workspace.realtimeserving.serving_endpoints
SET 
data__rate_limits = '{{ rate_limits }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
rate_limits;
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

No description available.

```sql
DELETE FROM databricks_workspace.realtimeserving.serving_endpoints
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="query"
    values={[
        { label: 'query', value: 'query' }
    ]}
>
<TabItem value="query">

Serving endpoint was queried successfully and returned predictions.

```sql
EXEC databricks_workspace.realtimeserving.serving_endpoints.query 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"prompt": "{{ prompt }}", 
"input": "{{ input }}", 
"temperature": "{{ temperature }}", 
"stop": "{{ stop }}", 
"max_tokens": {{ max_tokens }}, 
"n": {{ n }}, 
"stream": {{ stream }}, 
"dataframe_records": "{{ dataframe_records }}", 
"instances": "{{ instances }}", 
"inputs": "{{ inputs }}", 
"messages": "{{ messages }}", 
"extra_params": "{{ extra_params }}", 
"dataframe_split": "{{ dataframe_split }}"
}';
```
</TabItem>
</Tabs>
