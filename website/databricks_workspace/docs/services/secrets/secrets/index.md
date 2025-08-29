--- 
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.secrets.secrets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listsecrets"
    values={[
        { label: 'listsecrets', value: 'listsecrets' },
        { label: 'getsecret', value: 'getsecret' }
    ]}
>
<TabItem value="listsecrets">

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
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated_timestamp" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getsecret">

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
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
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
    <td><a href="#listsecrets"><CopyableCode code="listsecrets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists the secret keys that are stored at this scope.  This is a metadata-only operation; secret data cannot be retrieved using this API.  Users need the READ permission to make this call.</td>
</tr>
<tr>
    <td><a href="#getsecret"><CopyableCode code="getsecret" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the bytes representation of a secret value for the specified scope and key.</td>
</tr>
<tr>
    <td><a href="#putsecret"><CopyableCode code="putsecret" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Inserts a secret under the provided scope with the given name.  If a secret already exists with the same name, this command overwrites the existing secret's value. The server encrypts the secret using the secret scope's encryption settings before storing it.</td>
</tr>
<tr>
    <td><a href="#deletesecret"><CopyableCode code="deletesecret" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the secret stored in this secret scope.  You must have</td>
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
    defaultValue="listsecrets"
    values={[
        { label: 'listsecrets', value: 'listsecrets' },
        { label: 'getsecret', value: 'getsecret' }
    ]}
>
<TabItem value="listsecrets">

Lists the secret keys that are stored at this scope.  This is a metadata-only operation; secret data cannot be retrieved using this API.  Users need the READ permission to make this call.

```sql
SELECT
key,
last_updated_timestamp
FROM databricks_workspace.secrets.secrets
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getsecret">

Gets the bytes representation of a secret value for the specified scope and key.

```sql
SELECT
key,
value
FROM databricks_workspace.secrets.secrets
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="putsecret"
    values={[
        { label: 'putsecret', value: 'putsecret' }
    ]}
>
<TabItem value="putsecret">

Inserts a secret under the provided scope with the given name.  If a secret already exists with the same name, this command overwrites the existing secret's value. The server encrypts the secret using the secret scope's encryption settings before storing it.

```sql
REPLACE databricks_workspace.secrets.secrets
SET 
data__scope = '{{ scope }}',
data__key = '{{ key }}',
data__string_value = '{{ string_value }}',
data__bytes_value = '{{ bytes_value }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletesecret"
    values={[
        { label: 'deletesecret', value: 'deletesecret' }
    ]}
>
<TabItem value="deletesecret">

Deletes the secret stored in this secret scope.  You must have

```sql
DELETE FROM databricks_workspace.secrets.secrets
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
