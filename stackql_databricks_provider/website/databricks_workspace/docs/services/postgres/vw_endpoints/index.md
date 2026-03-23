---
title: vw_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_endpoints
  - postgres
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>vw_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.vw_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

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
    <td><CopyableCode code="name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The endpoint identifier (last component of the resource path).</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the endpoint was created.</td>
</tr>
<tr>
    <td><CopyableCode code="project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The project identifier that owns this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="branch_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The branch identifier that owns this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Endpoint specification including type, autoscaling limits, and suspension settings.</td>
</tr>
<tr>
    <td><CopyableCode code="max_cu" /></td>
    <td><CopyableCode code="number" /></td>
    <td>Maximum autoscaling Compute Units for the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="min_cu" /></td>
    <td><CopyableCode code="number" /></td>
    <td>Minimum autoscaling Compute Units for the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="current_state" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Current operational state of the endpoint (e.g. ACTIVE, IDLE, INIT).</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether connections to the endpoint are restricted.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint_type" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The compute endpoint type (ENDPOINT_TYPE_READ_WRITE or ENDPOINT_TYPE_READ_ONLY).</td>
</tr>
<tr>
    <td><CopyableCode code="last_active_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp of the last activity on the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Postgres settings for the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="group_enable_readable_secondaries" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether read-only connections to the read-write endpoint are allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="group_max" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Maximum number of computes in the endpoint group.</td>
</tr>
<tr>
    <td><CopyableCode code="group_min" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Minimum number of computes in the endpoint group.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Hostname for connecting to this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="read_write_pooled_host" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Pooled read-write hostname for the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><CopyableCode code="string" /></td>
    <td>System-generated unique ID for the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the endpoint was last updated.</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

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
    <td><CopyableCode code="project_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The project identifier to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="branch_id" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The branch identifier to scope the query.</td>
</tr>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The Databricks workspace deployment name.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  name,
  create_time,
  project_id,
  branch_id,
  spec,
  max_cu,
  min_cu,
  current_state,
  disabled,
  endpoint_type,
  last_active_time,
  settings,
  group_enable_readable_secondaries,
  group_max,
  group_min,
  host,
  read_write_pooled_host,
  uid,
  update_time
FROM databricks_workspace.postgres.vw_endpoints
WHERE project_id = '{{ project_id }}'
  AND branch_id = '{{ branch_id }}'
  AND deployment_name = '{{ deployment_name }}';
```

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  SPLIT_PART(name, '/', -1) AS name,
  create_time,
  project_id,
  branch_id,
  spec,
  JSON_EXTRACT(status, '$.autoscaling_limit_max_cu') AS max_cu,
  JSON_EXTRACT(status, '$.autoscaling_limit_min_cu') AS min_cu,
  JSON_EXTRACT(status, '$.current_state') AS current_state,
  JSON_EXTRACT(status, '$.disabled') AS disabled,
  JSON_EXTRACT(status, '$.endpoint_type') AS endpoint_type,
  JSON_EXTRACT(status, '$.last_active_time') AS last_active_time,
  JSON_EXTRACT(status, '$.settings') AS settings,
  JSON_EXTRACT(status, '$.group.enable_readable_secondaries') AS group_enable_readable_secondaries,
  JSON_EXTRACT(status, '$.group.max') AS group_max,
  JSON_EXTRACT(status, '$.group.min') AS group_min,
  JSON_EXTRACT(status, '$.hosts.host') AS host,
  JSON_EXTRACT(status, '$.hosts.read_write_pooled_host') AS read_write_pooled_host,
  uid,
  update_time
FROM databricks_workspace.postgres.endpoints
WHERE project_id = '{{ project_id }}'
AND branch_id = '{{ branch_id }}'
AND deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  SPLIT_PART(name, '/', -1) AS name,
  create_time,
  project_id,
  branch_id,
  spec,
  (status::jsonb)->>'autoscaling_limit_max_cu' AS max_cu,
  (status::jsonb)->>'autoscaling_limit_min_cu' AS min_cu,
  (status::jsonb)->>'current_state' AS current_state,
  (status::jsonb)->>'disabled' AS disabled,
  (status::jsonb)->>'endpoint_type' AS endpoint_type,
  (status::jsonb)->>'last_active_time' AS last_active_time,
  (status::jsonb)->>'settings' AS settings,
  (status::jsonb)#>>'{group,enable_readable_secondaries}' AS group_enable_readable_secondaries,
  (status::jsonb)#>>'{group,max}' AS group_max,
  (status::jsonb)#>>'{group,min}' AS group_min,
  (status::jsonb)#>>'{hosts,host}' AS host,
  (status::jsonb)#>>'{hosts,read_write_pooled_host}' AS read_write_pooled_host,
  uid,
  update_time
FROM databricks_workspace.postgres.endpoints
WHERE project_id = '{{ project_id }}'
AND branch_id = '{{ branch_id }}'
AND deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>
