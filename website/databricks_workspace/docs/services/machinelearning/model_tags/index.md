--- 
title: model_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - model_tags
  - machinelearning
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

Creates, updates, deletes, gets or lists a <code>model_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_tags" /></td></tr>
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
    <td><a href="#setmodeltag"><CopyableCode code="setmodeltag" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Sets a tag on a registered model.</td>
</tr>
<tr>
    <td><a href="#deletemodeltag"><CopyableCode code="deletemodeltag" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes the tag for a registered model.</td>
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
    defaultValue="setmodeltag"
    values={[
        { label: 'setmodeltag', value: 'setmodeltag' }
    ]}
>
<TabItem value="setmodeltag">

Sets a tag on a registered model.

```sql
REPLACE databricks_workspace.machinelearning.model_tags
SET 
data__name = '{{ name }}',
data__key = '{{ key }}',
data__value = '{{ value }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletemodeltag"
    values={[
        { label: 'deletemodeltag', value: 'deletemodeltag' }
    ]}
>
<TabItem value="deletemodeltag">

Deletes the tag for a registered model.

```sql
DELETE FROM databricks_workspace.machinelearning.model_tags
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
