---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - bundledeployments
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

Creates, updates, deletes, gets or lists a <code>versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.bundledeployments.versions" /></td></tr>
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
    "description": "Resource name of the version. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;"
  },
  {
    "name": "previous_version_id",
    "type": "string",
    "description": "The version_id this version was created on top of — the deployment's most recent version at creation time. Leave unset when creating the first version (the deployment has no prior versions). Set by the client on creation and immutable thereafter. Acts as an optimistic-concurrency precondition: the server requires it to equal the deployment's current most-recent version (and to be unset when the deployment has no versions) and returns ``INVALID_PARAMETER_VALUE`` on mismatch, so a deploy racing against a concurrent deploy is rejected rather than silently overwriting it."
  },
  {
    "name": "version_id",
    "type": "string",
    "description": "Version identifier within the parent deployment, assigned by the client on creation. A numeric string (base-10, fits in a signed 64-bit integer) that is greater than or equal to 1. Version IDs are strictly increasing within a deployment but are not required to start at 1 or to be contiguous."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name for the deployment, captured at the time of this version. Up to 256 characters. When present, creating the version updates the deployment display name. An empty value clears it; an absent value leaves the current deployment display name unchanged."
  },
  {
    "name": "target_name",
    "type": "string",
    "description": "Target name of the deployment, captured at the time of this version."
  },
  {
    "name": "cli_version",
    "type": "string",
    "description": "CLI version used to initiate the version."
  },
  {
    "name": "complete_time",
    "type": "string (date-time)",
    "description": "When the version completed. Unset while the version is in progress."
  },
  {
    "name": "completed_by",
    "type": "string",
    "description": "The user who completed the version (email or principal name). May differ from ``created_by`` when another user force-completes the version."
  },
  {
    "name": "completion_reason",
    "type": "string",
    "description": "Why the version was completed. Unset while in progress. Set when status transitions to COMPLETED. (VERSION_COMPLETE_FAILURE, VERSION_COMPLETE_FORCE_ABORT, VERSION_COMPLETE_LEASE_EXPIRED, VERSION_COMPLETE_SUCCESS)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the version was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The user who created the version (email or principal name)."
  },
  {
    "name": "deployment_mode",
    "type": "string",
    "description": "Bundle target deployment mode (development or production), captured at the time of this version. (DEPLOYMENT_MODE_DEVELOPMENT, DEPLOYMENT_MODE_PRODUCTION)"
  },
  {
    "name": "git_info",
    "type": "object",
    "description": "Git provenance of the source, captured at the time of this version.",
    "children": [
      {
        "name": "branch",
        "type": "string",
        "description": "Branch the source was deployed from."
      },
      {
        "name": "commit",
        "type": "string",
        "description": "Commit SHA of the deployed source."
      },
      {
        "name": "origin_url",
        "type": "string",
        "description": "URL of the git remote the source was deployed from."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the version: IN_PROGRESS or COMPLETED. (VERSION_STATUS_COMPLETED, VERSION_STATUS_IN_PROGRESS)"
  },
  {
    "name": "version_type",
    "type": "string",
    "description": "Type of version (deploy or destroy). (VERSION_TYPE_DEPLOY, VERSION_TYPE_DESTROY)"
  },
  {
    "name": "workspace_info",
    "type": "object",
    "description": "Workspace location of the deployment, captured at the time of this version.",
    "children": [
      {
        "name": "bundle_root_path",
        "type": "string",
        "description": "Path of the bundle root (the directory containing databricks.yml) relative to git_folder_path. Empty when the deployment is not from a Databricks Git folder."
      },
      {
        "name": "file_path",
        "type": "string",
        "description": "Absolute workspace path where the deployed bundle files live. Mirrors the workspace.file_path field in DABs bundle config."
      },
      {
        "name": "git_folder_path",
        "type": "string",
        "description": "When deployed from a Databricks Git folder, the absolute workspace path of that folder; empty for local deploys."
      },
      {
        "name": "root_path",
        "type": "string",
        "description": "Absolute workspace path of the deployment root — the base path the deployed files live under. Mirrors workspace.root_path in the DABs bundle config; file_path is its files subdirectory."
      },
      {
        "name": "source_linked",
        "type": "boolean",
        "description": "Whether files are served directly from the source sync root instead of being copied into file_path."
      }
    ]
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name of the version. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;"
  },
  {
    "name": "previous_version_id",
    "type": "string",
    "description": "The version_id this version was created on top of — the deployment's most recent version at creation time. Leave unset when creating the first version (the deployment has no prior versions). Set by the client on creation and immutable thereafter. Acts as an optimistic-concurrency precondition: the server requires it to equal the deployment's current most-recent version (and to be unset when the deployment has no versions) and returns ``INVALID_PARAMETER_VALUE`` on mismatch, so a deploy racing against a concurrent deploy is rejected rather than silently overwriting it."
  },
  {
    "name": "version_id",
    "type": "string",
    "description": "Version identifier within the parent deployment, assigned by the client on creation. A numeric string (base-10, fits in a signed 64-bit integer) that is greater than or equal to 1. Version IDs are strictly increasing within a deployment but are not required to start at 1 or to be contiguous."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name for the deployment, captured at the time of this version. Up to 256 characters. When present, creating the version updates the deployment display name. An empty value clears it; an absent value leaves the current deployment display name unchanged."
  },
  {
    "name": "target_name",
    "type": "string",
    "description": "Target name of the deployment, captured at the time of this version."
  },
  {
    "name": "cli_version",
    "type": "string",
    "description": "CLI version used to initiate the version."
  },
  {
    "name": "complete_time",
    "type": "string (date-time)",
    "description": "When the version completed. Unset while the version is in progress."
  },
  {
    "name": "completed_by",
    "type": "string",
    "description": "The user who completed the version (email or principal name). May differ from ``created_by`` when another user force-completes the version."
  },
  {
    "name": "completion_reason",
    "type": "string",
    "description": "Why the version was completed. Unset while in progress. Set when status transitions to COMPLETED. (VERSION_COMPLETE_FAILURE, VERSION_COMPLETE_FORCE_ABORT, VERSION_COMPLETE_LEASE_EXPIRED, VERSION_COMPLETE_SUCCESS)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the version was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The user who created the version (email or principal name)."
  },
  {
    "name": "deployment_mode",
    "type": "string",
    "description": "Bundle target deployment mode (development or production), captured at the time of this version. (DEPLOYMENT_MODE_DEVELOPMENT, DEPLOYMENT_MODE_PRODUCTION)"
  },
  {
    "name": "git_info",
    "type": "object",
    "description": "Git provenance of the source, captured at the time of this version.",
    "children": [
      {
        "name": "branch",
        "type": "string",
        "description": "Branch the source was deployed from."
      },
      {
        "name": "commit",
        "type": "string",
        "description": "Commit SHA of the deployed source."
      },
      {
        "name": "origin_url",
        "type": "string",
        "description": "URL of the git remote the source was deployed from."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the version: IN_PROGRESS or COMPLETED. (VERSION_STATUS_COMPLETED, VERSION_STATUS_IN_PROGRESS)"
  },
  {
    "name": "version_type",
    "type": "string",
    "description": "Type of version (deploy or destroy). (VERSION_TYPE_DEPLOY, VERSION_TYPE_DESTROY)"
  },
  {
    "name": "workspace_info",
    "type": "object",
    "description": "Workspace location of the deployment, captured at the time of this version.",
    "children": [
      {
        "name": "bundle_root_path",
        "type": "string",
        "description": "Path of the bundle root (the directory containing databricks.yml) relative to git_folder_path. Empty when the deployment is not from a Databricks Git folder."
      },
      {
        "name": "file_path",
        "type": "string",
        "description": "Absolute workspace path where the deployed bundle files live. Mirrors the workspace.file_path field in DABs bundle config."
      },
      {
        "name": "git_folder_path",
        "type": "string",
        "description": "When deployed from a Databricks Git folder, the absolute workspace path of that folder; empty for local deploys."
      },
      {
        "name": "root_path",
        "type": "string",
        "description": "Absolute workspace path of the deployment root — the base path the deployed files live under. Mirrors workspace.root_path in the DABs bundle config; file_path is its files subdirectory."
      },
      {
        "name": "source_linked",
        "type": "boolean",
        "description": "Whether files are served directly from the source sync root instead of being copied into file_path."
      }
    ]
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
    <td>Lists versions under a deployment, ordered numerically by version_id descending (most recent first).</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves a version by its resource name.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-version"><code>version</code></a></td>
    <td></td>
    <td>Creates a new version under a deployment.</td>
</tr>
<tr>
    <td><a href="#complete"><CopyableCode code="complete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-completion_reason"><code>completion_reason</code></a></td>
    <td></td>
    <td>Marks a version as complete and releases the deployment lock.</td>
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
    <td>The name of the version to complete. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The parent deployment where this version will be created. Format: deployments/&#123;deployment_id&#125;</td>
</tr>
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the version, which becomes the final component of the version's resource name. A numeric string (base-10, fits in a signed 64-bit integer) chosen by the caller; must be greater than or equal to 1. Must be numerically greater than the deployment's most recent version (see ``version.previous_version_id``); it does not need to start at 1 or increase by exactly 1. If the value is not numerically greater, the server returns ``INVALID_PARAMETER_VALUE``.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 20 versions will be returned. The maximum value is 100; values above 100 will be coerced to 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListVersions`` call. Provide this to retrieve the subsequent page.</td>
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

Lists versions under a deployment, ordered numerically by version_id descending (most recent first).

```sql
SELECT
name,
previous_version_id,
version_id,
display_name,
target_name,
cli_version,
complete_time,
completed_by,
completion_reason,
create_time,
created_by,
deployment_mode,
git_info,
status,
version_type,
workspace_info
FROM databricks_workspace.bundledeployments.versions
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Retrieves a version by its resource name.

```sql
SELECT
name,
previous_version_id,
version_id,
display_name,
target_name,
cli_version,
complete_time,
completed_by,
completion_reason,
create_time,
created_by,
deployment_mode,
git_info,
status,
version_type,
workspace_info
FROM databricks_workspace.bundledeployments.versions
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

Creates a new version under a deployment.

```sql
INSERT INTO databricks_workspace.bundledeployments.versions (
version,
parent,
version_id,
deployment_name
)
SELECT 
'{{ version }}' /* required */,
'{{ parent }}',
'{{ version_id }}',
'{{ deployment_name }}'
RETURNING
name,
previous_version_id,
version_id,
display_name,
target_name,
cli_version,
complete_time,
completed_by,
completion_reason,
create_time,
created_by,
deployment_mode,
git_info,
status,
version_type,
workspace_info
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: versions
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the versions resource.
    - name: version_id
      value: "{{ version_id }}"
      description: Required parameter for the versions resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the versions resource.
    - name: version
      description: |
        The version to create.
      value:
        cli_version: "{{ cli_version }}"
        version_type: "{{ version_type }}"
        complete_time: "{{ complete_time }}"
        completed_by: "{{ completed_by }}"
        completion_reason: "{{ completion_reason }}"
        create_time: "{{ create_time }}"
        created_by: "{{ created_by }}"
        deployment_mode: "{{ deployment_mode }}"
        display_name: "{{ display_name }}"
        git_info:
          branch: "{{ branch }}"
          commit: "{{ commit }}"
          origin_url: "{{ origin_url }}"
        name: "{{ name }}"
        previous_version_id: "{{ previous_version_id }}"
        status: "{{ status }}"
        target_name: "{{ target_name }}"
        version_id: "{{ version_id }}"
        workspace_info:
          bundle_root_path: "{{ bundle_root_path }}"
          file_path: "{{ file_path }}"
          git_folder_path: "{{ git_folder_path }}"
          root_path: "{{ root_path }}"
          source_linked: {{ source_linked }}
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="complete"
    values={[
        { label: 'complete', value: 'complete' }
    ]}
>
<TabItem value="complete">

Marks a version as complete and releases the deployment lock.

```sql
EXEC databricks_workspace.bundledeployments.versions.complete 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"completion_reason": "{{ completion_reason }}", 
"force": {{ force }}
}'
;
```
</TabItem>
</Tabs>
