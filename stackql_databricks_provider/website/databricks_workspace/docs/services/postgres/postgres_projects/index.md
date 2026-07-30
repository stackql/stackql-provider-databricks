---
title: postgres_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_projects
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

Creates, updates, deletes, gets or lists a <code>postgres_projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_projects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_projects" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the project. Format: projects/&#123;project_id&#125;"
  },
  {
    "name": "project_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "delete_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project was soft-deleted. Empty if the project is not deleted, otherwise set to a timestamp in the past."
  },
  {
    "name": "initial_branch_spec",
    "type": "object",
    "description": "Configuration for the initial default branch created as part of project creation. Allows overriding branch protection. These settings only apply at creation time and do not affect resources created after project creation.",
    "children": [
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "Whether the initial default branch should be protected from deletion."
      }
    ]
  },
  {
    "name": "initial_database_spec",
    "type": "object",
    "description": "Configuration for the initial Postgres database created inside the initial branch for this project. If omitted, the initial branch still gets an initial database with name ``databricks_postgres``. The initial database is always owned by the initial role (caller-provided via ``initial_role_spec`` or defaulted to the caller's identity). This field is input-only; to change databases after project creation, use the standalone Database API.",
    "children": [
      {
        "name": "postgres_database",
        "type": "string",
        "description": "The name of the Postgres database. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS"
      }
    ]
  },
  {
    "name": "initial_endpoint_spec",
    "type": "object",
    "description": "Configuration settings for the initial Read/Write endpoint created inside the initial branch for a newly created project. If omitted, the initial endpoint created will have default settings, without high availability configured. This field does not apply to any endpoints created after project creation. Use spec.default_endpoint_settings to configure default settings for endpoints created after project creation.",
    "children": [
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": "The maximum number of Compute Units for the initial endpoint."
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units for the initial endpoint."
      },
      {
        "name": "group",
        "type": "object",
        "description": "Settings for HA configuration of the endpoint.",
        "children": [
          {
            "name": "min",
            "type": "integer",
            "description": ""
          },
          {
            "name": "max",
            "type": "integer",
            "description": "The maximum number of computes in the endpoint group. Currently, this must be equal to min. Set to 1 for single compute endpoints, to disable HA. To manually suspend all computes in an endpoint group, set disabled to true on the EndpointSpec."
          },
          {
            "name": "enable_readable_secondaries",
            "type": "boolean",
            "description": "Whether to allow read-only connections to read-write endpoints. Only relevant for read-write endpoints where size.max &gt; 1."
          }
        ]
      },
      {
        "name": "no_suspension",
        "type": "boolean",
        "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``."
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the initial endpoint is automatically suspended. If specified, should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
      }
    ]
  },
  {
    "name": "initial_role_spec",
    "type": "object",
    "description": "Configuration for the initial Postgres role created inside the initial branch for this project. If omitted, the initial branch gets an initial role corresponding to the caller of the API endpoint. This field is input-only; to change roles after project creation, use the standalone Role API.",
    "children": [
      {
        "name": "attributes",
        "type": "object",
        "description": "The desired API-exposed Postgres role attribute to associate with the role. Optional.",
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
        "description": "The name of the Postgres role. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS If you wish to create a Postgres Role backed by a managed Databricks identity, then postgres_role must be one of the following: 1. user email for IdentityType.USER 2. app ID for IdentityType.SERVICE_PRINCIPAL 3. group name for IdentityType.GROUP"
      }
    ]
  },
  {
    "name": "purge_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project is scheduled for permanent deletion. Empty if the project is not deleted, otherwise set to a timestamp in the future."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the project configuration, including display_name, pg_version (Postgres version), history_retention_duration, and default_endpoint_settings.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "compute_provisioner",
        "type": "string",
        "description": "The compute provisioner used to provision endpoints in this project. Overrides the default provisioner when set."
      },
      {
        "name": "custom_tags",
        "type": "array",
        "description": "Custom tags to associate with the project. Forwarded to LBM for billing and cost tracking. To update tags, provide the new tag list and include \"spec.custom_tags\" in the update_mask. To clear all tags, provide an empty list and include \"spec.custom_tags\" in the update_mask. To preserve existing tags, omit this field from the update_mask (or use wildcard \"*\" which auto-excludes empty tags).",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the custom tag."
          }
        ]
      },
      {
        "name": "default_branch",
        "type": "string",
        "description": "The full resource path for the default branch of the project Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``. When updating, use ``spec.project_default_settings.suspension`` in the update_mask."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``. When updating, use ``spec.project_default_settings.suspension`` in the update_mask."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "Human-readable project name. Length should be between 1 and 256 characters."
      },
      {
        "name": "enable_pg_native_login",
        "type": "boolean",
        "description": "Whether to enable PG native password login on all endpoints in this project. Defaults to false."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The number of seconds to retain the shared history for point in time recovery for all branches in this project. Value should be between 172800s (2 days) and 3024000s (35 days)."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The major Postgres version number. The set of supported versions may vary; consult the API documentation for currently accepted values."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of a Project.",
    "children": [
      {
        "name": "branch_logical_size_limit_bytes",
        "type": "integer",
        "description": ""
      },
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": "The budget policy that is applied to the project."
      },
      {
        "name": "compute_last_active_time",
        "type": "string (date-time)",
        "description": "The most recent time when any endpoint of this project was active."
      },
      {
        "name": "compute_provisioner",
        "type": "string",
        "description": "The effective compute provisioner backing this project's endpoints."
      },
      {
        "name": "custom_tags",
        "type": "array",
        "description": "The effective custom tags associated with the project.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the custom tag."
          }
        ]
      },
      {
        "name": "default_branch",
        "type": "string",
        "description": "The full resource path of the default branch of the project"
      },
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``. When updating, use ``spec.project_default_settings.suspension`` in the update_mask."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``. When updating, use ``spec.project_default_settings.suspension`` in the update_mask."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "The effective human-readable project name."
      },
      {
        "name": "enable_pg_native_login",
        "type": "boolean",
        "description": "Whether to enable PG native password login on all endpoints in this project."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The effective number of seconds to retain the shared history for point in time recovery."
      },
      {
        "name": "owner",
        "type": "string",
        "description": "The email of the project owner."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The effective major Postgres version number."
      },
      {
        "name": "project_id",
        "type": "string",
        "description": "Part of the resource name."
      },
      {
        "name": "replication_role",
        "type": "string",
        "description": "The replication role of the project in this workspace. Populated only when cross-workspace replication is configured. (REPLICATION_ROLE_PREVIEW_DEMOTING, REPLICATION_ROLE_PREVIEW_PRIMARY, REPLICATION_ROLE_PREVIEW_SECONDARY)"
      },
      {
        "name": "synthetic_storage_size_bytes",
        "type": "integer",
        "description": "The current space occupied by the project in storage."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the project."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project was last updated."
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-show_deleted"><code>show_deleted</code></a></td>
    <td>Returns a paginated list of database projects in the workspace that the user has permission to access.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-project"><code>project</code></a></td>
    <td></td>
    <td>Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-snapshot_schedule"><code>snapshot_schedule</code></a></td>
    <td></td>
    <td>Sets the snapshot schedule for a branch. The ``schedule`` field is replaced wholesale; an empty</td>
</tr>
<tr>
    <td><a href="#undelete"><CopyableCode code="undelete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Undeletes a soft-deleted project.</td>
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
    <td>The full resource path of the project to undelete. Format: projects/&#123;project_id&#125;</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Project. This becomes the final component of the project's resource name. The ID is required and must be 1-63 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens. For example, ``my-app`` becomes ``projects/my-app``.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. The only updatable path is ``schedule``, which replaces the entire set of cadences.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned. Cannot be negative. The maximum value is 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
</tr>
<tr id="parameter-show_deleted">
    <td><CopyableCode code="show_deleted" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include soft-deleted projects in the response. When true, soft-deleted projects are included alongside active projects. Hard-deleted and already-purged projects are never returned.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Returns a paginated list of database projects in the workspace that the user has permission to access.

```sql
SELECT
name,
project_id,
create_time,
delete_time,
initial_branch_spec,
initial_database_spec,
initial_endpoint_spec,
initial_role_spec,
purge_time,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_projects
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND show_deleted = '{{ show_deleted }}'
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

Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute

```sql
INSERT INTO databricks_workspace.postgres.postgres_projects (
project,
project_id,
deployment_name
)
SELECT 
'{{ project }}' /* required */,
'{{ project_id }}',
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_projects
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the postgres_projects resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_projects resource.
    - name: project
      description: |
        The Project to create.
      value:
        create_time: "{{ create_time }}"
        delete_time: "{{ delete_time }}"
        initial_branch_spec:
          is_protected: {{ is_protected }}
        initial_database_spec:
          postgres_database: "{{ postgres_database }}"
        initial_endpoint_spec:
          autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
          autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
          group:
            min: {{ min }}
            max: {{ max }}
            enable_readable_secondaries: {{ enable_readable_secondaries }}
          no_suspension: {{ no_suspension }}
          suspend_timeout_duration: "{{ suspend_timeout_duration }}"
        initial_role_spec:
          attributes:
            bypassrls: {{ bypassrls }}
            createdb: {{ createdb }}
            createrole: {{ createrole }}
          auth_method: "{{ auth_method }}"
          identity_type: "{{ identity_type }}"
          membership_roles:
            - "{{ membership_roles }}"
          postgres_role: "{{ postgres_role }}"
        name: "{{ name }}"
        project_id: "{{ project_id }}"
        purge_time: "{{ purge_time }}"
        spec:
          budget_policy_id: "{{ budget_policy_id }}"
          compute_provisioner: "{{ compute_provisioner }}"
          custom_tags:
            - key: "{{ key }}"
              value: "{{ value }}"
          default_branch: "{{ default_branch }}"
          default_endpoint_settings:
            autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
            autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
            no_suspension: {{ no_suspension }}
            pg_settings: "{{ pg_settings }}"
            suspend_timeout_duration: "{{ suspend_timeout_duration }}"
          display_name: "{{ display_name }}"
          enable_pg_native_login: {{ enable_pg_native_login }}
          history_retention_duration: "{{ history_retention_duration }}"
          pg_version: {{ pg_version }}
        status:
          branch_logical_size_limit_bytes: {{ branch_logical_size_limit_bytes }}
          budget_policy_id: "{{ budget_policy_id }}"
          compute_last_active_time: "{{ compute_last_active_time }}"
          compute_provisioner: "{{ compute_provisioner }}"
          custom_tags:
            - key: "{{ key }}"
              value: "{{ value }}"
          default_branch: "{{ default_branch }}"
          default_endpoint_settings:
            autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
            autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
            no_suspension: {{ no_suspension }}
            pg_settings: "{{ pg_settings }}"
            suspend_timeout_duration: "{{ suspend_timeout_duration }}"
          display_name: "{{ display_name }}"
          enable_pg_native_login: {{ enable_pg_native_login }}
          history_retention_duration: "{{ history_retention_duration }}"
          owner: "{{ owner }}"
          pg_version: {{ pg_version }}
          project_id: "{{ project_id }}"
          replication_role: "{{ replication_role }}"
          synthetic_storage_size_bytes: {{ synthetic_storage_size_bytes }}
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
`}</CodeBlock>

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

Sets the snapshot schedule for a branch. The ``schedule`` field is replaced wholesale; an empty

```sql
UPDATE databricks_workspace.postgres.postgres_projects
SET 
snapshot_schedule = '{{ snapshot_schedule }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND snapshot_schedule = '{{ snapshot_schedule }}' --required
RETURNING
name,
schedule;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="undelete"
    values={[
        { label: 'undelete', value: 'undelete' }
    ]}
>
<TabItem value="undelete">

Undeletes a soft-deleted project.

```sql
EXEC databricks_workspace.postgres.postgres_projects.undelete 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
