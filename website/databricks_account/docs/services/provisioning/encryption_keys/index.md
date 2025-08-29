--- 
title: encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_keys
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

Creates, updates, deletes, gets or lists an <code>encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.encryption_keys" /></td></tr>
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

The encryption key configuration was successfully returned.

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
    <td><CopyableCode code="customer_managed_key_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_key_info" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="use_cases" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

The encryption key configurations were successfully returned.

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
    <td><CopyableCode code="customer_managed_key_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_key_info" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="use_cases" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets a customer-managed key configuration object for an account, specified by ID. This operation uploads a reference to a customer-managed key to Databricks. If assigned as a workspace's customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is specified as a workspace's customer-managed key for storage, the key encrypts the workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume data.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets all customer-managed key configuration objects for an account. If the key is specified as a workspace's managed services customer-managed key, Databricks uses the key to encrypt the workspace's notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If the key is specified as a workspace's storage customer-managed key, the key is used to encrypt the workspace's root S3 bucket and optionally can encrypt cluster EBS volumes data in the data plane.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Creates a customer-managed key configuration object for an account, specified by ID. This operation uploads a reference to a customer-managed key to Databricks. If the key is assigned as a workspace's customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is specified as a workspace's customer-managed key for workspace storage, the key encrypts the workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume data.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a customer-managed key configuration object for an account. You cannot delete a configuration that is associated with a running workspace.</td>
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

Gets a customer-managed key configuration object for an account, specified by ID. This operation uploads a reference to a customer-managed key to Databricks. If assigned as a workspace's customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is specified as a workspace's customer-managed key for storage, the key encrypts the workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume data.

```sql
SELECT
account_id,
customer_managed_key_id,
aws_key_info,
creation_time,
use_cases
FROM databricks_account.provisioning.encryption_keys;
```
</TabItem>
<TabItem value="list">

Gets all customer-managed key configuration objects for an account. If the key is specified as a workspace's managed services customer-managed key, Databricks uses the key to encrypt the workspace's notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If the key is specified as a workspace's storage customer-managed key, the key is used to encrypt the workspace's root S3 bucket and optionally can encrypt cluster EBS volumes data in the data plane.

```sql
SELECT
account_id,
customer_managed_key_id,
aws_key_info,
creation_time,
use_cases
FROM databricks_account.provisioning.encryption_keys;
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

Creates a customer-managed key configuration object for an account, specified by ID. This operation uploads a reference to a customer-managed key to Databricks. If the key is assigned as a workspace's customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is specified as a workspace's customer-managed key for workspace storage, the key encrypts the workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume data.

```sql
INSERT INTO databricks_account.provisioning.encryption_keys (
data__use_cases,
data__aws_key_info
)
SELECT 
'{{ use_cases }}',
'{{ aws_key_info }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: encryption_keys
  props:
    - name: use_cases
      value: required
    - name: aws_key_info
      value: object
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

Deletes a customer-managed key configuration object for an account. You cannot delete a configuration that is associated with a running workspace.

```sql
DELETE FROM databricks_account.provisioning.encryption_keys;
```
</TabItem>
</Tabs>
