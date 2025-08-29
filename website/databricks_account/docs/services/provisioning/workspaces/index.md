--- 
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
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

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.workspaces" /></td></tr>
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

The workspace configuration was successfully returned.

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
    <td><CopyableCode code="credentials_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="managed_services_customer_managed_key_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="network_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_settings_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_configuration_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_customer_managed_key_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_no_public_ip_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pricing_tier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_status_message" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

The workspaces were returned successfully.

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
    <td><CopyableCode code="credentials_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="managed_services_customer_managed_key_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="network_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="private_access_settings_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_configuration_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="storage_customer_managed_key_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_no_public_ip_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pricing_tier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_status_message" /></td>
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
    <td>Gets information including status for a Databricks workspace, specified by ID. In the response, the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets a list of all workspaces associated with an account, specified by ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Creates a new workspace using a credential configuration and a storage configuration, an optional network configuration (if using a customer-managed VPC), an optional managed services key configuration (if using customer-managed keys for managed services), and an optional storage key configuration (if using customer-managed keys for storage). The key configurations used for managed services and storage encryption can be the same or different.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Updates a workspace configuration for either a running workspace or a failed workspace. The elements that can be updated varies between these two use cases.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Terminates and deletes a Databricks workspace. From an API perspective, deletion is immediate. However, it might take a few minutes for all workspaces resources to be deleted, depending on the size and number of workspace resources.</td>
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

Gets information including status for a Databricks workspace, specified by ID. In the response, the

```sql
SELECT
account_id,
credentials_id,
managed_services_customer_managed_key_id,
network_id,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
deployment_name,
workspace_name,
aws_region,
creation_time,
custom_tags,
is_no_public_ip_enabled,
pricing_tier,
workspace_status,
workspace_status_message
FROM databricks_account.provisioning.workspaces;
```
</TabItem>
<TabItem value="list">

Gets a list of all workspaces associated with an account, specified by ID.

```sql
SELECT
account_id,
credentials_id,
managed_services_customer_managed_key_id,
network_id,
private_access_settings_id,
storage_configuration_id,
storage_customer_managed_key_id,
workspace_id,
deployment_name,
workspace_name,
aws_region,
creation_time,
custom_tags,
is_no_public_ip_enabled,
pricing_tier,
workspace_status,
workspace_status_message
FROM databricks_account.provisioning.workspaces;
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

Creates a new workspace using a credential configuration and a storage configuration, an optional network configuration (if using a customer-managed VPC), an optional managed services key configuration (if using customer-managed keys for managed services), and an optional storage key configuration (if using customer-managed keys for storage). The key configurations used for managed services and storage encryption can be the same or different.

```sql
INSERT INTO databricks_account.provisioning.workspaces (
data__workspace_name,
data__network_id,
data__deployment_name,
data__aws_region,
data__credentials_id,
data__storage_configuration_id,
data__managed_services_customer_managed_key_id,
data__private_access_settings_id,
data__pricing_tier,
data__storage_customer_managed_key_id,
data__custom_tags
)
SELECT 
'{{ workspace_name }}',
'{{ network_id }}',
'{{ deployment_name }}',
'{{ aws_region }}',
'{{ credentials_id }}',
'{{ storage_configuration_id }}',
'{{ managed_services_customer_managed_key_id }}',
'{{ private_access_settings_id }}',
'{{ pricing_tier }}',
'{{ storage_customer_managed_key_id }}',
'{{ custom_tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: workspaces
  props:
    - name: workspace_name
      value: required
    - name: network_id
      value: string
    - name: deployment_name
      value: uuid
    - name: aws_region
      value: string
    - name: credentials_id
      value: string
    - name: storage_configuration_id
      value: uuid
    - name: managed_services_customer_managed_key_id
      value: uuid
    - name: private_access_settings_id
      value: uuid
    - name: pricing_tier
      value: uuid
    - name: storage_customer_managed_key_id
      value: string
    - name: custom_tags
      value: object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a workspace configuration for either a running workspace or a failed workspace. The elements that can be updated varies between these two use cases.

```sql
UPDATE databricks_account.provisioning.workspaces
SET 
data__aws_region = '{{ aws_region }}',
data__credentials_id = '{{ credentials_id }}',
data__storage_configuration_id = '{{ storage_configuration_id }}',
data__network_id = '{{ network_id }}',
data__managed_services_customer_managed_key_id = '{{ managed_services_customer_managed_key_id }}',
data__private_access_settings_id = '{{ private_access_settings_id }}',
data__storage_customer_managed_key_id = '{{ storage_customer_managed_key_id }}',
data__network_connectivity_config_id = '{{ network_connectivity_config_id }}',
data__custom_tags = '{{ custom_tags }}'
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

Terminates and deletes a Databricks workspace. From an API perspective, deletion is immediate. However, it might take a few minutes for all workspaces resources to be deleted, depending on the size and number of workspace resources.

```sql
DELETE FROM databricks_account.provisioning.workspaces;
```
</TabItem>
</Tabs>
