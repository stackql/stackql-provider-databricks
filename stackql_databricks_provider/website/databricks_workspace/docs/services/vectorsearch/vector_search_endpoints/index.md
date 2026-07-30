---
title: vector_search_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vector_search_endpoints
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

Creates, updates, deletes, gets or lists a <code>vector_search_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vector_search_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.vector_search_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Update an endpoint</td>
</tr>
<tr>
    <td><a href="#patch_throughput"><CopyableCode code="patch_throughput" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Update the throughput (concurrency) of an endpoint</td>
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
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of the AI Search endpoint</td>
</tr>
</tbody>
</table>

## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an endpoint

```sql
UPDATE databricks_workspace.vectorsearch.vector_search_endpoints
SET 
replication_factor = {{ replication_factor }},
target_qps = {{ target_qps }}
WHERE 
endpoint_name = '{{ endpoint_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
name,
budget_policy_id,
effective_budget_policy_id,
creation_timestamp,
creator,
custom_tags,
endpoint_status,
endpoint_type,
last_updated_timestamp,
last_updated_user,
num_indexes,
scaling_info,
throughput_info;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="patch_throughput"
    values={[
        { label: 'patch_throughput', value: 'patch_throughput' }
    ]}
>
<TabItem value="patch_throughput">

Update the throughput (concurrency) of an endpoint

```sql
EXEC databricks_workspace.vectorsearch.vector_search_endpoints.patch_throughput 
@endpoint_name='{{ endpoint_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"all_or_nothing": {{ all_or_nothing }}, 
"concurrency": {{ concurrency }}, 
"maximum_concurrency_allowed": {{ maximum_concurrency_allowed }}, 
"minimal_concurrency_allowed": {{ minimal_concurrency_allowed }}, 
"num_replicas": {{ num_replicas }}
}'
;
```
</TabItem>
</Tabs>
