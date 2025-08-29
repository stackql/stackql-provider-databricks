--- 
title: registered_model_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_model_aliases
  - unitycatalog
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

Creates, updates, deletes, gets or lists a <code>registered_model_aliases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_model_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.registered_model_aliases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#setalias"><CopyableCode code="setalias" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Set an alias on the specified registered model.</td>
</tr>
<tr>
    <td><a href="#deletealias"><CopyableCode code="deletealias" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a registered model alias.</td>
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

## `REPLACE` examples

<Tabs
    defaultValue="setalias"
    values={[
        { label: 'setalias', value: 'setalias' }
    ]}
>
<TabItem value="setalias">

Set an alias on the specified registered model.

```sql
REPLACE databricks_workspace.unitycatalog.registered_model_aliases
SET 
data__full_name = '{{ full_name }}',
data__alias = '{{ alias }}',
data__version_num = '{{ version_num }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
alias_name,
version_num;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletealias"
    values={[
        { label: 'deletealias', value: 'deletealias' }
    ]}
>
<TabItem value="deletealias">

Deletes a registered model alias.

```sql
DELETE FROM databricks_workspace.unitycatalog.registered_model_aliases
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
