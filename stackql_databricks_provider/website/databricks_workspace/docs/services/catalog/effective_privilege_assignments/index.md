---
title: effective_privilege_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - effective_privilege_assignments
  - catalog
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

Creates, updates, deletes, gets or lists an <code>effective_privilege_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="effective_privilege_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.effective_privilege_assignments" /></td></tr>
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
    "name": "principal",
    "type": "string",
    "description": ""
  },
  {
    "name": "privileges",
    "type": "array",
    "description": "The privileges conveyed to the principal (either directly or via inheritance).",
    "children": [
      {
        "name": "inherited_from_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "inherited_from_type",
        "type": "string",
        "description": "The type of Unity Catalog securable. (CATALOG, CLEAN_ROOM, CONNECTION, CREDENTIAL, EXTERNAL_LOCATION, EXTERNAL_METADATA, FUNCTION, METASTORE, PIPELINE, PROVIDER, RECIPIENT, SCHEMA, SHARE, STAGING_TABLE, STORAGE_CREDENTIAL, TABLE, VOLUME)"
      },
      {
        "name": "privilege",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ACCESS, ALL_PRIVILEGES, APPLY_TAG, BROWSE, CREATE, CREATE_CASE_COLLECTION, CREATE_CATALOG, CREATE_CLEAN_ROOM, CREATE_CONNECTION, CREATE_DATASOURCE, CREATE_EXTERNAL_LOCATION, CREATE_EXTERNAL_TABLE, CREATE_EXTERNAL_VOLUME, CREATE_FEATURE, CREATE_FLOW, CREATE_FOREIGN_CATALOG, CREATE_FOREIGN_SECURABLE, CREATE_FUNCTION, CREATE_MANAGED_STORAGE, CREATE_MATERIALIZED_VIEW, CREATE_MEMORY_STORE, CREATE_MODEL, CREATE_PROVIDER, CREATE_RECIPIENT, CREATE_RULE, CREATE_SCHEMA, CREATE_SEMANTIC_GRAPH, CREATE_SERVICE, CREATE_SERVICE_CREDENTIAL, CREATE_SHARE, CREATE_SKILL, CREATE_STORAGE_CREDENTIAL, CREATE_STREAM, CREATE_TABLE, CREATE_VIEW, CREATE_VOLUME, DELETE, DELETE_EVENTS, DELETE_SECURITY_DATA, EXECUTE, EXECUTE_CLEAN_ROOM_TASK, EXTERNAL_USE_SCHEMA, INSERT, INSERT_SECURITY_DATA, MANAGE, MANAGE_ACCESS, MANAGE_ACCESS_CONTROL, MANAGE_ALLOWLIST, MANAGE_GRANTS, MODIFY, MODIFY_CLEAN_ROOM, READ_EVENTS, READ_FEATURE, READ_FILES, READ_FLOW, READ_MEMORY_STORE, READ_METADATA, READ_PRIVATE_FILES, READ_SECURITY_DATA, READ_SEMANTIC_GRAPH, READ_SKILL, READ_STREAM, READ_VOLUME, REFRESH, SELECT, SET_SHARE_PERMISSION, UPDATE, UPDATE_EVENTS, UPDATE_SECURITY_DATA, USAGE, USE_CATALOG, USE_CONNECTION, USE_MARKETPLACE_ASSETS, USE_PROVIDER, USE_RECIPIENT, USE_SCHEMA, USE_SHARE, USE_VOLUME, VIEW_ADMIN_METADATA, VIEW_METADATA, VIEW_OBJECT, WRITE_FILES, WRITE_FLOW, WRITE_MEMORY_STORE, WRITE_PRIVATE_FILES, WRITE_SEMANTIC_GRAPH, WRITE_SKILL, WRITE_VOLUME)"
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
    <td><a href="#parameter-securable_type"><code>securable_type</code></a>, <a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-principal"><code>principal</code></a></td>
    <td>Lists the effective privilege assignments for a securable. Includes inherited privileges. Paginated</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Full name of securable.</td>
</tr>
<tr id="parameter-securable_type">
    <td><CopyableCode code="securable_type" /></td>
    <td><code>string</code></td>
    <td>Type of securable.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum number of privilege assignments to return (page length). Every EffectivePrivilegeAssignment present in a single page response is guaranteed to contain all the effective privileges granted on (or inherited by) the requested Securable for the respective principal. If not set, a server-configured default is used. If set to - lesser than 0: invalid parameter error - 0: page length is set to a server configured value - lesser than 150 but greater than 0: invalid parameter error (this is to ensure that server is able to return at least one complete EffectivePrivilegeAssignment in a single page response) - greater than (or equal to) 150: page length is the minimum of this value and a server configured value</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token to go to next page based on previous query.</td>
</tr>
<tr id="parameter-principal">
    <td><CopyableCode code="principal" /></td>
    <td><code>string</code></td>
    <td>If provided, only the effective permissions for the specified principal (user or group) are returned.</td>
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

Lists the effective privilege assignments for a securable. Includes inherited privileges. Paginated

```sql
SELECT
principal,
privileges
FROM databricks_workspace.catalog.effective_privilege_assignments
WHERE securable_type = '{{ securable_type }}' -- required
AND full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND principal = '{{ principal }}'
;
```
</TabItem>
</Tabs>
