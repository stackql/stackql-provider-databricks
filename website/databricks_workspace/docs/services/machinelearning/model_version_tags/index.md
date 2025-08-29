--- 
title: model_version_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - model_version_tags
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

Creates, updates, deletes, gets or lists a <code>model_version_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_version_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_version_tags" /></td></tr>
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
    <td><a href="#setmodelversiontag"><CopyableCode code="setmodelversiontag" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Sets a model version tag.</td>
</tr>
<tr>
    <td><a href="#deletemodelversiontag"><CopyableCode code="deletemodelversiontag" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a model version tag.</td>
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
    defaultValue="setmodelversiontag"
    values={[
        { label: 'setmodelversiontag', value: 'setmodelversiontag' }
    ]}
>
<TabItem value="setmodelversiontag">

Sets a model version tag.

```sql
REPLACE databricks_workspace.machinelearning.model_version_tags
SET 
data__name = '{{ name }}',
data__version = '{{ version }}',
data__key = '{{ key }}',
data__value = '{{ value }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletemodelversiontag"
    values={[
        { label: 'deletemodelversiontag', value: 'deletemodelversiontag' }
    ]}
>
<TabItem value="deletemodelversiontag">

Deletes a model version tag.

```sql
DELETE FROM databricks_workspace.machinelearning.model_version_tags
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
