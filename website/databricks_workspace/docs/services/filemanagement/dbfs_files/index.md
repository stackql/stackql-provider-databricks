--- 
title: dbfs_files
hide_title: false
hide_table_of_contents: false
keywords:
  - dbfs_files
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

Creates, updates, deletes, gets or lists a <code>dbfs_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.dbfs_files" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="read"
    values={[
        { label: 'read', value: 'read' }
    ]}
>
<TabItem value="read">

Request completed successfully.

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
    <td><CopyableCode code="bytes_read" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
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
    <td><a href="#read"><CopyableCode code="read" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns the contents of a file. If the file does not exist, this call throws an exception with</td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Moves a file from one location to another location within DBFS. If the source file does not exist, this call throws an exception with</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but can also be used as a convenient single call for data upload.</td>
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
    defaultValue="read"
    values={[
        { label: 'read', value: 'read' }
    ]}
>
<TabItem value="read">

Returns the contents of a file. If the file does not exist, this call throws an exception with

```sql
SELECT
bytes_read,
data
FROM databricks_workspace.filemanagement.dbfs_files
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="move"
    values={[
        { label: 'move', value: 'move' },
        { label: 'put', value: 'put' }
    ]}
>
<TabItem value="move">

Moves a file from one location to another location within DBFS. If the source file does not exist, this call throws an exception with

```sql
EXEC databricks_workspace.filemanagement.dbfs_files.move 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"source_path": "{{ source_path }}", 
"destination_path": "{{ destination_path }}"
}';
```
</TabItem>
<TabItem value="put">

Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but can also be used as a convenient single call for data upload.

```sql
EXEC databricks_workspace.filemanagement.dbfs_files.put 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"path": "{{ path }}", 
"contents": "{{ contents }}", 
"overwrite": "{{ overwrite }}"
}';
```
</TabItem>
</Tabs>
