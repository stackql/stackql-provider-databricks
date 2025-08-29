--- 
title: dbfs_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - dbfs_streams
  - filemanagement
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

Creates, updates, deletes, gets or lists a <code>dbfs_streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.dbfs_streams" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle timeout on this handle. If a file or directory already exists on the given path and</td>
</tr>
<tr>
    <td><a href="#close"><CopyableCode code="close" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Closes the stream specified by the input handle. If the handle does not exist, this call throws an exception with</td>
</tr>
<tr>
    <td><a href="#addblock"><CopyableCode code="addblock" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Appends a block of data to the stream specified by the input handle. If the handle does not exist, this call will throw an exception with</td>
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

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle timeout on this handle. If a file or directory already exists on the given path and

```sql
INSERT INTO databricks_workspace.filemanagement.dbfs_streams (
data__path,
data__overwrite,
deployment_name
)
SELECT 
'{{ path }}',
'{{ overwrite }}',
'{{ deployment_name }}'
RETURNING
handle
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dbfs_streams
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the dbfs_streams resource.
    - name: path
      value: required
    - name: overwrite
      value: string
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="close"
    values={[
        { label: 'close', value: 'close' }
    ]}
>
<TabItem value="close">

Closes the stream specified by the input handle. If the handle does not exist, this call throws an exception with

```sql
DELETE FROM databricks_workspace.filemanagement.dbfs_streams
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="addblock"
    values={[
        { label: 'addblock', value: 'addblock' }
    ]}
>
<TabItem value="addblock">

Appends a block of data to the stream specified by the input handle. If the handle does not exist, this call will throw an exception with

```sql
EXEC databricks_workspace.filemanagement.dbfs_streams.addblock 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"handle": "{{ handle }}", 
"data": {{ data }}
}';
```
</TabItem>
</Tabs>
