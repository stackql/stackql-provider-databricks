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
    <td><a href="#vector_search_endpoints_patch_endpoint"><CopyableCode code="vector_search_endpoints_patch_endpoint" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Update an endpoint</td>
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
    <td>Name of the vector search endpoint</td>
</tr>
</tbody>
</table>

## `UPDATE` examples

<Tabs
    defaultValue="vector_search_endpoints_patch_endpoint"
    values={[
        { label: 'vector_search_endpoints_patch_endpoint', value: 'vector_search_endpoints_patch_endpoint' }
    ]}
>
<TabItem value="vector_search_endpoints_patch_endpoint">

Update an endpoint

```sql
UPDATE databricks_workspace.vectorsearch.vector_search_endpoints
SET 
min_qps = {{ min_qps }}
WHERE 
endpoint_name = '{{ endpoint_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
RETURNING
id,
name,
effective_budget_policy_id,
creation_timestamp,
creator,
custom_tags,
endpoint_status,
endpoint_type,
last_updated_timestamp,
last_updated_user,
num_indexes,
scaling_info;
```
</TabItem>
</Tabs>
