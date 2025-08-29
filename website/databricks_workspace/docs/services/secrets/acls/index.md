--- 
title: acls
hide_title: false
hide_table_of_contents: false
keywords:
  - acls
  - secrets
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

Creates, updates, deletes, gets or lists an <code>acls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.secrets.acls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listacls"
    values={[
        { label: 'listacls', value: 'listacls' },
        { label: 'getacl', value: 'getacl' }
    ]}
>
<TabItem value="listacls">

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
    <td><CopyableCode code="permission" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getacl">

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
    <td><CopyableCode code="permission" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
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
    <td><a href="#listacls"><CopyableCode code="listacls" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>List the ACLs for a given secret scope. Users must have the</td>
</tr>
<tr>
    <td><a href="#getacl"><CopyableCode code="getacl" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the details about the given ACL, such as the group and permission. Users must have the</td>
</tr>
<tr>
    <td><a href="#putacl"><CopyableCode code="putacl" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates or overwrites the Access Control List (ACL) associated with the given principal (user or group) on the specified scope point.</td>
</tr>
<tr>
    <td><a href="#deleteacl"><CopyableCode code="deleteacl" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the given ACL on the given scope.</td>
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
    defaultValue="listacls"
    values={[
        { label: 'listacls', value: 'listacls' },
        { label: 'getacl', value: 'getacl' }
    ]}
>
<TabItem value="listacls">

List the ACLs for a given secret scope. Users must have the

```sql
SELECT
permission,
principal
FROM databricks_workspace.secrets.acls
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getacl">

Gets the details about the given ACL, such as the group and permission. Users must have the

```sql
SELECT
permission,
principal
FROM databricks_workspace.secrets.acls
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="putacl"
    values={[
        { label: 'putacl', value: 'putacl' }
    ]}
>
<TabItem value="putacl">

Creates or overwrites the Access Control List (ACL) associated with the given principal (user or group) on the specified scope point.

```sql
REPLACE databricks_workspace.secrets.acls
SET 
data__scope = '{{ scope }}',
data__principal = '{{ principal }}',
data__permission = '{{ permission }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deleteacl"
    values={[
        { label: 'deleteacl', value: 'deleteacl' }
    ]}
>
<TabItem value="deleteacl">

Deletes the given ACL on the given scope.

```sql
DELETE FROM databricks_workspace.secrets.acls
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
