--- 
title: share_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - share_permissions
  - deltasharing
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

Creates, updates, deletes, gets or lists a <code>share_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>share_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.share_permissions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="sharepermissions"
    values={[
        { label: 'sharepermissions', value: 'sharepermissions' }
    ]}
>
<TabItem value="sharepermissions">

The share permissions list was successfully retrieved.

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
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="privileges" /></td>
    <td><code>array</code></td>
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
    <td><a href="#sharepermissions"><CopyableCode code="sharepermissions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the permissions for a data share from the metastore. The caller must be a metastore admin or the owner of the share.</td>
</tr>
<tr>
    <td><a href="#updatepermissions"><CopyableCode code="updatepermissions" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates the permissions for a data share in the metastore. The caller must be a metastore admin or an owner of the share.</td>
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
    defaultValue="sharepermissions"
    values={[
        { label: 'sharepermissions', value: 'sharepermissions' }
    ]}
>
<TabItem value="sharepermissions">

Gets the permissions for a data share from the metastore. The caller must be a metastore admin or the owner of the share.

```sql
SELECT
principal,
privileges
FROM databricks_workspace.deltasharing.share_permissions
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updatepermissions"
    values={[
        { label: 'updatepermissions', value: 'updatepermissions' }
    ]}
>
<TabItem value="updatepermissions">

Updates the permissions for a data share in the metastore. The caller must be a metastore admin or an owner of the share.

```sql
UPDATE databricks_workspace.deltasharing.share_permissions
SET 
data__changes = '{{ changes }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
