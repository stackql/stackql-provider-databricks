--- 
title: quality_monitor_refreshes
hide_title: false
hide_table_of_contents: false
keywords:
  - quality_monitor_refreshes
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

Creates, updates, deletes, gets or lists a <code>quality_monitor_refreshes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quality_monitor_refreshes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.quality_monitor_refreshes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listrefreshes"
    values={[
        { label: 'listrefreshes', value: 'listrefreshes' },
        { label: 'getrefresh', value: 'getrefresh' }
    ]}
>
<TabItem value="listrefreshes">

The list of refresh info was successfully retrieved.

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
    <td><CopyableCode code="refresh_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="end_time_ms" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="start_time_ms" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getrefresh">

The refresh info was successfully retrieved.

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
    <td><CopyableCode code="refresh_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="end_time_ms" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="start_time_ms" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
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
    <td><a href="#listrefreshes"><CopyableCode code="listrefreshes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets an array containing the history of the most recent refreshes (up to 25) for this table.</td>
</tr>
<tr>
    <td><a href="#getrefresh"><CopyableCode code="getrefresh" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets info about a specific monitor refresh using the given refresh ID.</td>
</tr>
<tr>
    <td><a href="#runrefresh"><CopyableCode code="runrefresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Queues a metric refresh on the monitor for the specified table. The refresh will execute in the background.</td>
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
    defaultValue="listrefreshes"
    values={[
        { label: 'listrefreshes', value: 'listrefreshes' },
        { label: 'getrefresh', value: 'getrefresh' }
    ]}
>
<TabItem value="listrefreshes">

Gets an array containing the history of the most recent refreshes (up to 25) for this table.

```sql
SELECT
refresh_id,
end_time_ms,
message,
start_time_ms,
state,
trigger
FROM databricks_workspace.unitycatalog.quality_monitor_refreshes
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getrefresh">

Gets info about a specific monitor refresh using the given refresh ID.

```sql
SELECT
refresh_id,
end_time_ms,
message,
start_time_ms,
state,
trigger
FROM databricks_workspace.unitycatalog.quality_monitor_refreshes
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="runrefresh"
    values={[
        { label: 'runrefresh', value: 'runrefresh' }
    ]}
>
<TabItem value="runrefresh">

Queues a metric refresh on the monitor for the specified table. The refresh will execute in the background.

```sql
EXEC databricks_workspace.unitycatalog.quality_monitor_refreshes.runrefresh 
@deployment_name='{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
