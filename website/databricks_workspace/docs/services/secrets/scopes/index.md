--- 
title: scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - scopes
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

Creates, updates, deletes, gets or lists a <code>scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.secrets.scopes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listscopes"
    values={[
        { label: 'listscopes', value: 'listscopes' }
    ]}
>
<TabItem value="listscopes">

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
    <td><CopyableCode code="backend_type" /></td>
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
    <td><a href="#listscopes"><CopyableCode code="listscopes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Lists all secret scopes available in the workspace.</td>
</tr>
<tr>
    <td><a href="#createscope"><CopyableCode code="createscope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>The scope name must consist of alphanumeric characters, dashes, underscores, and periods,  and may not exceed 128 characters.</td>
</tr>
<tr>
    <td><a href="#deletescope"><CopyableCode code="deletescope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a secret scope.</td>
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
    defaultValue="listscopes"
    values={[
        { label: 'listscopes', value: 'listscopes' }
    ]}
>
<TabItem value="listscopes">

Lists all secret scopes available in the workspace.

```sql
SELECT
name,
backend_type
FROM databricks_workspace.secrets.scopes
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createscope"
    values={[
        { label: 'createscope', value: 'createscope' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createscope">

The scope name must consist of alphanumeric characters, dashes, underscores, and periods,  and may not exceed 128 characters.

```sql
INSERT INTO databricks_workspace.secrets.scopes (
data__scope,
data__initial_manage_principal,
data__scope_backend_type,
deployment_name
)
SELECT 
'{{ scope }}',
'{{ initial_manage_principal }}',
'{{ scope_backend_type }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: scopes
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the scopes resource.
    - name: scope
      value: required
    - name: initial_manage_principal
      value: string
    - name: scope_backend_type
      value: string
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletescope"
    values={[
        { label: 'deletescope', value: 'deletescope' }
    ]}
>
<TabItem value="deletescope">

Deletes a secret scope.

```sql
DELETE FROM databricks_workspace.secrets.scopes
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
