--- 
title: instance_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_pools
  - compute
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

Creates, updates, deletes, gets or lists an <code>instance_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.instance_pools" /></td></tr>
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
    <td><CopyableCode code="instance_pool_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="node_type_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="instance_pool_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_attributes" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="default_tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="disk_spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_elastic_disk" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="idle_instance_autotermination_minutes" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="min_idle_instances" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="preloaded_spark_versions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
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
    <td><CopyableCode code="instance_pool_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="node_type_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="instance_pool_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_attributes" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="default_tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="disk_spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_elastic_disk" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="idle_instance_autotermination_minutes" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="min_idle_instances" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="preloaded_spark_versions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
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
    <td>Gets a list of instance pools with their statistics.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieve the information for an instance pool based on its identifier.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new instance pool using idle and ready-to-use cloud instances.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Modifies the configuration of an existing instance pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously.</td>
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

Gets a list of instance pools with their statistics.

```sql
SELECT
instance_pool_id,
node_type_id,
instance_pool_name,
aws_attributes,
default_tags,
disk_spec,
enable_elastic_disk,
idle_instance_autotermination_minutes,
min_idle_instances,
preloaded_spark_versions,
state,
stats,
status
FROM databricks_workspace.compute.instance_pools
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="get">

Retrieve the information for an instance pool based on its identifier.

```sql
SELECT
instance_pool_id,
node_type_id,
instance_pool_name,
aws_attributes,
custom_tags,
default_tags,
disk_spec,
enable_elastic_disk,
idle_instance_autotermination_minutes,
min_idle_instances,
preloaded_spark_versions,
state,
stats,
status
FROM databricks_workspace.compute.instance_pools
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

Creates a new instance pool using idle and ready-to-use cloud instances.

```sql
INSERT INTO databricks_workspace.compute.instance_pools (
data__instance_pool_name,
data__min_idle_instances,
data__max_capacity,
data__node_type_id,
data__idle_instance_autotermination_minutes,
data__enable_elastic_disk,
data__preloaded_spark_versions,
data__aws_attributes,
data__custom_tags,
data__disk_spec,
data__preloaded_docker_images,
deployment_name
)
SELECT 
'{{ instance_pool_name }}',
'{{ min_idle_instances }}',
'{{ max_capacity }}',
'{{ node_type_id }}',
'{{ idle_instance_autotermination_minutes }}',
'{{ enable_elastic_disk }}',
'{{ preloaded_spark_versions }}',
'{{ aws_attributes }}',
'{{ custom_tags }}',
'{{ disk_spec }}',
'{{ preloaded_docker_images }}',
'{{ deployment_name }}'
RETURNING
instance_pool_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: instance_pools
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the instance_pools resource.
    - name: instance_pool_name
      value: required
    - name: min_idle_instances
      value: string
    - name: max_capacity
      value: int32
    - name: node_type_id
      value: int32
    - name: idle_instance_autotermination_minutes
      value: required
    - name: enable_elastic_disk
      value: string
    - name: preloaded_spark_versions
      value: int32
    - name: aws_attributes
      value: object
    - name: custom_tags
      value: object
    - name: disk_spec
      value: object
    - name: preloaded_docker_images
      value: Array of object
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

Modifies the configuration of an existing instance pool.

```sql
REPLACE databricks_workspace.compute.instance_pools
SET 
data__instance_pool_name = '{{ instance_pool_name }}',
data__min_idle_instances = '{{ min_idle_instances }}',
data__max_capacity = '{{ max_capacity }}',
data__idle_instance_autotermination_minutes = '{{ idle_instance_autotermination_minutes }}',
data__instance_pool_id = '{{ instance_pool_id }}',
data__node_type_id = '{{ node_type_id }}',
data__custom_tags = '{{ custom_tags }}'
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

Deletes the instance pool permanently. The idle instances in the pool are terminated asynchronously.

```sql
DELETE FROM databricks_workspace.compute.instance_pools
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
