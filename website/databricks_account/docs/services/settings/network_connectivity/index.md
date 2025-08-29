--- 
title: network_connectivity
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connectivity
  - settings
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

Creates, updates, deletes, gets or lists a <code>network_connectivity</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_connectivity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.network_connectivity" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getnetworkconnectivityconfiguration"
    values={[
        { label: 'getnetworkconnectivityconfiguration', value: 'getnetworkconnectivityconfiguration' },
        { label: 'listnetworkconnectivityconfigurations', value: 'listnetworkconnectivityconfigurations' }
    ]}
>
<TabItem value="getnetworkconnectivityconfiguration">

The network connectivity configuration was successfully returned.

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
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="network_connectivity_config_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="egress_config" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_time" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="listnetworkconnectivityconfigurations">

The network connectivity configuration list was successfully retrieved.

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
    <td><CopyableCode code="items" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="next_page_token" /></td>
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
    <td><a href="#getnetworkconnectivityconfiguration"><CopyableCode code="getnetworkconnectivityconfiguration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets a network connectivity configuration.</td>
</tr>
<tr>
    <td><a href="#listnetworkconnectivityconfigurations"><CopyableCode code="listnetworkconnectivityconfigurations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets an array of network connectivity configurations.</td>
</tr>
<tr>
    <td><a href="#createnetworkconnectivityconfiguration"><CopyableCode code="createnetworkconnectivityconfiguration" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Creates a network connectivity configuration (NCC), which provides stable IP CIDR blocks that are associated with your workspace. You can assign an NCC to one or more workspaces in the same region. Once assigned, the workspace serverless compute resources use the same set of stable IP CIDR blocks to access your resources.</td>
</tr>
<tr>
    <td><a href="#deletenetworkconnectivityconfiguration"><CopyableCode code="deletenetworkconnectivityconfiguration" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a network connectivity configuration.</td>
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
    defaultValue="getnetworkconnectivityconfiguration"
    values={[
        { label: 'getnetworkconnectivityconfiguration', value: 'getnetworkconnectivityconfiguration' },
        { label: 'listnetworkconnectivityconfigurations', value: 'listnetworkconnectivityconfigurations' }
    ]}
>
<TabItem value="getnetworkconnectivityconfiguration">

Gets a network connectivity configuration.

```sql
SELECT
name,
account_id,
network_connectivity_config_id,
creation_time,
egress_config,
region,
updated_time
FROM databricks_account.settings.network_connectivity;
```
</TabItem>
<TabItem value="listnetworkconnectivityconfigurations">

Gets an array of network connectivity configurations.

```sql
SELECT
items,
next_page_token
FROM databricks_account.settings.network_connectivity;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createnetworkconnectivityconfiguration"
    values={[
        { label: 'createnetworkconnectivityconfiguration', value: 'createnetworkconnectivityconfiguration' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createnetworkconnectivityconfiguration">

Creates a network connectivity configuration (NCC), which provides stable IP CIDR blocks that are associated with your workspace. You can assign an NCC to one or more workspaces in the same region. Once assigned, the workspace serverless compute resources use the same set of stable IP CIDR blocks to access your resources.

```sql
INSERT INTO databricks_account.settings.network_connectivity (
data__name,
data__region
)
SELECT 
'{{ name }}',
'{{ region }}'
RETURNING
name,
account_id,
network_connectivity_config_id,
creation_time,
egress_config,
region,
updated_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: network_connectivity
  props:
    - name: name
      value: required
    - name: region
      value: uuid
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletenetworkconnectivityconfiguration"
    values={[
        { label: 'deletenetworkconnectivityconfiguration', value: 'deletenetworkconnectivityconfiguration' }
    ]}
>
<TabItem value="deletenetworkconnectivityconfiguration">

Deletes a network connectivity configuration.

```sql
DELETE FROM databricks_account.settings.network_connectivity;
```
</TabItem>
</Tabs>
