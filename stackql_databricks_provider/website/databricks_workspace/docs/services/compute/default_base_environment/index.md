---
title: default_base_environment
hide_title: false
hide_table_of_contents: false
keywords:
  - default_base_environment
  - compute
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

Creates, updates, deletes, gets or lists a <code>default_base_environment</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="default_base_environment" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.default_base_environment" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "creator_user_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "last_updated_user_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "base_environment_cache",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "indefinite_materialized_environment",
        "type": "object",
        "description": "Materialized Environment information enables environment sharing and reuse via Environment<br />    Caching during library installations. Currently this feature is only supported for Python<br />    libraries.<br /><br />    - If the env cache entry in LMv2 DB doesn't exist or invalid, library installations and<br />      environment materialization will occur. A new Materialized Environment metadata will be sent<br />      from DP upon successful library installations and env materialization, and is persisted into<br />      database by LMv2.<br />    - If the env cache entry in LMv2 DB is valid, the Materialized Environment will be sent to DP by<br />      LMv2, and DP will restore the cached environment from a store instead of reinstalling<br />      libraries from scratch.<br /><br />    If changed, also update estore/namespaces/defaultbaseenvironments/latest.proto with new version<br />    If changed, also update estore/namespaces/envspecenvironments/latest.proto with new version",
        "children": [
          {
            "name": "last_updated_timestamp",
            "type": "integer",
            "description": "The timestamp (in epoch milliseconds) when the materialized env is updated."
          }
        ]
      },
      {
        "name": "materialized_environment",
        "type": "object",
        "description": "Materialized Environment information enables environment sharing and reuse via Environment<br />    Caching during library installations. Currently this feature is only supported for Python<br />    libraries.<br /><br />    - If the env cache entry in LMv2 DB doesn't exist or invalid, library installations and<br />      environment materialization will occur. A new Materialized Environment metadata will be sent<br />      from DP upon successful library installations and env materialization, and is persisted into<br />      database by LMv2.<br />    - If the env cache entry in LMv2 DB is valid, the Materialized Environment will be sent to DP by<br />      LMv2, and DP will restore the cached environment from a store instead of reinstalling<br />      libraries from scratch.<br /><br />    If changed, also update estore/namespaces/defaultbaseenvironments/latest.proto with new version<br />    If changed, also update estore/namespaces/envspecenvironments/latest.proto with new version",
        "children": [
          {
            "name": "last_updated_timestamp",
            "type": "integer",
            "description": "The timestamp (in epoch milliseconds) when the materialized env is updated."
          }
        ]
      },
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "status",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CREATED, EXPIRED, FAILED, INVALID, PENDING, REFRESHING)"
      }
    ]
  },
  {
    "name": "base_environment_type",
    "type": "string",
    "description": "If changed, also update estore/namespaces/defaultbaseenvironments/latest.proto (CPU, GPU)"
  },
  {
    "name": "created_timestamp",
    "type": "integer",
    "description": ""
  },
  {
    "name": "environment",
    "type": "object",
    "description": "Note: we made ``environment`` non-internal because we need to expose its ``client`` field. All other fields should be treated as internal.",
    "children": [
      {
        "name": "base_environment",
        "type": "string",
        "description": "The base environment this environment is built on top of. A base environment defines the environment version and a list of dependencies for serverless compute. The value can be a file path to a custom ``env.yaml`` file (e.g., ``/Workspace/path/to/env.yaml``). Support for a Databricks-provided base environment ID (e.g., ``workspace-base-environments/databricks_ai_v4``) and workspace base environment ID (e.g., ``workspace-base-environments/dbe_b849b66e-b31a-4cb5-b161-1f2b10877fb7``) is in Beta. Either ``environment_version`` or ``base_environment`` can be provided. For more information about Databricks-provided base environments, see the [list workspace base environments](:method:Environments/ListWorkspaceBaseEnvironments) API. For more information, see"
      },
      {
        "name": "client",
        "type": "string",
        "description": "Use ``environment_version`` instead."
      },
      {
        "name": "dependencies",
        "type": "array",
        "description": "List of pip dependencies, as supported by the version of pip in this environment. Each dependency is a valid pip requirements file line per https://pip.pypa.io/en/stable/reference/requirements-file-format/. Allowed dependencies include a requirement specifier, an archive URL, a local project path (such as WSFS or UC Volumes in Databricks), or a VCS project URL."
      },
      {
        "name": "environment_version",
        "type": "string",
        "description": "Either ``environment_version`` or ``base_environment`` needs to be provided. Environment version used by the environment. Each version comes with a specific Python version and a set of Python packages. The version is a string, consisting of an integer."
      },
      {
        "name": "java_dependencies",
        "type": "array",
        "description": "List of java dependencies. Each dependency is a string representing a java library path. For example: ``/Volumes/path/to/test.jar``."
      }
    ]
  },
  {
    "name": "filepath",
    "type": "string",
    "description": ""
  },
  {
    "name": "is_default",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": ""
  },
  {
    "name": "message",
    "type": "string",
    "description": ""
  },
  {
    "name": "principal_ids",
    "type": "array",
    "description": ""
  },
  {
    "name": "status",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CREATED, EXPIRED, FAILED, INVALID, PENDING, REFRESHING)"
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-trace_id"><code>trace_id</code></a></td>
    <td>Return the default base environment details for a given ID.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-trace_id">
    <td><CopyableCode code="trace_id" /></td>
    <td><code>string</code></td>
    <td>Deprecated: use ctx.requestId instead</td>
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

Return the default base environment details for a given ID.

```sql
SELECT
id,
name,
creator_user_id,
last_updated_user_id,
base_environment_cache,
base_environment_type,
created_timestamp,
environment,
filepath,
is_default,
last_updated_timestamp,
message,
principal_ids,
status
FROM databricks_workspace.compute.default_base_environment
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND trace_id = '{{ trace_id }}'
;
```
</TabItem>
</Tabs>
