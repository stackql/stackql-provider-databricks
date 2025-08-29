--- 
title: ai_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateways
  - realtimeserving
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

Creates, updates, deletes, gets or lists an <code>ai_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ai_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.realtimeserving.ai_gateways" /></td></tr>
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
    <td><a href="#putaigateway"><CopyableCode code="putaigateway" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Used to update the AI Gateway of a serving endpoint. NOTE: Only external model endpoints are currently supported.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="putaigateway"
    values={[
        { label: 'putaigateway', value: 'putaigateway' }
    ]}
>
<TabItem value="putaigateway">

Used to update the AI Gateway of a serving endpoint. NOTE: Only external model endpoints are currently supported.

```sql
EXEC databricks_workspace.realtimeserving.ai_gateways.putaigateway 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"usage_tracking_config": "{{ usage_tracking_config }}", 
"inference_table_config": "{{ inference_table_config }}", 
"rate_limits": "{{ rate_limits }}", 
"guardrails": "{{ guardrails }}"
}';
```
</TabItem>
</Tabs>
