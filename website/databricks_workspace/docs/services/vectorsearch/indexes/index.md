--- 
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.indexes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getindex"
    values={[
        { label: 'getindex', value: 'getindex' },
        { label: 'listindexes', value: 'listindexes' }
    ]}
>
<TabItem value="getindex">

Successful response with details of the index

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delta_sync_index_spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="index_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="primary_key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="listindexes">

Successful response with list of endpoints.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="index_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="primary_key" /></td>
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
    <td><a href="#getindex"><CopyableCode code="getindex" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get an index.</td>
</tr>
<tr>
    <td><a href="#listindexes"><CopyableCode code="listindexes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>List all indexes in the given endpoint.</td>
</tr>
<tr>
    <td><a href="#createindex"><CopyableCode code="createindex" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create a new index.</td>
</tr>
<tr>
    <td><a href="#deleteindex"><CopyableCode code="deleteindex" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete an index.</td>
</tr>
<tr>
    <td><a href="#querynextpage"><CopyableCode code="querynextpage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Use</td>
</tr>
<tr>
    <td><a href="#syncindex"><CopyableCode code="syncindex" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Triggers a synchronization process for a specified vector index.</td>
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
    defaultValue="getindex"
    values={[
        { label: 'getindex', value: 'getindex' },
        { label: 'listindexes', value: 'listindexes' }
    ]}
>
<TabItem value="getindex">

Get an index.

```sql
SELECT
name,
endpoint_name,
creator,
delta_sync_index_spec,
index_type,
primary_key,
status
FROM databricks_workspace.vectorsearch.indexes
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listindexes">

List all indexes in the given endpoint.

```sql
SELECT
name,
endpoint_name,
creator,
index_type,
primary_key
FROM databricks_workspace.vectorsearch.indexes
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createindex"
    values={[
        { label: 'createindex', value: 'createindex' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createindex">

Create a new index.

```sql
INSERT INTO databricks_workspace.vectorsearch.indexes (
data__name,
data__endpoint_name,
data__primary_key,
data__index_type,
data__delta_sync_index_spec,
data__direct_access_index_spec,
deployment_name
)
SELECT 
'{{ name }}',
'{{ endpoint_name }}',
'{{ primary_key }}',
'{{ index_type }}',
'{{ delta_sync_index_spec }}',
'{{ direct_access_index_spec }}',
'{{ deployment_name }}'
RETURNING
name,
endpoint_name,
creator,
delta_sync_index_spec,
index_type,
primary_key,
status
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: indexes
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the indexes resource.
    - name: name
      value: required
    - name: endpoint_name
      value: string
    - name: primary_key
      value: required
    - name: index_type
      value: string
    - name: delta_sync_index_spec
      value: object
    - name: direct_access_index_spec
      value: object
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deleteindex"
    values={[
        { label: 'deleteindex', value: 'deleteindex' }
    ]}
>
<TabItem value="deleteindex">

Delete an index.

```sql
DELETE FROM databricks_workspace.vectorsearch.indexes
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="querynextpage"
    values={[
        { label: 'querynextpage', value: 'querynextpage' },
        { label: 'syncindex', value: 'syncindex' }
    ]}
>
<TabItem value="querynextpage">

Use

```sql
EXEC databricks_workspace.vectorsearch.indexes.querynextpage 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"endpoint_name": "{{ endpoint_name }}", 
"page_token": "{{ page_token }}"
}';
```
</TabItem>
<TabItem value="syncindex">

Triggers a synchronization process for a specified vector index.

```sql
EXEC databricks_workspace.vectorsearch.indexes.syncindex 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
