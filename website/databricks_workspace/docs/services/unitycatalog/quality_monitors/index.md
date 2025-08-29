--- 
title: quality_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - quality_monitors
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

Creates, updates, deletes, gets or lists a <code>quality_monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quality_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.quality_monitors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

The monitor was successfully retrieved.

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
    <td><CopyableCode code="baseline_table_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="drift_metrics_table_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="output_schema_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="profile_metrics_table_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="assets_dir" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_metrics" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="inference_log" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="latest_monitor_failure_msg" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="monitor_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="slicing_exprs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="snapshot" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="time_series" /></td>
    <td><code>object</code></td>
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
    <td>Gets a monitor for the specified table.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Creates a new monitor for the specified table.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Updates a monitor for the specified table.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a monitor for the specified table.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a monitor for the specified table.

```sql
SELECT
dashboard_id,
baseline_table_name,
drift_metrics_table_name,
output_schema_name,
profile_metrics_table_name,
table_name,
assets_dir,
custom_metrics,
inference_log,
latest_monitor_failure_msg,
monitor_version,
notifications,
schedule,
slicing_exprs,
snapshot,
status,
time_series
FROM databricks_workspace.unitycatalog.quality_monitors
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

Creates a new monitor for the specified table.

```sql
INSERT INTO databricks_workspace.unitycatalog.quality_monitors (
data__skip_builtin_dashboard,
data__warehouse_id,
data__assets_dir,
data__output_schema_name,
data__snapshot,
data__slicing_exprs,
data__baseline_table_name,
data__inference_log,
data__time_series,
data__custom_metrics,
data__schedule,
data__notifications,
deployment_name
)
SELECT 
{{ skip_builtin_dashboard }},
'{{ warehouse_id }}',
'{{ assets_dir }}',
'{{ output_schema_name }}',
'{{ snapshot }}',
'{{ slicing_exprs }}',
'{{ baseline_table_name }}',
'{{ inference_log }}',
'{{ time_series }}',
'{{ custom_metrics }}',
'{{ schedule }}',
'{{ notifications }}',
'{{ deployment_name }}'
RETURNING
dashboard_id,
baseline_table_name,
drift_metrics_table_name,
output_schema_name,
profile_metrics_table_name,
table_name,
assets_dir,
custom_metrics,
inference_log,
latest_monitor_failure_msg,
monitor_version,
notifications,
schedule,
slicing_exprs,
snapshot,
status,
time_series
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: quality_monitors
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the quality_monitors resource.
    - name: skip_builtin_dashboard
      value: boolean
    - name: warehouse_id
      value: string
    - name: assets_dir
      value: required
    - name: output_schema_name
      value: string
    - name: snapshot
      value: required
    - name: slicing_exprs
      value: string
    - name: baseline_table_name
      value: object
    - name: inference_log
      value: object
    - name: time_series
      value: object
    - name: custom_metrics
      value: Array of object
    - name: schedule
      value: object
    - name: notifications
      value: object
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

Updates a monitor for the specified table.

```sql
UPDATE databricks_workspace.unitycatalog.quality_monitors
SET 
data__output_schema_name = '{{ output_schema_name }}',
data__snapshot = '{{ snapshot }}',
data__slicing_exprs = '{{ slicing_exprs }}',
data__baseline_table_name = '{{ baseline_table_name }}',
data__dashboard_id = '{{ dashboard_id }}',
data__inference_log = '{{ inference_log }}',
data__time_series = '{{ time_series }}',
data__custom_metrics = '{{ custom_metrics }}',
data__schedule = '{{ schedule }}',
data__notifications = '{{ notifications }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
RETURNING
dashboard_id,
baseline_table_name,
drift_metrics_table_name,
output_schema_name,
profile_metrics_table_name,
table_name,
assets_dir,
custom_metrics,
inference_log,
latest_monitor_failure_msg,
monitor_version,
notifications,
schedule,
slicing_exprs,
snapshot,
status,
time_series;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a monitor for the specified table.

```sql
DELETE FROM databricks_workspace.unitycatalog.quality_monitors
WHERE deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
