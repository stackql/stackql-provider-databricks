---
title: postgres_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_roles
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

Creates, updates, deletes, gets or lists a <code>postgres_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_roles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_roles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the role. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;"
  },
  {
    "name": "role_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The Branch where this Role exists. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the role configuration, including identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "attributes",
        "type": "object",
        "description": "Attributes that can be granted to a Postgres role. We are only implementing a subset for now,<br />    see xref: https://www.postgresql.org/docs/16/sql-createrole.html The values follow Postgres<br />    keyword naming e.g. CREATEDB, BYPASSRLS, etc. which is why they don't include typical<br />    underscores between words.",
        "children": [
          {
            "name": "bypassrls",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createdb",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createrole",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "auth_method",
        "type": "string",
        "description": "Controls how the Postgres role authenticates when a client opens a database connection. Supported values: - LAKEBASE_OAUTH_V1: the role authenticates by presenting a Databricks OAuth access token derived from the backing managed identity (the Databricks user, service principal, or group named by the role's ``postgres_role``). No static password exists for roles using this method. - PG_PASSWORD_SCRAM_SHA_256: the role authenticates with a Postgres password verified server-side using the SCRAM-SHA-256 mechanism. Lakebase generates a password for the role. - NO_LOGIN: the role cannot open a Postgres session at all. Useful for roles that exist only to own objects or to aggregate privileges that are then granted to other, loginable roles. If auth_method is left unspecified, a meaningful authentication method is derived from the identity_type: - For the managed identities, OAUTH is used. - For the regular postgres roles, authentication based on postgres passwords is used. NOTE: for the Databricks identity type GROUP, LAKEBASE_OAUTH_V1 is the default auth method (group can login as well). (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of role. When specifying a managed-identity, the chosen role_id must be a valid: - application ID for SERVICE_PRINCIPAL - user email for USER - group name for GROUP (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "membership_roles",
        "type": "array",
        "description": "An enum value for a standard role that this role is a member of."
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS Required when creating the Role. If you wish to create a Postgres Role backed by a managed Databricks identity, then postgres_role must be one of the following: 1. user email for IdentityType.USER 2. app ID for IdentityType.SERVICE_PRINCIPAL 3. group name for IdentityType.GROUP"
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current status of the role, including its identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "attributes",
        "type": "object",
        "description": "Attributes that can be granted to a Postgres role. We are only implementing a subset for now,<br />    see xref: https://www.postgresql.org/docs/16/sql-createrole.html The values follow Postgres<br />    keyword naming e.g. CREATEDB, BYPASSRLS, etc. which is why they don't include typical<br />    underscores between words.",
        "children": [
          {
            "name": "bypassrls",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createdb",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createrole",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "auth_method",
        "type": "string",
        "description": "How the role is authenticated when connecting to Postgres. (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of the role. (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "membership_roles",
        "type": "array",
        "description": "An enum value for a standard role that this role is a member of."
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role."
      },
      {
        "name": "role_id",
        "type": "string",
        "description": "Part of the resource name."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The Full resource name of the synced table in Postgres where (catalog, schema, table) are the UC entity names. Format \"synced_tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;\" For the corresponding source table in the Unity catalog look for the \"source_table_full_name\" attribute."
  },
  {
    "name": "synced_table_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "spec",
    "type": "object",
    "description": "Configuration details of the synced table, such as the source table, scheduling policy, etc. This attribute is specified at creation time and most fields are returned as is on subsequent queries.",
    "children": [
      {
        "name": "accelerated_sync",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "branch",
        "type": "string",
        "description": "The full resource name the branch associated with the table. Format: \"projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;\"."
      },
      {
        "name": "create_database_objects_if_missing",
        "type": "boolean",
        "description": "If true, the synced table's logical database and schema resources in PG will be created if they do not already exist. The request will fail if this is false and the database/schema do not exist. Defaults to true if omitted."
      },
      {
        "name": "existing_pipeline_id",
        "type": "string",
        "description": "ID of an existing pipeline to bin-pack this synced table into. At most one of existing_pipeline_id and new_pipeline_spec should be defined. The pipeline used for the synced table is returned via the top level pipeline_id attribute."
      },
      {
        "name": "extra_columns",
        "type": "array",
        "description": "Extra PostgreSQL-only columns to add to the synced table.",
        "children": [
          {
            "name": "column_name",
            "type": "string",
            "description": "Name of the column."
          },
          {
            "name": "column_type",
            "type": "string",
            "description": "PostgreSQL type of the column, for example \"tsvector\" or \"vector(1024)\"."
          },
          {
            "name": "compute",
            "type": "string",
            "description": "SQL expression used to compute the column's value, for example \"to_tsvector('english', content)\"."
          },
          {
            "name": "maintenance",
            "type": "string",
            "description": "How the column's value is populated and kept up to date. (DEFAULT_VALUE, STORED_GENERATED)"
          }
        ]
      },
      {
        "name": "extra_index_definitions",
        "type": "array",
        "description": "Secondary indexes to create on the synced table.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Name of the index as it will appear in PostgreSQL."
          },
          {
            "name": "definition",
            "type": "string",
            "description": "The definition portion of a CREATE INDEX statement, placed after ON table_name. For example: USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64)."
          },
          {
            "name": "creation_point",
            "type": "string",
            "description": "When the index should be created relative to the initial data load. (CREATION_POINT_AFTER_DATA_LOAD)"
          }
        ]
      },
      {
        "name": "new_pipeline_spec",
        "type": "object",
        "description": "Specification for creating a new pipeline. At most one of existing_pipeline_id and new_pipeline_spec should be defined. The pipeline used for the synced table is returned via the top level pipeline_id attribute.",
        "children": [
          {
            "name": "budget_policy_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "pipeline_channel",
            "type": "string",
            "description": "Release channel of the underlying pipeline's runtime. Some source table configurations (e.g., read-time CDF) require PREVIEW. Defaults to CURRENT if not specified. (CURRENT, PREVIEW)"
          },
          {
            "name": "storage_catalog",
            "type": "string",
            "description": "UC catalog for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be a standard catalog where the user has permissions to create Delta tables."
          },
          {
            "name": "storage_schema",
            "type": "string",
            "description": "UC schema for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be in the standard catalog where the user has permissions to create Delta tables."
          }
        ]
      },
      {
        "name": "postgres_database",
        "type": "string",
        "description": "The Postgres database name where the synced table will be created in. If this synced table is created inside a Lakebase Catalog, this attribute can be omitted on creation and is inferred from the postgres_database associated with the Lakebase Catalog. If specified when inside a Lakebase Catalog, the value must match. A value must be specified when creating a synced table inside a Standard Catalog."
      },
      {
        "name": "primary_key_columns",
        "type": "array",
        "description": "Primary Key columns to be used for data insert/update in the destination."
      },
      {
        "name": "scheduling_policy",
        "type": "string",
        "description": "Scheduling policy of the underlying pipeline. (CONTINUOUS, SNAPSHOT, TRIGGERED)"
      },
      {
        "name": "source_table_full_name",
        "type": "string",
        "description": "Three-part (catalog, schema, table) name of the source Delta table. For the corresponding destination table, use any of the two: - synced_table_id used at the creation of the SyncedTable - \"name\" consisting of \"synced_tables/\" prefix and the full name of the destination table."
      },
      {
        "name": "timeseries_key",
        "type": "string",
        "description": "Time series key to deduplicate (tie-break) rows with the same primary key."
      },
      {
        "name": "type_overrides",
        "type": "array",
        "description": "Override the default Delta-&gt;PG type mapping for specific columns. A TypeOverride with PG_SPECIFIC_TYPE_UNSPECIFIED is rejected; a valid pg_type must be set.",
        "children": [
          {
            "name": "column_name",
            "type": "string",
            "description": "Name of the source column whose target PostgreSQL type should be overridden."
          },
          {
            "name": "pg_type",
            "type": "string",
            "description": "PostgreSQL-specific target type to use for the column. (PG_SPECIFIC_TYPE_HALFVEC, PG_SPECIFIC_TYPE_VARCHAR, PG_SPECIFIC_TYPE_VECTOR)"
          },
          {
            "name": "size",
            "type": "integer",
            "description": "Size parameter for the target type, for types that take one (e.g. vector dimension, varchar length). Required when the chosen pg_type needs a size."
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Synced Table data synchronization status.",
    "children": [
      {
        "name": "detailed_state",
        "type": "string",
        "description": "The state of a synced table. (SYNCED_TABLE_OFFLINE, SYNCED_TABLE_OFFLINE_FAILED, SYNCED_TABLE_ONLINE, SYNCED_TABLE_ONLINE_CONTINUOUS_UPDATE, SYNCED_TABLE_ONLINE_NO_PENDING_UPDATE, SYNCED_TABLE_ONLINE_PIPELINE_FAILED, SYNCED_TABLE_ONLINE_TRIGGERED_UPDATE, SYNCED_TABLE_ONLINE_UPDATING_PIPELINE_RESOURCES, SYNCED_TABLE_PROVISIONING, SYNCED_TABLE_PROVISIONING_INITIAL_SNAPSHOT, SYNCED_TABLE_PROVISIONING_PIPELINE_RESOURCES)"
      },
      {
        "name": "last_processed_commit_version",
        "type": "integer",
        "description": "The last source table Delta version that was successfully synced to the synced table."
      },
      {
        "name": "last_sync",
        "type": "object",
        "description": "Summary of the last successful synchronization from source to destination.",
        "children": [
          {
            "name": "delta_table_sync_info",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "delta_commit_time",
                "type": "string (date-time)",
                "description": ""
              },
              {
                "name": "delta_commit_version",
                "type": "integer",
                "description": "The Delta Lake commit version that was last successfully synced."
              }
            ]
          },
          {
            "name": "sync_end_time",
            "type": "string (date-time)",
            "description": "The end timestamp of the most recent successful synchronization. This is the time when the data is available in the synced table."
          },
          {
            "name": "sync_start_time",
            "type": "string (date-time)",
            "description": "The starting timestamp of the most recent successful synchronization from the source table to the destination (synced) table. Note this is the starting timestamp of the sync operation, not the end time. E.g., for a batch, this is the time when the sync operation started."
          }
        ]
      },
      {
        "name": "last_sync_time",
        "type": "string (date-time)",
        "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. This is when the data is available in the synced table."
      },
      {
        "name": "message",
        "type": "string",
        "description": "A text description of the current state of the synced table."
      },
      {
        "name": "ongoing_sync_progress",
        "type": "object",
        "description": "Progress information of the Synced Table data synchronization pipeline.",
        "children": [
          {
            "name": "estimated_completion_time_seconds",
            "type": "number",
            "description": "The estimated time remaining to complete this update in seconds."
          },
          {
            "name": "latest_version_currently_processing",
            "type": "integer",
            "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
          },
          {
            "name": "sync_progress_completion",
            "type": "number",
            "description": "The completion ratio of this update. This is a number between 0 and 1."
          },
          {
            "name": "synced_row_count",
            "type": "integer",
            "description": "The number of rows that have been synced in this update."
          },
          {
            "name": "total_row_count",
            "type": "integer",
            "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
          }
        ]
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "ID of the associated pipeline."
      },
      {
        "name": "project",
        "type": "string",
        "description": "The full resource name of the project associated with the table. Format: \"projects/&#123;project_id&#125;\"."
      },
      {
        "name": "provisioning_phase",
        "type": "string",
        "description": "The current phase of the data synchronization pipeline. (PROVISIONING_PHASE_INDEX_SCAN, PROVISIONING_PHASE_INDEX_SORT, PROVISIONING_PHASE_MAIN)"
      },
      {
        "name": "unity_catalog_provisioning_state",
        "type": "string",
        "description": "The provisioning state of the synced table entity in Unity Catalog. (ACTIVE, DEGRADED, DELETING, FAILED, PROVISIONING, UPDATING)"
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "The Unity Catalog table ID for this synced table."
  }
]} />
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of Postgres roles in the branch.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a Synced Table.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-role"><code>role</code></a></td>
    <td><a href="#parameter-replace_existing"><code>replace_existing</code></a>, <a href="#parameter-role_id"><code>role_id</code></a></td>
    <td>Creates a new Postgres role in the branch.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a Synced Table.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The Full resource name of the synced table, of the format "synced_tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;", where (catalog, schema, table) are the UC entity names.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Branch where this Role is created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned. Cannot be negative.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
</tr>
<tr id="parameter-replace_existing">
    <td><CopyableCode code="replace_existing" /></td>
    <td><code>boolean</code></td>
    <td>If true, update the role if it already exists instead of returning an error. When the role already exists, the provided ``role`` spec fully replaces the existing one: ``membership_roles`` is overwritten, not merged. Leaving ``membership_roles`` empty clears all of the role's existing memberships, including ``DATABRICKS_SUPERUSER``. Always send the complete desired list of memberships when using this field.</td>
</tr>
<tr id="parameter-role_id">
    <td><CopyableCode code="role_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="list">

Returns a paginated list of Postgres roles in the branch.

```sql
SELECT
name,
role_id,
create_time,
parent,
spec,
status,
update_time
FROM databricks_workspace.postgres.postgres_roles
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Get a Synced Table.

```sql
SELECT
name,
synced_table_id,
create_time,
spec,
status,
uid
FROM databricks_workspace.postgres.postgres_roles
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
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

Creates a new Postgres role in the branch.

```sql
INSERT INTO databricks_workspace.postgres.postgres_roles (
role,
parent,
deployment_name,
replace_existing,
role_id
)
SELECT 
'{{ role }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}',
'{{ replace_existing }}',
'{{ role_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_roles
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the postgres_roles resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_roles resource.
    - name: role
      description: |
        The desired specification of a Role.
      value:
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        parent: "{{ parent }}"
        role_id: "{{ role_id }}"
        spec:
          attributes:
            bypassrls: {{ bypassrls }}
            createdb: {{ createdb }}
            createrole: {{ createrole }}
          auth_method: "{{ auth_method }}"
          identity_type: "{{ identity_type }}"
          membership_roles:
            - "{{ membership_roles }}"
          postgres_role: "{{ postgres_role }}"
        status:
          attributes:
            bypassrls: {{ bypassrls }}
            createdb: {{ createdb }}
            createrole: {{ createrole }}
          auth_method: "{{ auth_method }}"
          identity_type: "{{ identity_type }}"
          membership_roles:
            - "{{ membership_roles }}"
          postgres_role: "{{ postgres_role }}"
          role_id: "{{ role_id }}"
        update_time: "{{ update_time }}"
    - name: replace_existing
      value: {{ replace_existing }}
      description: If true, update the role if it already exists instead of returning an error. When the role already exists, the provided \`\`role\`\` spec fully replaces the existing one: \`\`membership_roles\`\` is overwritten, not merged. Leaving \`\`membership_roles\`\` empty clears all of the role's existing memberships, including \`\`DATABRICKS_SUPERUSER\`\`. Always send the complete desired list of memberships when using this field.
      description: If true, update the role if it already exists instead of returning an error. When the role already exists, the provided \`\`role\`\` spec fully replaces the existing one: \`\`membership_roles\`\` is overwritten, not merged. Leaving \`\`membership_roles\`\` empty clears all of the role's existing memberships, including \`\`DATABRICKS_SUPERUSER\`\`. Always send the complete desired list of memberships when using this field.
    - name: role_id
      value: "{{ role_id }}"
      description: The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.
      description: The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.
`}</CodeBlock>

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

Delete a Synced Table.

```sql
DELETE FROM databricks_workspace.postgres.postgres_roles
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
