---
title: database
hide_title: false
hide_table_of_contents: false
keywords:
  - database
  - database
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

Creates, updates, deletes, gets or lists a <code>database</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.database.database" /></td></tr>
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
    <td><a href="#database_failover_database_instance"><CopyableCode code="database_failover_database_instance" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Failover the primary node of a Database Instance to a secondary.</td>
</tr>
<tr>
    <td><a href="#database_update_database_instance_role"><CopyableCode code="database_update_database_instance_role" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-database_instance_role"><code>database_instance_role</code></a></td>
    <td><a href="#parameter-database_instance_name"><code>database_instance_name</code></a></td>
    <td>Update a role for a Database Instance.</td>
</tr>
<tr>
    <td><a href="#database_upgrade_instance_to_autoscaling"><CopyableCode code="database_upgrade_instance_to_autoscaling" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Upgrade a Database Instance to Autoscaling.</td>
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
<tr id="parameter-instance_name">
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the instance to upgrade.</td>
</tr>
<tr id="parameter-database_instance_name">
    <td><CopyableCode code="database_instance_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="database_failover_database_instance"
    values={[
        { label: 'database_failover_database_instance', value: 'database_failover_database_instance' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="database_failover_database_instance">

Failover the primary node of a Database Instance to a secondary.

```sql
INSERT INTO databricks_workspace.database.database (
failover_target_database_instance_name,
name,
deployment_name
)
SELECT 
'{{ failover_target_database_instance_name }}',
'{{ name }}',
'{{ deployment_name }}'
RETURNING
name,
effective_usage_policy_id,
usage_policy_id,
capacity,
child_instance_refs,
creation_time,
creator,
custom_tags,
effective_capacity,
effective_custom_tags,
effective_enable_pg_native_login,
effective_enable_readable_secondaries,
effective_node_count,
effective_retention_window_in_days,
effective_stopped,
enable_pg_native_login,
enable_readable_secondaries,
node_count,
parent_instance_ref,
pg_version,
read_only_dns,
read_write_dns,
retention_window_in_days,
state,
stopped,
uid
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: database
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the database resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the database resource.
    - name: failover_target_database_instance_name
      value: "{{ failover_target_database_instance_name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="database_update_database_instance_role"
    values={[
        { label: 'database_update_database_instance_role', value: 'database_update_database_instance_role' },
        { label: 'database_upgrade_instance_to_autoscaling', value: 'database_upgrade_instance_to_autoscaling' }
    ]}
>
<TabItem value="database_update_database_instance_role">

Update a role for a Database Instance.

```sql
UPDATE databricks_workspace.database.database
SET 
database_instance_role = '{{ database_instance_role }}'
WHERE 
instance_name = '{{ instance_name }}' --required
AND name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND database_instance_role = '{{ database_instance_role }}' --required
AND database_instance_name = '{{ database_instance_name}}'
RETURNING
name,
instance_name,
attributes,
effective_attributes,
identity_type,
membership_role;
```
</TabItem>
<TabItem value="database_upgrade_instance_to_autoscaling">

Upgrade a Database Instance to Autoscaling.

```sql
UPDATE databricks_workspace.database.database
SET 
-- No updatable properties
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required;
```
</TabItem>
</Tabs>
