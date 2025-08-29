--- 
title: warehouses
hide_title: false
hide_table_of_contents: false
keywords:
  - warehouses
  - dbsql
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

Creates, updates, deletes, gets or lists a <code>warehouses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warehouses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.warehouses" /></td></tr>
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
    <td><CopyableCode code="creator_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="auto_stop_mins" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="channel" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_size" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_photon" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_serverless_compute" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="instance_profile_arn" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="jdbc_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_num_clusters" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="min_num_clusters" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_active_sessions" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_clusters" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="odbc_params" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spot_instance_policy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="creator_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="auto_stop_mins" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="channel" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_size" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_photon" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_serverless_compute" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="instance_profile_arn" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="jdbc_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_num_clusters" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="min_num_clusters" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_active_sessions" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_clusters" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="odbc_params" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spot_instance_policy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_type" /></td>
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
    <td>Gets the information for a single SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists all SQL warehouses that a user has manager permissions on.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the configuration for a SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Starts a SQL warehouse.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Stops a SQL warehouse.</td>
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

Gets the information for a single SQL warehouse.

```sql
SELECT
id,
name,
creator_name,
auto_stop_mins,
channel,
cluster_size,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type
FROM databricks_workspace.dbsql.warehouses
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="list">

Lists all SQL warehouses that a user has manager permissions on.

```sql
SELECT
id,
name,
creator_name,
auto_stop_mins,
channel,
cluster_size,
enable_photon,
enable_serverless_compute,
health,
instance_profile_arn,
jdbc_url,
max_num_clusters,
min_num_clusters,
num_active_sessions,
num_clusters,
odbc_params,
spot_instance_policy,
state,
tags,
warehouse_type
FROM databricks_workspace.dbsql.warehouses
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

Creates a new SQL warehouse.

```sql
INSERT INTO databricks_workspace.dbsql.warehouses (
data__name,
data__cluster_size,
data__min_num_clusters,
data__max_num_clusters,
data__auto_stop_mins,
data__creator_name,
data__instance_profile_arn,
data__spot_instance_policy,
data__enable_photon,
data__enable_serverless_compute,
data__warehouse_type,
data__tags,
data__channel,
deployment_name
)
SELECT 
'{{ name }}',
'{{ cluster_size }}',
'{{ min_num_clusters }}',
'{{ max_num_clusters }}',
'{{ auto_stop_mins }}',
'{{ creator_name }}',
'{{ instance_profile_arn }}',
'{{ spot_instance_policy }}',
{{ enable_photon }},
{{ enable_serverless_compute }},
'{{ warehouse_type }}',
'{{ tags }}',
'{{ channel }}',
'{{ deployment_name }}'
RETURNING
id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: warehouses
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the warehouses resource.
    - name: name
      value: string
    - name: cluster_size
      value: string
    - name: min_num_clusters
      value: int32
    - name: max_num_clusters
      value: int32
    - name: auto_stop_mins
      value: int32
    - name: creator_name
      value: string
    - name: instance_profile_arn
      value: string
    - name: spot_instance_policy
      value: string
    - name: enable_photon
      value: boolean
    - name: enable_serverless_compute
      value: boolean
    - name: warehouse_type
      value: string
    - name: tags
      value: object
    - name: channel
      value: object
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Updates the configuration for a SQL warehouse.

```sql
REPLACE databricks_workspace.dbsql.warehouses
SET 
data__name = '{{ name }}',
data__cluster_size = '{{ cluster_size }}',
data__min_num_clusters = '{{ min_num_clusters }}',
data__max_num_clusters = '{{ max_num_clusters }}',
data__auto_stop_mins = '{{ auto_stop_mins }}',
data__creator_name = '{{ creator_name }}',
data__instance_profile_arn = '{{ instance_profile_arn }}',
data__spot_instance_policy = '{{ spot_instance_policy }}',
data__enable_photon = {{ enable_photon }},
data__enable_serverless_compute = {{ enable_serverless_compute }},
data__warehouse_type = '{{ warehouse_type }}',
data__tags = '{{ tags }}',
data__channel = '{{ channel }}'
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

Deletes a SQL warehouse.

```sql
DELETE FROM databricks_workspace.dbsql.warehouses
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Starts a SQL warehouse.

```sql
EXEC databricks_workspace.dbsql.warehouses.start 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
<TabItem value="stop">

Stops a SQL warehouse.

```sql
EXEC databricks_workspace.dbsql.warehouses.stop 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
