---
title: deployment_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_resources
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

Creates, updates, deletes, gets or lists a <code>deployment_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployment_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.bundledeployments.deployment_resources" /></td></tr>
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
    "description": "Resource name. Format: deployments/&#123;deployment_id&#125;/resources/&#123;resource_key&#125;"
  },
  {
    "name": "last_version_id",
    "type": "string",
    "description": "The version_id of the last version where this resource was updated."
  },
  {
    "name": "resource_id",
    "type": "string",
    "description": "ID that references the actual resource in the workspace (e.g. the job ID, pipeline ID)."
  },
  {
    "name": "dashboard_metadata",
    "type": "object",
    "description": "Dashboard-specific metadata; set only for dashboard resources.",
    "children": [
      {
        "name": "definition_path",
        "type": "string",
        "description": "Path of the file that declares this dashboard, relative to the bundle's workspace.file_path (Version.workspace_info.file_path) — join the two to get the file's absolute workspace path. For now this lives only on the dashboard metadata, and is a single string because it was a single string (``relative_path``) in the legacy bundle metadata.json. We may generalize it in the future: lifting it to a top-level field on Resource/Operation (every resource type has a definition location) and converting it to a repeated field, since a resource can be declared across multiple files/locations."
      },
      {
        "name": "source_path",
        "type": "string",
        "description": "Path of the dashboard's source artifact (its ``.lvdash.json``), relative to the deployment root."
      }
    ]
  },
  {
    "name": "last_action_type",
    "type": "string",
    "description": "The action performed on this resource during the last version. (OPERATION_ACTION_TYPE_BIND, OPERATION_ACTION_TYPE_BIND_AND_UPDATE, OPERATION_ACTION_TYPE_CREATE, OPERATION_ACTION_TYPE_DELETE, OPERATION_ACTION_TYPE_INITIAL_REGISTER, OPERATION_ACTION_TYPE_RECREATE, OPERATION_ACTION_TYPE_RESIZE, OPERATION_ACTION_TYPE_UPDATE, OPERATION_ACTION_TYPE_UPDATE_WITH_ID)"
  },
  {
    "name": "resource_key",
    "type": "string",
    "description": "Resource identifier within the bundle (e.g. \"jobs.foo\", \"pipelines.bar\", \"jobs.foo.permissions\")."
  },
  {
    "name": "resource_type",
    "type": "string",
    "description": "The type of the deployment resource. (DEPLOYMENT_RESOURCE_TYPE_ALERT, DEPLOYMENT_RESOURCE_TYPE_APP, DEPLOYMENT_RESOURCE_TYPE_CATALOG, DEPLOYMENT_RESOURCE_TYPE_CLUSTER, DEPLOYMENT_RESOURCE_TYPE_DASHBOARD, DEPLOYMENT_RESOURCE_TYPE_DATABASE_CATALOG, DEPLOYMENT_RESOURCE_TYPE_DATABASE_INSTANCE, DEPLOYMENT_RESOURCE_TYPE_EXPERIMENT, DEPLOYMENT_RESOURCE_TYPE_EXTERNAL_LOCATION, DEPLOYMENT_RESOURCE_TYPE_JOB, DEPLOYMENT_RESOURCE_TYPE_MODEL, DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_PIPELINE, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT, DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR, DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL, DEPLOYMENT_RESOURCE_TYPE_SCHEMA, DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE, DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE, DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE, DEPLOYMENT_RESOURCE_TYPE_VOLUME)"
  },
  {
    "name": "state",
    "type": "object",
    "description": "Serialized local config state (what the CLI deployed)."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the last operation that updated this resource's recorded state was applied. Pairs with last_action_type and last_version_id (all three advance together on that write)."
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
    <td>Lists resources under a deployment.</td>
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
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The parent deployment. Format: deployments/&#123;deployment_id&#125;</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return. The service may return fewer than this value. If unspecified, at most 50 resources will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListResources`` call. Provide this to retrieve the subsequent page.</td>
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

Lists resources under a deployment.

```sql
SELECT
name,
last_version_id,
resource_id,
dashboard_metadata,
last_action_type,
resource_key,
resource_type,
state,
update_time
FROM databricks_workspace.bundledeployments.deployment_resources
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>
