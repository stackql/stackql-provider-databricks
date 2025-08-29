--- 
title: dbfs_directories
hide_title: false
hide_table_of_contents: false
keywords:
  - dbfs_directories
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

Creates, updates, deletes, gets or lists a <code>dbfs_directories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs_directories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.dbfs_directories" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

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
    <td><CopyableCode code="file_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_dir" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modification_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>List the contents of a directory, or details of the file. If the file or directory does not exist, this call throws an exception with</td>
</tr>
<tr>
    <td><a href="#mkdirs"><CopyableCode code="mkdirs" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates the given directory and necessary parent directories if they do not exist. If a file (not a directory) exists at any prefix of the input path, this call throws an exception with</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List the contents of a directory, or details of the file. If the file or directory does not exist, this call throws an exception with

```sql
SELECT
file_size,
is_dir,
modification_time,
path
FROM databricks_workspace.filemanagement.dbfs_directories
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="mkdirs"
    values={[
        { label: 'mkdirs', value: 'mkdirs' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="mkdirs">

Creates the given directory and necessary parent directories if they do not exist. If a file (not a directory) exists at any prefix of the input path, this call throws an exception with

```sql
INSERT INTO databricks_workspace.filemanagement.dbfs_directories (
data__path,
deployment_name
)
SELECT 
'{{ path }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dbfs_directories
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the dbfs_directories resource.
    - name: path
      value: required
```
</TabItem>
</Tabs>
