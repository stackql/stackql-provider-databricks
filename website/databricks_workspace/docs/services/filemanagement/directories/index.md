--- 
title: directories
hide_title: false
hide_table_of_contents: false
keywords:
  - directories
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

Creates, updates, deletes, gets or lists a <code>directories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.directories" /></td></tr>
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
    <td><a href="#createdirectory"><CopyableCode code="createdirectory" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates an empty directory. If necessary, also creates any parent directories of the new, empty directory (like the shell command</td>
</tr>
<tr>
    <td><a href="#deletedirectory"><CopyableCode code="deletedirectory" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an empty directory.</td>
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
    defaultValue="createdirectory"
    values={[
        { label: 'createdirectory', value: 'createdirectory' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createdirectory">

Creates an empty directory. If necessary, also creates any parent directories of the new, empty directory (like the shell command

```sql
INSERT INTO databricks_workspace.filemanagement.directories (
deployment_name
)
SELECT 
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: directories
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the directories resource.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletedirectory"
    values={[
        { label: 'deletedirectory', value: 'deletedirectory' }
    ]}
>
<TabItem value="deletedirectory">

Deletes an empty directory.

```sql
DELETE FROM databricks_workspace.filemanagement.directories
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
