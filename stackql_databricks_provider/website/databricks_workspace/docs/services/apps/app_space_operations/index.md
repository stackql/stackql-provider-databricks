---
title: app_space_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - app_space_operations
  - apps
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

Creates, updates, deletes, gets or lists an <code>app_space_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_space_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.app_space_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the ``name`` should be a resource name ending with ``operations/&#123;unique_id&#125;``."
  },
  {
    "name": "done",
    "type": "boolean",
    "description": "If the value is ``false``, it means the operation is still in progress. If ``true``, the operation is completed, and either ``error`` or ``response`` is available."
  },
  {
    "name": "error",
    "type": "object",
    "description": "The error result of the operation in case of failure or cancellation.",
    "children": [
      {
        "name": "details",
        "type": "array",
        "description": ""
      },
      {
        "name": "error_code",
        "type": "string",
        "description": "Error codes returned by Databricks APIs to indicate specific failure conditions. (ABORTED, ALREADY_EXISTS, BAD_REQUEST, CANCELLED, CATALOG_ALREADY_EXISTS, CATALOG_DOES_NOT_EXIST, CATALOG_NOT_EMPTY, COULD_NOT_ACQUIRE_LOCK, CUSTOMER_UNAUTHORIZED, DAC_ALREADY_EXISTS, DAC_DOES_NOT_EXIST, DATA_LOSS, DEADLINE_EXCEEDED, DEPLOYMENT_TIMEOUT, DIRECTORY_NOT_EMPTY, DIRECTORY_PROTECTED, DRY_RUN_FAILED, ENDPOINT_NOT_FOUND, EXTERNAL_LOCATION_ALREADY_EXISTS, EXTERNAL_LOCATION_DOES_NOT_EXIST, FEATURE_DISABLED, GIT_CONFLICT, GIT_REMOTE_ERROR, GIT_SENSITIVE_TOKEN_DETECTED, GIT_UNKNOWN_REF, GIT_URL_NOT_ON_ALLOW_LIST, INSECURE_PARTNER_RESPONSE, INTERNAL_ERROR, INVALID_PARAMETER_VALUE, INVALID_STATE, INVALID_STATE_TRANSITION, IO_ERROR, IPYNB_FILE_IN_REPO, MALFORMED_PARTNER_RESPONSE, MALFORMED_REQUEST, MANAGED_RESOURCE_GROUP_DOES_NOT_EXIST, MAX_BLOCK_SIZE_EXCEEDED, MAX_CHILD_NODE_SIZE_EXCEEDED, MAX_LIST_SIZE_EXCEEDED, MAX_NOTEBOOK_SIZE_EXCEEDED, MAX_READ_SIZE_EXCEEDED, METASTORE_ALREADY_EXISTS, METASTORE_DOES_NOT_EXIST, METASTORE_NOT_EMPTY, NOT_FOUND, NOT_IMPLEMENTED, PARTIAL_DELETE, PERMISSION_DENIED, PERMISSION_NOT_PROPAGATED, PRINCIPAL_DOES_NOT_EXIST, PROJECTS_OPERATION_TIMEOUT, PROVIDER_ALREADY_EXISTS, PROVIDER_DOES_NOT_EXIST, PROVIDER_SHARE_NOT_ACCESSIBLE, QUOTA_EXCEEDED, RECIPIENT_ALREADY_EXISTS, RECIPIENT_DOES_NOT_EXIST, REQUEST_LIMIT_EXCEEDED, RESOURCE_ALREADY_EXISTS, RESOURCE_CONFLICT, RESOURCE_DOES_NOT_EXIST, RESOURCE_EXHAUSTED, RESOURCE_LIMIT_EXCEEDED, SCHEMA_ALREADY_EXISTS, SCHEMA_DOES_NOT_EXIST, SCHEMA_NOT_EMPTY, SEARCH_QUERY_TOO_LONG, SEARCH_QUERY_TOO_SHORT, SERVICE_UNDER_MAINTENANCE, SHARE_ALREADY_EXISTS, SHARE_DOES_NOT_EXIST, STORAGE_CREDENTIAL_ALREADY_EXISTS, STORAGE_CREDENTIAL_DOES_NOT_EXIST, TABLE_ALREADY_EXISTS, TABLE_DOES_NOT_EXIST, TEMPORARILY_UNAVAILABLE, UNAUTHENTICATED, UNAVAILABLE, UNKNOWN, UNPARSEABLE_HTTP_ERROR, WORKSPACE_TEMPORARILY_UNAVAILABLE)"
      },
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "stack_trace",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata."
  },
  {
    "name": "response",
    "type": "object",
    "description": "The normal, successful response of the operation."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the status of an app space update operation.</td>
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
    <td>The name of the operation resource.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the status of an app space update operation.

```sql
SELECT
name,
done,
error,
metadata,
response
FROM databricks_workspace.apps.app_space_operations
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>
