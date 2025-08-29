--- 
title: output_catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - output_catalog
  - cleanrooms
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

Creates, updates, deletes, gets or lists an <code>output_catalog</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>output_catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.output_catalog" /></td></tr>
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
    <td><a href="#createoutputcatalog"><CopyableCode code="createoutputcatalog" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create the output catalog of the clean room.</td>
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
    defaultValue="createoutputcatalog"
    values={[
        { label: 'createoutputcatalog', value: 'createoutputcatalog' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createoutputcatalog">

Create the output catalog of the clean room.

```sql
INSERT INTO databricks_workspace.cleanrooms.output_catalog (
data__catalog_name,
deployment_name
)
SELECT 
'{{ catalog_name }}',
'{{ deployment_name }}'
RETURNING
output_catalog
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: output_catalog
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the output_catalog resource.
    - name: catalog_name
      value: string
```
</TabItem>
</Tabs>
