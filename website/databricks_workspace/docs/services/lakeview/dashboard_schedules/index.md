--- 
title: dashboard_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_schedules
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

Creates, updates, deletes, gets or lists a <code>dashboard_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.lakeview.dashboard_schedules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="getschedule"
    values={[
        { label: 'getschedule', value: 'getschedule' },
        { label: 'listschedules', value: 'listschedules' }
    ]}
>
<TabItem value="getschedule">

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
    <td><CopyableCode code="schedule_id" /></td>
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
    <td><CopyableCode code="cron_schedule" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pause_status" /></td>
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
<TabItem value="listschedules">

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
    <td><CopyableCode code="schedule_id" /></td>
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
    <td><CopyableCode code="cron_schedule" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pause_status" /></td>
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
    <td><a href="#getschedule"><CopyableCode code="getschedule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#listschedules"><CopyableCode code="listschedules" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#createschedule"><CopyableCode code="createschedule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#updateschedule"><CopyableCode code="updateschedule" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#deleteschedule"><CopyableCode code="deleteschedule" /></a></td>
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
    defaultValue="getschedule"
    values={[
        { label: 'getschedule', value: 'getschedule' },
        { label: 'listschedules', value: 'listschedules' }
    ]}
>
<TabItem value="getschedule">

Request completed successfully.

```sql
SELECT
dashboard_id,
schedule_id,
warehouse_id,
display_name,
create_time,
cron_schedule,
etag,
pause_status,
update_time
FROM databricks_workspace.lakeview.dashboard_schedules
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="listschedules">

Request completed successfully.

```sql
SELECT
dashboard_id,
schedule_id,
warehouse_id,
display_name,
create_time,
cron_schedule,
etag,
pause_status,
update_time
FROM databricks_workspace.lakeview.dashboard_schedules
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="createschedule"
    values={[
        { label: 'createschedule', value: 'createschedule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="createschedule">

No description available.

```sql
INSERT INTO databricks_workspace.lakeview.dashboard_schedules (
data__pause_status,
data__display_name,
data__etag,
data__warehouse_id,
data__cron_schedule,
deployment_name
)
SELECT 
'{{ pause_status }}',
'{{ display_name }}',
'{{ etag }}',
'{{ warehouse_id }}',
'{{ cron_schedule }}',
'{{ deployment_name }}'
RETURNING
dashboard_id,
schedule_id,
warehouse_id,
display_name,
create_time,
cron_schedule,
etag,
pause_status,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: dashboard_schedules
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the dashboard_schedules resource.
    - name: pause_status
      value: string
    - name: display_name
      value: string
    - name: etag
      value: string
    - name: warehouse_id
      value: string
    - name: cron_schedule
      value: object
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="updateschedule"
    values={[
        { label: 'updateschedule', value: 'updateschedule' }
    ]}
>
<TabItem value="updateschedule">

No description available.

```sql
UPDATE databricks_workspace.lakeview.dashboard_schedules
SET 
data__pause_status = '{{ pause_status }}',
data__display_name = '{{ display_name }}',
data__etag = '{{ etag }}',
data__warehouse_id = '{{ warehouse_id }}',
data__cron_schedule = '{{ cron_schedule }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
dashboard_id,
schedule_id,
warehouse_id,
display_name,
create_time,
cron_schedule,
etag,
pause_status,
update_time;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="deleteschedule"
    values={[
        { label: 'deleteschedule', value: 'deleteschedule' }
    ]}
>
<TabItem value="deleteschedule">

No description available.

```sql
DELETE FROM databricks_workspace.lakeview.dashboard_schedules
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
