--- 
title: workspace_permission_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_permission_assignments
  - iam
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>workspace_permission_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_permission_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.workspace_permission_assignments" /></td></tr>
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
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
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
    <td></td>
    <td></td>
    <td>Get the permission assignments for the specified Databricks account and Databricks workspace.</td>
</tr>
<tr>
    <td><a href="#createorupdate"><CopyableCode code="createorupdate" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Creates or updates the workspace permissions assignment in a given account and workspace for the specified principal.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes the workspace permissions assignment in a given account and workspace for the specified principal.</td>
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

Get the permission assignments for the specified Databricks account and Databricks workspace.

```sql
SELECT
error,
permissions,
principal
FROM databricks_account.iam.workspace_permission_assignments;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createorupdate"
    values={[
        { label: 'createorupdate', value: 'createorupdate' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createorupdate">

Creates or updates the workspace permissions assignment in a given account and workspace for the specified principal.

```sql
INSERT INTO databricks_account.iam.workspace_permission_assignments (
data__permissions
)
SELECT 
'{{ permissions }}'
RETURNING
error,
permissions,
principal
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: workspace_permission_assignments
  props:
    - name: permissions
      value: Array of string
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

Deletes the workspace permissions assignment in a given account and workspace for the specified principal.

```sql
DELETE FROM databricks_account.iam.workspace_permission_assignments;
```
</TabItem>
</Tabs>
