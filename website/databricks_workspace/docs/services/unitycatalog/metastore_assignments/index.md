--- 
title: metastore_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - metastore_assignments
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

Creates, updates, deletes, gets or lists a <code>metastore_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastore_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.metastore_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="current"
    values={[
        { label: 'current', value: 'current' }
    ]}
>
<TabItem value="current">

The metastore assignment was successfully retrieved.

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
    <td><CopyableCode code="metastore_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="default_catalog_name" /></td>
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
    <td><a href="#current"><CopyableCode code="current" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the metastore assignment for the workspace being accessed.</td>
</tr>
<tr>
    <td><a href="#assign"><CopyableCode code="assign" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new metastore assignment. If an assignment for the same</td>
</tr>
<tr>
    <td><a href="#updateassignment"><CopyableCode code="updateassignment" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a metastore assignment. This operation can be used to update</td>
</tr>
<tr>
    <td><a href="#unassign"><CopyableCode code="unassign" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a metastore assignment. The caller must be an account administrator.</td>
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
    defaultValue="current"
    values={[
        { label: 'current', value: 'current' }
    ]}
>
<TabItem value="current">

Gets the metastore assignment for the workspace being accessed.

```sql
SELECT
metastore_id,
workspace_id,
default_catalog_name
FROM databricks_workspace.unitycatalog.metastore_assignments
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="assign"
    values={[
        { label: 'assign', value: 'assign' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="assign">

Creates a new metastore assignment. If an assignment for the same

```sql
INSERT INTO databricks_workspace.unitycatalog.metastore_assignments (
data__metastore_id,
data__default_catalog_name,
deployment_name
)
SELECT 
'{{ metastore_id }}',
'{{ default_catalog_name }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: metastore_assignments
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the metastore_assignments resource.
    - name: metastore_id
      value: required
    - name: default_catalog_name
      value: string
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updateassignment"
    values={[
        { label: 'updateassignment', value: 'updateassignment' }
    ]}
>
<TabItem value="updateassignment">

Updates a metastore assignment. This operation can be used to update

```sql
UPDATE databricks_workspace.unitycatalog.metastore_assignments
SET 
data__metastore_id = '{{ metastore_id }}',
data__default_catalog_name = '{{ default_catalog_name }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="unassign"
    values={[
        { label: 'unassign', value: 'unassign' }
    ]}
>
<TabItem value="unassign">

Deletes a metastore assignment. The caller must be an account administrator.

```sql
DELETE FROM databricks_workspace.unitycatalog.metastore_assignments
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
