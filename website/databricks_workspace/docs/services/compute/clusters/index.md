--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.clusters" /></td></tr>
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
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="driver_node_type_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="node_type_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spark_context_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="autotermination_minutes" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_attributes" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_source" /></td>
    <td><code>string</code></td>
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
    <td><CopyableCode code="driver_instance_source" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_elastic_disk" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_local_disk_encryption" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="init_scripts_safe_mode" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="instance_source" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_state_loss_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_workers" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spark_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state_message" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="terminated_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="termination_reason" /></td>
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
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="driver_node_type_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="node_type_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spark_context_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creator_user_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="autotermination_minutes" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_attributes" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cluster_source" /></td>
    <td><code>string</code></td>
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
    <td><CopyableCode code="driver_instance_source" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_elastic_disk" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enable_local_disk_encryption" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="init_scripts_safe_mode" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="instance_source" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_state_loss_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_workers" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spark_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state_message" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="terminated_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="termination_reason" /></td>
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
    <td>Return information about all pinned and active clusters, and all clusters terminated within the last 30 days. Clusters terminated prior to this period are not included.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves the information for a cluster given its identifier. Clusters can be described while they are running, or up to 60 days after they are terminated.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new Spark cluster. This method will acquire new instances from the cloud provider if necessary. This method is asynchronous; the returned</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the configuration of a cluster to match the partial set of attributes and size. Denote which fields to update using the</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the configuration of a cluster to match the provided attributes and size. A cluster can be updated if it is in a</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the termination has completed, the cluster will be in a</td>
</tr>
<tr>
    <td><a href="#changeowner"><CopyableCode code="changeowner" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Change the owner of the cluster. You must be an admin and the cluster must be terminated to perform this operation. The service principal application ID can be supplied as an argument to</td>
</tr>
<tr>
    <td><a href="#permanentdelete"><CopyableCode code="permanentdelete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously removed.</td>
</tr>
<tr>
    <td><a href="#pin"><CopyableCode code="pin" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a cluster that is already pinned will have no effect. This API can only be called by workspace admins.</td>
</tr>
<tr>
    <td><a href="#resize"><CopyableCode code="resize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Starts a terminated Spark cluster with the supplied ID. This works similar to</td>
</tr>
<tr>
    <td><a href="#unpin"><CopyableCode code="unpin" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API. Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace admins.</td>
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

Return information about all pinned and active clusters, and all clusters terminated within the last 30 days. Clusters terminated prior to this period are not included.

```sql
SELECT
cluster_id,
driver_node_type_id,
node_type_id,
spark_context_id,
cluster_name,
creator_user_name,
autotermination_minutes,
aws_attributes,
cluster_source,
default_tags,
disk_spec,
driver_instance_source,
enable_elastic_disk,
enable_local_disk_encryption,
init_scripts_safe_mode,
instance_source,
last_state_loss_time,
num_workers,
spark_version,
start_time,
state,
state_message,
terminated_time,
termination_reason
FROM databricks_workspace.compute.clusters
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="get">

Retrieves the information for a cluster given its identifier. Clusters can be described while they are running, or up to 60 days after they are terminated.

```sql
SELECT
cluster_id,
driver_node_type_id,
node_type_id,
spark_context_id,
cluster_name,
creator_user_name,
autotermination_minutes,
aws_attributes,
cluster_source,
default_tags,
disk_spec,
driver_instance_source,
enable_elastic_disk,
enable_local_disk_encryption,
init_scripts_safe_mode,
instance_source,
last_state_loss_time,
num_workers,
spark_version,
spec,
start_time,
state,
state_message,
terminated_time,
termination_reason
FROM databricks_workspace.compute.clusters
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

Creates a new Spark cluster. This method will acquire new instances from the cloud provider if necessary. This method is asynchronous; the returned

```sql
INSERT INTO databricks_workspace.compute.clusters (
data__num_workers,
data__kind,
data__cluster_name,
data__spark_version,
data__use_ml_runtime,
data__is_single_node,
data__node_type_id,
data__driver_node_type_id,
data__ssh_public_keys,
data__autotermination_minutes,
data__enable_elastic_disk,
data__instance_pool_id,
data__policy_id,
data__enable_local_disk_encryption,
data__driver_instance_pool_id,
data__runtime_engine,
data__data_security_mode,
data__single_user_name,
data__apply_policy_default_values,
data__autoscale,
data__spark_conf,
data__aws_attributes,
data__custom_tags,
data__cluster_log_conf,
data__init_scripts,
data__spark_env_vars,
data__workload_type,
data__docker_image,
data__clone_from,
deployment_name
)
SELECT 
'{{ num_workers }}',
'{{ kind }}',
'{{ cluster_name }}',
'{{ spark_version }}',
'{{ use_ml_runtime }}',
{{ is_single_node }},
{{ node_type_id }},
'{{ driver_node_type_id }}',
'{{ ssh_public_keys }}',
'{{ autotermination_minutes }}',
'{{ enable_elastic_disk }}',
{{ instance_pool_id }},
'{{ policy_id }}',
'{{ enable_local_disk_encryption }}',
{{ driver_instance_pool_id }},
'{{ runtime_engine }}',
'{{ data_security_mode }}',
'{{ single_user_name }}',
'{{ apply_policy_default_values }}',
'{{ autoscale }}',
'{{ spark_conf }}',
'{{ aws_attributes }}',
'{{ custom_tags }}',
'{{ cluster_log_conf }}',
'{{ init_scripts }}',
'{{ spark_env_vars }}',
'{{ workload_type }}',
'{{ docker_image }}',
'{{ clone_from }}',
'{{ deployment_name }}'
RETURNING
cluster_id
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: clusters
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the clusters resource.
    - name: num_workers
      value: int32
    - name: kind
      value: string
    - name: cluster_name
      value: string
    - name: spark_version
      value: required
    - name: use_ml_runtime
      value: string
    - name: is_single_node
      value: boolean
    - name: node_type_id
      value: boolean
    - name: driver_node_type_id
      value: string
    - name: ssh_public_keys
      value: string
    - name: autotermination_minutes
      value: Array of string
    - name: enable_elastic_disk
      value: int32
    - name: instance_pool_id
      value: boolean
    - name: policy_id
      value: string
    - name: enable_local_disk_encryption
      value: string
    - name: driver_instance_pool_id
      value: boolean
    - name: runtime_engine
      value: string
    - name: data_security_mode
      value: string
    - name: single_user_name
      value: string
    - name: apply_policy_default_values
      value: string
    - name: autoscale
      value: object
    - name: spark_conf
      value: object
    - name: aws_attributes
      value: object
    - name: custom_tags
      value: object
    - name: cluster_log_conf
      value: object
    - name: init_scripts
      value: Array of object
    - name: spark_env_vars
      value: object
    - name: workload_type
      value: object
    - name: docker_image
      value: object
    - name: clone_from
      value: object
```
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

