--- 
title: model_version_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - model_version_comments
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

Creates, updates, deletes, gets or lists a <code>model_version_comments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_version_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_version_comments" /></td></tr>
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
    <td><a href="#createcomment"><CopyableCode code="createcomment" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Posts a comment on a model version. A comment can be submitted either by a user or programmatically to display relevant information about the model. For example, test results or deployment errors.</td>
</tr>
<tr>
    <td><a href="#updatecomment"><CopyableCode code="updatecomment" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Post an edit to a comment on a model version.</td>
</tr>
<tr>
    <td><a href="#deletecomment"><CopyableCode code="deletecomment" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a comment on a model version.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="createcomment"
    values={[
        { label: 'createcomment', value: 'createcomment' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createcomment">

Posts a comment on a model version. A comment can be submitted either by a user or programmatically to display relevant information about the model. For example, test results or deployment errors.

```sql
INSERT INTO databricks_workspace.machinelearning.model_version_comments (
data__name,
data__version,
data__comment,
deployment_name
)
SELECT 
'{{ name }}',
'{{ version }}',
'{{ comment }}',
'{{ deployment_name }}'
RETURNING
comment
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: model_version_comments
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the model_version_comments resource.
    - name: name
      value: required
    - name: version
      value: string
    - name: comment
      value: required
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updatecomment"
    values={[
        { label: 'updatecomment', value: 'updatecomment' }
    ]}
>
<TabItem value="updatecomment">

Post an edit to a comment on a model version.

```sql
UPDATE databricks_workspace.machinelearning.model_version_comments
SET 
data__id = '{{ id }}',
data__comment = '{{ comment }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
comment;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletecomment"
    values={[
        { label: 'deletecomment', value: 'deletecomment' }
    ]}
>
<TabItem value="deletecomment">

Deletes a comment on a model version.

```sql
DELETE FROM databricks_workspace.machinelearning.model_version_comments
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
