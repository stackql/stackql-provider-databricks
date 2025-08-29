--- 
title: assignable_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - assignable_roles
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

Creates, updates, deletes, gets or lists an <code>assignable_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignable_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.assignable_roles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getassignablerolesforresource"
    values={[
        { label: 'getassignablerolesforresource', value: 'getassignablerolesforresource' }
    ]}
>
<TabItem value="getassignablerolesforresource">

Assignable roles were returned successfully.

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
    <td><CopyableCode code="name" /></td>
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
    <td><a href="#getassignablerolesforresource"><CopyableCode code="getassignablerolesforresource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets all the roles that can be granted on an account level resource. A role is grantable if the rule set on the resource can contain an access rule of the role.</td>
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
    defaultValue="getassignablerolesforresource"
    values={[
        { label: 'getassignablerolesforresource', value: 'getassignablerolesforresource' }
    ]}
>
<TabItem value="getassignablerolesforresource">

Gets all the roles that can be granted on an account level resource. A role is grantable if the rule set on the resource can contain an access rule of the role.

```sql
SELECT
name
FROM databricks_account.iam.assignable_roles;
```
</TabItem>
</Tabs>