Updates the configuration of a cluster to match the partial set of attributes and size. Denote which fields to update using the

```sql
UPDATE databricks_workspace.compute.clusters
SET 
data__cluster_id = '{{ cluster_id }}',
data__update_mask = '{{ update_mask }}',
data__cluster = '{{ cluster }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
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

Updates the configuration of a cluster to match the provided attributes and size. A cluster can be updated if it is in a

```sql
REPLACE databricks_workspace.compute.clusters
SET 
data__cluster_id = '{{ cluster_id }}',
data__num_workers = '{{ num_workers }}',
data__kind = '{{ kind }}',
data__cluster_name = '{{ cluster_name }}',
data__spark_version = '{{ spark_version }}',
data__use_ml_runtime = '{{ use_ml_runtime }}',
data__is_single_node = '{{ is_single_node }}',
data__node_type_id = {{ node_type_id }},
data__driver_node_type_id = {{ driver_node_type_id }},
data__ssh_public_keys = '{{ ssh_public_keys }}',
data__autotermination_minutes = '{{ autotermination_minutes }}',
data__enable_elastic_disk = '{{ enable_elastic_disk }}',
data__instance_pool_id = '{{ instance_pool_id }}',
data__policy_id = {{ policy_id }},
data__enable_local_disk_encryption = '{{ enable_local_disk_encryption }}',
data__driver_instance_pool_id = '{{ driver_instance_pool_id }}',
data__runtime_engine = {{ runtime_engine }},
data__data_security_mode = '{{ data_security_mode }}',
data__single_user_name = '{{ single_user_name }}',
data__apply_policy_default_values = '{{ apply_policy_default_values }}',
data__autoscale = '{{ autoscale }}',
data__spark_conf = '{{ spark_conf }}',
data__aws_attributes = '{{ aws_attributes }}',
data__custom_tags = '{{ custom_tags }}',
data__cluster_log_conf = '{{ cluster_log_conf }}',
data__init_scripts = '{{ init_scripts }}',
data__spark_env_vars = '{{ spark_env_vars }}',
data__workload_type = '{{ workload_type }}',
data__docker_image = '{{ docker_image }}'
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

Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the termination has completed, the cluster will be in a

```sql
DELETE FROM databricks_workspace.compute.clusters
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="changeowner"
    values={[
        { label: 'changeowner', value: 'changeowner' },
        { label: 'permanentdelete', value: 'permanentdelete' },
        { label: 'pin', value: 'pin' },
        { label: 'resize', value: 'resize' },
        { label: 'restart', value: 'restart' },
        { label: 'start', value: 'start' },
        { label: 'unpin', value: 'unpin' }
    ]}
>
<TabItem value="changeowner">

Change the owner of the cluster. You must be an admin and the cluster must be terminated to perform this operation. The service principal application ID can be supplied as an argument to

```sql
EXEC databricks_workspace.compute.clusters.changeowner 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"owner_username": "{{ owner_username }}"
}';
```
</TabItem>
<TabItem value="permanentdelete">

Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously removed.

```sql
EXEC databricks_workspace.compute.clusters.permanentdelete 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}';
```
</TabItem>
<TabItem value="pin">

Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a cluster that is already pinned will have no effect. This API can only be called by workspace admins.

```sql
EXEC databricks_workspace.compute.clusters.pin 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}';
```
</TabItem>
<TabItem value="resize">

Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a

```sql
EXEC databricks_workspace.compute.clusters.resize 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"num_workers": "{{ num_workers }}", 
"cluster_id": "{{ cluster_id }}", 
"autoscale": "{{ autoscale }}"
}';
```
</TabItem>
<TabItem value="restart">

Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a

```sql
EXEC databricks_workspace.compute.clusters.restart 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"restart_user": "{{ restart_user }}"
}';
```
</TabItem>
<TabItem value="start">

Starts a terminated Spark cluster with the supplied ID. This works similar to

```sql
EXEC databricks_workspace.compute.clusters.start 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}';
```
</TabItem>
<TabItem value="unpin">

Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API. Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace admins.

```sql
EXEC databricks_workspace.compute.clusters.unpin 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}"
}';
```
</TabItem>
</Tabs>
