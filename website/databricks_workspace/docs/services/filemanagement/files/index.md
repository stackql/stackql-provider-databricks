--- 
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
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

Creates, updates, deletes, gets or lists a <code>files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.files" /></td></tr>
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
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a file. If the request is successful, there is no response body.</td>
</tr>
<tr>
    <td><a href="#download"><CopyableCode code="download" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Downloads a file. The file contents are the response body. This is a standard HTTP file download, not a JSON RPC. It supports the Range and If-Unmodified-Since HTTP headers.</td>
</tr>
<tr>
    <td><a href="#upload"><CopyableCode code="upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Uploads a file of up to 5 GiB. The file contents should be sent as the request body as raw bytes (an octet stream); do not encode or otherwise modify the bytes before sending. The contents of the resulting file will be exactly the bytes sent in the request body. If the request is successful, there is no response body.</td>
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

## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a file. If the request is successful, there is no response body.

```sql
DELETE FROM databricks_workspace.filemanagement.files
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="download"
    values={[
        { label: 'download', value: 'download' },
        { label: 'upload', value: 'upload' }
    ]}
>
<TabItem value="download">

Downloads a file. The file contents are the response body. This is a standard HTTP file download, not a JSON RPC. It supports the Range and If-Unmodified-Since HTTP headers.

```sql
EXEC databricks_workspace.filemanagement.files.download 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
<TabItem value="upload">

Uploads a file of up to 5 GiB. The file contents should be sent as the request body as raw bytes (an octet stream); do not encode or otherwise modify the bytes before sending. The contents of the resulting file will be exactly the bytes sent in the request body. If the request is successful, there is no response body.

```sql
EXEC databricks_workspace.filemanagement.files.upload 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
