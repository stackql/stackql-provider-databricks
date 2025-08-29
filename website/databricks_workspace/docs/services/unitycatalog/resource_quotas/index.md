--- 
title: resource_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_quotas
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

Creates, updates, deletes, gets or lists a <code>resource_quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.resource_quotas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="listquotas"
    values={[
        { label: 'listquotas', value: 'listquotas' },
        { label: 'getquota', value: 'getquota' }
    ]}
>
<TabItem value="listquotas">

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
    <td><CopyableCode code="parent_full_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="quota_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_refreshed_at" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="parent_securable_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="quota_count" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="quota_limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="getquota">

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
    <td><CopyableCode code="parent_full_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="quota_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_refreshed_at" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="parent_securable_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="quota_count" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="quota_limit" /></td>
    <td><code>integer</code></td>
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
    <td><a href="#listquotas"><CopyableCode code="listquotas" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>ListQuotas returns all quota values under the metastore. There are no SLAs on the freshness of the counts returned. This API does not trigger a refresh of quota counts.</td>
</tr>
<tr>
    <td><a href="#getquota"><CopyableCode code="getquota" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>The GetQuota API returns usage information for a single resource quota, defined as a child-parent pair. This API also refreshes the quota count if it is out of date. Refreshes are triggered asynchronously. The updated count might not be returned in the first call.</td>
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
    defaultValue="listquotas"
    values={[
        { label: 'listquotas', value: 'listquotas' },
        { label: 'getquota', value: 'getquota' }
    ]}
>
<TabItem value="listquotas">

ListQuotas returns all quota values under the metastore. There are no SLAs on the freshness of the counts returned. This API does not trigger a refresh of quota counts.

```sql
SELECT
parent_full_name,
quota_name,
last_refreshed_at,
parent_securable_type,
quota_count,
quota_limit
FROM databricks_workspace.unitycatalog.resource_quotas
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
<TabItem value="getquota">

The GetQuota API returns usage information for a single resource quota, defined as a child-parent pair. This API also refreshes the quota count if it is out of date. Refreshes are triggered asynchronously. The updated count might not be returned in the first call.

```sql
SELECT
parent_full_name,
quota_name,
last_refreshed_at,
parent_securable_type,
quota_count,
quota_limit
FROM databricks_workspace.unitycatalog.resource_quotas
WHERE deployment_name = '{{ deployment_name }}' -- required;
```
</TabItem>
</Tabs>
