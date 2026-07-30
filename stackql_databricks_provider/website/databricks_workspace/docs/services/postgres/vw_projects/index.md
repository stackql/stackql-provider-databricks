---
title: vw_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_projects
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

Creates, updates, deletes, gets or lists a <code>vw_projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_projects" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.vw_projects" /></td></tr>
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
    <td>The project identifier (last component of the resource path).</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the project was created.</td>
</tr>
<tr>
    <td><CopyableCode code="initial_endpoint_spec" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Initial endpoint configuration for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><CopyableCode code="object" /></td>
    <td>Project specification including display_name, pg_version, and default endpoint settings.</td>
</tr>
<tr>
    <td><CopyableCode code="compute_last_active_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp of the last compute activity on the project.</td>
</tr>
<tr>
    <td><CopyableCode code="min_cu" /></td>
    <td><CopyableCode code="number" /></td>
    <td>Minimum autoscaling Compute Units for the default endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="max_cu" /></td>
    <td><CopyableCode code="number" /></td>
    <td>Maximum autoscaling Compute Units for the default endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="suspend_timeout_duration" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Duration of inactivity after which the default endpoint is automatically suspended.</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Human-readable project name.</td>
</tr>
<tr>
    <td><CopyableCode code="enable_pg_native_login" /></td>
    <td><CopyableCode code="boolean" /></td>
    <td>Whether PG native password login is enabled on all endpoints in this project.</td>
</tr>
<tr>
    <td><CopyableCode code="history_retention_duration" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Duration for retaining point-in-time recovery history across all branches.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Email of the project owner.</td>
</tr>
<tr>
    <td><CopyableCode code="pg_version" /></td>
    <td><CopyableCode code="integer" /></td>
    <td>Major Postgres version number in use.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><CopyableCode code="string" /></td>
    <td>System-generated unique ID for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Timestamp when the project was last updated.</td>
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
  initial_endpoint_spec,
  spec,
  compute_last_active_time,
  min_cu,
  max_cu,
  suspend_timeout_duration,
  display_name,
  enable_pg_native_login,
  history_retention_duration,
  owner,
  pg_version,
  uid,
  update_time
FROM databricks_workspace.postgres.vw_projects
WHERE deployment_name = '{{ deployment_name }}';
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
  initial_endpoint_spec,
  spec,
  JSON_EXTRACT(status, '$.compute_last_active_time') AS compute_last_active_time,
  JSON_EXTRACT(status, '$.default_endpoint_settings.autoscaling_limit_min_cu') AS min_cu,
  JSON_EXTRACT(status, '$.default_endpoint_settings.autoscaling_limit_max_cu') AS max_cu,
  JSON_EXTRACT(status, '$.default_endpoint_settings.suspend_timeout_duration') AS suspend_timeout_duration,
  JSON_EXTRACT(status, '$.display_name') AS display_name,
  JSON_EXTRACT(status, '$.enable_pg_native_login') AS enable_pg_native_login,
  JSON_EXTRACT(status, '$.history_retention_duration') AS history_retention_duration,
  JSON_EXTRACT(status, '$.owner') AS owner,
  JSON_EXTRACT(status, '$.pg_version') AS pg_version,
  uid,
  update_time
FROM databricks_workspace.postgres.postgres_projects
WHERE deployment_name = '{{ deployment_name }}'
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  SPLIT_PART(name, '/', -1) AS name,
  create_time,
  initial_endpoint_spec,
  spec,
  (status::jsonb)->>'compute_last_active_time' AS compute_last_active_time,
  (status::jsonb)#>>'{default_endpoint_settings,autoscaling_limit_min_cu}' AS min_cu,
  (status::jsonb)#>>'{default_endpoint_settings,autoscaling_limit_max_cu}' AS max_cu,
  (status::jsonb)#>>'{default_endpoint_settings,suspend_timeout_duration}' AS suspend_timeout_duration,
  (status::jsonb)->>'display_name' AS display_name,
  (status::jsonb)->>'enable_pg_native_login' AS enable_pg_native_login,
  (status::jsonb)->>'history_retention_duration' AS history_retention_duration,
  (status::jsonb)->>'owner' AS owner,
  (status::jsonb)->>'pg_version' AS pg_version,
  uid,
  update_time
FROM databricks_workspace.postgres.postgres_projects
WHERE deployment_name = '{{ deployment_name }}'
```

</TabItem>
</Tabs>
