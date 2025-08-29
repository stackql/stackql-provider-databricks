--- 
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - lakeview
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

Creates, updates, deletes, gets or lists a <code>dashboards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.lakeview.dashboards" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Request completed successfully.

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
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle_state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="parent_path" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="serialized_dashboard" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Request completed successfully.

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
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle_state" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a draft dashboard.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create a draft dashboard.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Update a draft dashboard.</td>
</tr>
<tr>
    <td><a href="#trash"><CopyableCode code="trash" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Trash a dashboard.</td>
</tr>
<tr>
    <td><a href="#migrate"><CopyableCode code="migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Migrates a classic SQL dashboard to Lakeview.</td>
</tr>
<tr>
    <td><a href="#publish"><CopyableCode code="publish" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Publish the current draft dashboard.</td>
</tr>
<tr>
    <td><a href="#unpublish"><CopyableCode code="unpublish" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Unpublish the dashboard.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a draft dashboard.

```sql
SELECT
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time
FROM databricks_workspace.lakeview.dashboards
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="list">

Request completed successfully.

```sql
SELECT
dashboard_id,
warehouse_id,
display_name,
create_time,
lifecycle_state
FROM databricks_workspace.lakeview.dashboards
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a draft dashboard.

```sql
INSERT INTO databricks_workspace.lakeview.dashboards (
data__display_name,
data__warehouse_id,
data__etag,
data__serialized_dashboard,
data__parent_path,
deployment_name
)
SELECT 
'{{ display_name }}',
'{{ warehouse_id }}',
'{{ etag }}',
'{{ serialized_dashboard }}',
'{{ parent_path }}',
'{{ deployment_name }}'
RETURNING
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dashboards
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the dashboards resource.
    - name: display_name
      value: string
    - name: warehouse_id
      value: string
    - name: etag
      value: string
    - name: serialized_dashboard
      value: string
    - name: parent_path
      value: string
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a draft dashboard.

```sql
UPDATE databricks_workspace.lakeview.dashboards
SET 
data__display_name = '{{ display_name }}',
data__warehouse_id = '{{ warehouse_id }}',
data__etag = '{{ etag }}',
data__serialized_dashboard = '{{ serialized_dashboard }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
dashboard_id,
warehouse_id,
display_name,
create_time,
etag,
lifecycle_state,
parent_path,
path,
serialized_dashboard,
update_time;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="trash"
    values={[
        { label: 'trash', value: 'trash' }
    ]}
>
<TabItem value="trash">

Trash a dashboard.

```sql
DELETE FROM databricks_workspace.lakeview.dashboards
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="migrate"
    values={[
        { label: 'migrate', value: 'migrate' },
        { label: 'publish', value: 'publish' },
        { label: 'unpublish', value: 'unpublish' }
    ]}
>
<TabItem value="migrate">

Migrates a classic SQL dashboard to Lakeview.

```sql
EXEC databricks_workspace.lakeview.dashboards.migrate 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"source_dashboard_id": "{{ source_dashboard_id }}", 
"display_name": "{{ display_name }}", 
"parent_path": "{{ parent_path }}", 
"update_parameter_syntax": "{{ update_parameter_syntax }}"
}';
```
</TabItem>
<TabItem value="publish">

Publish the current draft dashboard.

```sql
EXEC databricks_workspace.lakeview.dashboards.publish 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"embed_credentials": {{ embed_credentials }}, 
"warehouse_id": "{{ warehouse_id }}"
}';
```
</TabItem>
<TabItem value="unpublish">

Unpublish the dashboard.

```sql
EXEC databricks_workspace.lakeview.dashboards.unpublish 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
