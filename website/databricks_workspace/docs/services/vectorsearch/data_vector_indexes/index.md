--- 
title: data_vector_indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - data_vector_indexes
  - vectorsearch
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

Creates, updates, deletes, gets or lists a <code>data_vector_indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_vector_indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.data_vector_indexes" /></td></tr>
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
    <td><a href="#upsertdatavectorindex"><CopyableCode code="upsertdatavectorindex" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Handles the upserting of data into a specified vector index.</td>
</tr>
<tr>
    <td><a href="#deletedatavectorindex"><CopyableCode code="deletedatavectorindex" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Handles the deletion of data from a specified vector index.</td>
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
    defaultValue="upsertdatavectorindex"
    values={[
        { label: 'upsertdatavectorindex', value: 'upsertdatavectorindex' }
    ]}
>
<TabItem value="upsertdatavectorindex">

Handles the upserting of data into a specified vector index.

```sql
REPLACE databricks_workspace.vectorsearch.data_vector_indexes
SET 
data__inputs_json = '{{ inputs_json }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
result,
status;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletedatavectorindex"
    values={[
        { label: 'deletedatavectorindex', value: 'deletedatavectorindex' }
    ]}
>
<TabItem value="deletedatavectorindex">

Handles the deletion of data from a specified vector index.

```sql
DELETE FROM databricks_workspace.vectorsearch.data_vector_indexes
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
