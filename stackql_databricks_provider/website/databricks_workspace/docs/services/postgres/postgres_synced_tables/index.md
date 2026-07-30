---
title: postgres_synced_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_synced_tables
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

Creates, updates, deletes, gets or lists a <code>postgres_synced_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_synced_tables" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_synced_tables" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-synced_table_id"><code>synced_table_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-synced_table"><code>synced_table</code></a></td>
    <td></td>
    <td>Create a Synced Table.</td>
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
<tr id="parameter-synced_table_id">
    <td><CopyableCode code="synced_table_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Synced Table. This becomes the final component of the SyncedTable's resource name. ID is required and is the synced table name, containing (catalog, schema, table) tuple. Elements of the tuple are the UC entity names. Example: "&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;" synced_table_id represents both of the following: 1. An online VIEW virtual table in the Unity Catalog accessible via the Lakehouse Federation. 2. Postgres table named "&#123;table&#125;" in schema "&#123;schema&#125;" in the connected Postgres database</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a Synced Table.

```sql
INSERT INTO databricks_workspace.postgres.postgres_synced_tables (
synced_table,
synced_table_id,
deployment_name
)
SELECT 
'{{ synced_table }}' /* required */,
'{{ synced_table_id }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_synced_tables
  props:
    - name: synced_table_id
      value: "{{ synced_table_id }}"
      description: Required parameter for the postgres_synced_tables resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_synced_tables resource.
    - name: synced_table
      value:
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        spec:
          accelerated_sync: {{ accelerated_sync }}
          branch: "{{ branch }}"
          create_database_objects_if_missing: {{ create_database_objects_if_missing }}
          existing_pipeline_id: "{{ existing_pipeline_id }}"
          extra_columns:
            - column_name: "{{ column_name }}"
              column_type: "{{ column_type }}"
              compute: "{{ compute }}"
              maintenance: "{{ maintenance }}"
          extra_index_definitions:
            - name: "{{ name }}"
              definition: "{{ definition }}"
              creation_point: "{{ creation_point }}"
          new_pipeline_spec:
            budget_policy_id: "{{ budget_policy_id }}"
            pipeline_channel: "{{ pipeline_channel }}"
            storage_catalog: "{{ storage_catalog }}"
            storage_schema: "{{ storage_schema }}"
          postgres_database: "{{ postgres_database }}"
          primary_key_columns:
            - "{{ primary_key_columns }}"
          scheduling_policy: "{{ scheduling_policy }}"
          source_table_full_name: "{{ source_table_full_name }}"
          timeseries_key: "{{ timeseries_key }}"
          type_overrides:
            - column_name: "{{ column_name }}"
              pg_type: "{{ pg_type }}"
              size: {{ size }}
        status:
          detailed_state: "{{ detailed_state }}"
          last_processed_commit_version: {{ last_processed_commit_version }}
          last_sync:
            delta_table_sync_info:
              delta_commit_time: "{{ delta_commit_time }}"
              delta_commit_version: {{ delta_commit_version }}
            sync_end_time: "{{ sync_end_time }}"
            sync_start_time: "{{ sync_start_time }}"
          last_sync_time: "{{ last_sync_time }}"
          message: "{{ message }}"
          ongoing_sync_progress:
            estimated_completion_time_seconds: {{ estimated_completion_time_seconds }}
            latest_version_currently_processing: {{ latest_version_currently_processing }}
            sync_progress_completion: {{ sync_progress_completion }}
            synced_row_count: {{ synced_row_count }}
            total_row_count: {{ total_row_count }}
          pipeline_id: "{{ pipeline_id }}"
          project: "{{ project }}"
          provisioning_phase: "{{ provisioning_phase }}"
          unity_catalog_provisioning_state: "{{ unity_catalog_provisioning_state }}"
        synced_table_id: "{{ synced_table_id }}"
        uid: "{{ uid }}"
`}</CodeBlock>

</TabItem>
</Tabs>
