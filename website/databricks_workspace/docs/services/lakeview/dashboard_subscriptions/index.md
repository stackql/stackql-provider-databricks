--- 
title: dashboard_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_subscriptions
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

Creates, updates, deletes, gets or lists a <code>dashboard_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.lakeview.dashboard_subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getsubscription"
    values={[
        { label: 'getsubscription', value: 'getsubscription' },
        { label: 'listsubscriptions', value: 'listsubscriptions' }
    ]}
>
<TabItem value="getsubscription">

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
    <td><CopyableCode code="created_by_user_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schedule_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="subscription_id" /></td>
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
    <td><CopyableCode code="subscriber" /></td>
    <td><code>object</code></td>
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
<TabItem value="listsubscriptions">

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
    <td><CopyableCode code="created_by_user_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dashboard_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schedule_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="subscription_id" /></td>
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
    <td><CopyableCode code="subscriber" /></td>
    <td><code>object</code></td>
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
    <td><a href="#getsubscription"><CopyableCode code="getsubscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#listsubscriptions"><CopyableCode code="listsubscriptions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#createsubscription"><CopyableCode code="createsubscription" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#deletesubscription"><CopyableCode code="deletesubscription" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
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
    defaultValue="getsubscription"
    values={[
        { label: 'getsubscription', value: 'getsubscription' },
        { label: 'listsubscriptions', value: 'listsubscriptions' }
    ]}
>
<TabItem value="getsubscription">

Request completed successfully.

```sql
SELECT
created_by_user_id,
dashboard_id,
schedule_id,
subscription_id,
create_time,
etag,
subscriber,
update_time
FROM databricks_workspace.lakeview.dashboard_subscriptions
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listsubscriptions">

Request completed successfully.

```sql
SELECT
created_by_user_id,
dashboard_id,
schedule_id,
subscription_id,
create_time,
etag,
subscriber,
update_time
FROM databricks_workspace.lakeview.dashboard_subscriptions
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createsubscription"
    values={[
        { label: 'createsubscription', value: 'createsubscription' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createsubscription">

No description available.

```sql
INSERT INTO databricks_workspace.lakeview.dashboard_subscriptions (
data__etag,
data__subscriber,
deployment_name
)
SELECT 
'{{ etag }}',
'{{ subscriber }}',
'{{ deployment_name }}'
RETURNING
created_by_user_id,
dashboard_id,
schedule_id,
subscription_id,
create_time,
etag,
subscriber,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dashboard_subscriptions
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the dashboard_subscriptions resource.
    - name: etag
      value: string
    - name: subscriber
      value: required
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deletesubscription"
    values={[
        { label: 'deletesubscription', value: 'deletesubscription' }
    ]}
>
<TabItem value="deletesubscription">

No description available.

```sql
DELETE FROM databricks_workspace.lakeview.dashboard_subscriptions
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
