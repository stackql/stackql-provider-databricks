--- 
title: private_access
hide_title: false
hide_table_of_contents: false
keywords:
  - private_access
  - provisioning
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

Creates, updates, deletes, gets or lists a <code>private_access</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.private_access" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

The private access settings object was successfully returned.

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
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_settings_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_settings_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="allowed_vpc_endpoint_ids" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_level" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="public_access_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

The private access settings object was successfully returned.

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
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_settings_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_settings_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="allowed_vpc_endpoint_ids" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_level" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="public_access_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets a private access settings object, which specifies how your workspace is accessed over</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets a list of all private access settings objects for an account, specified by ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Creates a private access settings object, which specifies how your workspace is accessed over</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates an existing private access settings object, which specifies how your workspace is accessed over</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a private access settings object, which determines how your workspace is accessed over</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a private access settings object, which specifies how your workspace is accessed over

```sql
SELECT
account_id,
private_access_settings_id,
private_access_settings_name,
allowed_vpc_endpoint_ids,
private_access_level,
public_access_enabled,
region
FROM databricks_account.provisioning.private_access;
```
</TabItem>
<TabItem value="list">

Gets a list of all private access settings objects for an account, specified by ID.

```sql
SELECT
account_id,
private_access_settings_id,
private_access_settings_name,
allowed_vpc_endpoint_ids,
private_access_level,
public_access_enabled,
region
FROM databricks_account.provisioning.private_access;
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

Creates a private access settings object, which specifies how your workspace is accessed over

```sql
INSERT INTO databricks_account.provisioning.private_access (
data__private_access_settings_name,
data__region,
data__public_access_enabled,
data__private_access_level,
data__allowed_vpc_endpoint_ids
)
SELECT 
'{{ private_access_settings_name }}',
'{{ region }}',
'{{ public_access_enabled }}',
'{{ private_access_level }}',
{{ allowed_vpc_endpoint_ids }}
RETURNING
account_id,
private_access_settings_id,
private_access_settings_name,
allowed_vpc_endpoint_ids,
private_access_level,
public_access_enabled,
region
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: private_access
  props:
    - name: private_access_settings_name
      value: required
    - name: region
      value: string
    - name: public_access_enabled
      value: required
    - name: private_access_level
      value: string
    - name: allowed_vpc_endpoint_ids
      value: boolean
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Updates an existing private access settings object, which specifies how your workspace is accessed over

```sql
REPLACE databricks_account.provisioning.private_access
SET 
data__private_access_settings_name = '{{ private_access_settings_name }}',
data__region = '{{ region }}',
data__public_access_enabled = '{{ public_access_enabled }}',
data__private_access_level = '{{ private_access_level }}',
data__allowed_vpc_endpoint_ids = {{ allowed_vpc_endpoint_ids }}
WHERE 
;
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

Deletes a private access settings object, which determines how your workspace is accessed over

```sql
DELETE FROM databricks_account.provisioning.private_access;
```
</TabItem>
</Tabs>
