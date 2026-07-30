---
title: tools
hide_title: false
hide_table_of_contents: false
keywords:
  - tools
  - supervisoragents
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

Creates, updates, deletes, gets or lists a <code>tools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.supervisoragents.tools" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "Deprecated: Use tool_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name: supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;"
  },
  {
    "name": "tool_id",
    "type": "string",
    "description": "User specified id of the Tool."
  },
  {
    "name": "app",
    "type": "object",
    "description": "Databricks app. Supported app: custom mcp, custom agent.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "App name"
      }
    ]
  },
  {
    "name": "catalog",
    "type": "object",
    "description": "Configuration for a UC catalog asset_search scope tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Bare UC catalog name this tool is authorized to search (no ``.``)."
      }
    ]
  },
  {
    "name": "dashboard",
    "type": "object",
    "description": "Lakeview dashboard tool. Replaces the deprecated ``lakeview_dashboard`` field.",
    "children": [
      {
        "name": "dashboard_id",
        "type": "string",
        "description": "The unique identifier of the Lakeview dashboard."
      }
    ]
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this tool does (user-facing)."
  },
  {
    "name": "genie_space",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "space_id",
        "type": "string",
        "description": "The ID of the genie space."
      }
    ]
  },
  {
    "name": "knowledge_assistant",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "knowledge_assistant_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "serving_endpoint_name",
        "type": "string",
        "description": "Deprecated: use knowledge_assistant_id instead."
      }
    ]
  },
  {
    "name": "lakeview_dashboard",
    "type": "object",
    "description": "Deprecated: use ``dashboard`` instead.",
    "children": [
      {
        "name": "dashboard_id",
        "type": "string",
        "description": "The unique identifier of the Lakeview dashboard."
      }
    ]
  },
  {
    "name": "schema",
    "type": "object",
    "description": "Configuration for a UC schema asset_search scope tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full UC schema name (catalog.schema) this tool is authorized to search."
      }
    ]
  },
  {
    "name": "serving_endpoint",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "skill",
    "type": "object",
    "description": "Skill tool. Points to a folder containing skill subdirectories with SKILL.md files. Skills are discovered from the folder at runtime and loaded on demand via a read_skill tool.",
    "children": [
      {
        "name": "path",
        "type": "string",
        "description": "Absolute WSFS path to a folder containing skill subdirectories. Example: /Workspace/Users/creator@company.com/.assistant/skills"
      }
    ]
  },
  {
    "name": "supervisor_agent",
    "type": "object",
    "description": "Nested Supervisor Agent tool.",
    "children": [
      {
        "name": "supervisor_agent_id",
        "type": "string",
        "description": "The ID of the supervisor agent (tile ID)."
      }
    ]
  },
  {
    "name": "table",
    "type": "object",
    "description": "Unity Catalog table tool. Replaces the deprecated ``uc_table`` field.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full UC table name (catalog.schema.table) this tool is authorized to access."
      }
    ]
  },
  {
    "name": "tool_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "uc_connection",
    "type": "object",
    "description": "Databricks UC connection. Supported connection: external mcp server.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "uc_function",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "uc_mcp",
    "type": "object",
    "description": "UC-registered MCP service tool. The ``name`` field on UcMcpService is the three-level UC FQN (catalog.schema.mcp_service); the supervisor resolves it at request build time, calls ``tools/list`` against the AI Gateway mcp-services proxy, and dynamically registers every discovered MCP sub-tool as a separately-callable tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Three-level UC FQN of the registered MCP service (catalog.schema.mcp_service)."
      }
    ]
  },
  {
    "name": "uc_table",
    "type": "object",
    "description": "Deprecated: use ``table`` instead.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full UC table name (catalog.schema.table) this tool is authorized to access."
      }
    ]
  },
  {
    "name": "vector_search_index",
    "type": "object",
    "description": "Configuration for a Vector Search index tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full Vector Search index name (catalog.schema.index)."
      },
      {
        "name": "columns",
        "type": "array",
        "description": "Optional columns to return from the index. If unset, discovered from index schema at query time."
      }
    ]
  },
  {
    "name": "volume",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "web_search",
    "type": "object",
    "description": "Configuration for a public-web search tool. The supervisor collapses multiple web_search tools on the same agent into a single registered ``web_search`` tool at runtime."
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Deprecated: Use tool_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name: supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;"
  },
  {
    "name": "tool_id",
    "type": "string",
    "description": "User specified id of the Tool."
  },
  {
    "name": "app",
    "type": "object",
    "description": "Databricks app. Supported app: custom mcp, custom agent.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "App name"
      }
    ]
  },
  {
    "name": "catalog",
    "type": "object",
    "description": "Configuration for a UC catalog asset_search scope tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Bare UC catalog name this tool is authorized to search (no ``.``)."
      }
    ]
  },
  {
    "name": "dashboard",
    "type": "object",
    "description": "Lakeview dashboard tool. Replaces the deprecated ``lakeview_dashboard`` field.",
    "children": [
      {
        "name": "dashboard_id",
        "type": "string",
        "description": "The unique identifier of the Lakeview dashboard."
      }
    ]
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this tool does (user-facing)."
  },
  {
    "name": "genie_space",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "space_id",
        "type": "string",
        "description": "The ID of the genie space."
      }
    ]
  },
  {
    "name": "knowledge_assistant",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "knowledge_assistant_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "serving_endpoint_name",
        "type": "string",
        "description": "Deprecated: use knowledge_assistant_id instead."
      }
    ]
  },
  {
    "name": "lakeview_dashboard",
    "type": "object",
    "description": "Deprecated: use ``dashboard`` instead.",
    "children": [
      {
        "name": "dashboard_id",
        "type": "string",
        "description": "The unique identifier of the Lakeview dashboard."
      }
    ]
  },
  {
    "name": "schema",
    "type": "object",
    "description": "Configuration for a UC schema asset_search scope tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full UC schema name (catalog.schema) this tool is authorized to search."
      }
    ]
  },
  {
    "name": "serving_endpoint",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "skill",
    "type": "object",
    "description": "Skill tool. Points to a folder containing skill subdirectories with SKILL.md files. Skills are discovered from the folder at runtime and loaded on demand via a read_skill tool.",
    "children": [
      {
        "name": "path",
        "type": "string",
        "description": "Absolute WSFS path to a folder containing skill subdirectories. Example: /Workspace/Users/creator@company.com/.assistant/skills"
      }
    ]
  },
  {
    "name": "supervisor_agent",
    "type": "object",
    "description": "Nested Supervisor Agent tool.",
    "children": [
      {
        "name": "supervisor_agent_id",
        "type": "string",
        "description": "The ID of the supervisor agent (tile ID)."
      }
    ]
  },
  {
    "name": "table",
    "type": "object",
    "description": "Unity Catalog table tool. Replaces the deprecated ``uc_table`` field.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full UC table name (catalog.schema.table) this tool is authorized to access."
      }
    ]
  },
  {
    "name": "tool_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "uc_connection",
    "type": "object",
    "description": "Databricks UC connection. Supported connection: external mcp server.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "uc_function",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "uc_mcp",
    "type": "object",
    "description": "UC-registered MCP service tool. The ``name`` field on UcMcpService is the three-level UC FQN (catalog.schema.mcp_service); the supervisor resolves it at request build time, calls ``tools/list`` against the AI Gateway mcp-services proxy, and dynamically registers every discovered MCP sub-tool as a separately-callable tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Three-level UC FQN of the registered MCP service (catalog.schema.mcp_service)."
      }
    ]
  },
  {
    "name": "uc_table",
    "type": "object",
    "description": "Deprecated: use ``table`` instead.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full UC table name (catalog.schema.table) this tool is authorized to access."
      }
    ]
  },
  {
    "name": "vector_search_index",
    "type": "object",
    "description": "Configuration for a Vector Search index tool.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Full Vector Search index name (catalog.schema.index)."
      },
      {
        "name": "columns",
        "type": "array",
        "description": "Optional columns to return from the index. If unset, discovered from index schema at query time."
      }
    ]
  },
  {
    "name": "volume",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "web_search",
    "type": "object",
    "description": "Configuration for a public-web search tool. The supervisor collapses multiple web_search tools on the same agent into a single registered ``web_search`` tool at runtime."
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
    <td>Lists Tools under a Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a Tool.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-tool_id"><code>tool_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-tool"><code>tool</code></a></td>
    <td></td>
    <td>Creates a Tool under a Supervisor Agent. Specify one of "genie_space", "knowledge_assistant",</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-tool"><code>tool</code></a></td>
    <td></td>
    <td>Updates a Tool. Only the ``description`` field can be updated. To change immutable fields such as tool</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a Tool.</td>
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
    <td>The resource name of the Tool. Format: supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Parent resource where this tool will be created. Format: supervisor-agents/&#123;supervisor_agent_id&#125;</td>
</tr>
<tr id="parameter-tool_id">
    <td><CopyableCode code="tool_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the tool, which will become the final component of the tool's resource name.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Field mask for fields to be updated.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
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

Lists Tools under a Supervisor Agent.

```sql
SELECT
id,
name,
tool_id,
app,
catalog,
dashboard,
description,
genie_space,
knowledge_assistant,
lakeview_dashboard,
schema,
serving_endpoint,
skill,
supervisor_agent,
table,
tool_type,
uc_connection,
uc_function,
uc_mcp,
uc_table,
vector_search_index,
volume,
web_search
FROM databricks_workspace.supervisoragents.tools
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Gets a Tool.

```sql
SELECT
id,
name,
tool_id,
app,
catalog,
dashboard,
description,
genie_space,
knowledge_assistant,
lakeview_dashboard,
schema,
serving_endpoint,
skill,
supervisor_agent,
table,
tool_type,
uc_connection,
uc_function,
uc_mcp,
uc_table,
vector_search_index,
volume,
web_search
FROM databricks_workspace.supervisoragents.tools
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

Creates a Tool under a Supervisor Agent. Specify one of "genie_space", "knowledge_assistant",

```sql
INSERT INTO databricks_workspace.supervisoragents.tools (
tool,
parent,
tool_id,
deployment_name
)
SELECT 
'{{ tool }}' /* required */,
'{{ parent }}',
'{{ tool_id }}',
'{{ deployment_name }}'
RETURNING
id,
name,
tool_id,
app,
catalog,
dashboard,
description,
genie_space,
knowledge_assistant,
lakeview_dashboard,
schema,
serving_endpoint,
skill,
supervisor_agent,
table,
tool_type,
uc_connection,
uc_function,
uc_mcp,
uc_table,
vector_search_index,
volume,
web_search
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tools
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the tools resource.
    - name: tool_id
      value: "{{ tool_id }}"
      description: Required parameter for the tools resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the tools resource.
    - name: tool
      value:
        tool_type: "{{ tool_type }}"
        app:
          name: "{{ name }}"
        catalog:
          name: "{{ name }}"
        dashboard:
          dashboard_id: "{{ dashboard_id }}"
        description: "{{ description }}"
        genie_space:
          id: "{{ id }}"
          space_id: "{{ space_id }}"
        id: "{{ id }}"
        knowledge_assistant:
          knowledge_assistant_id: "{{ knowledge_assistant_id }}"
          serving_endpoint_name: "{{ serving_endpoint_name }}"
        lakeview_dashboard:
          dashboard_id: "{{ dashboard_id }}"
        name: "{{ name }}"
        schema:
          name: "{{ name }}"
        serving_endpoint:
          name: "{{ name }}"
        skill:
          path: "{{ path }}"
        supervisor_agent:
          supervisor_agent_id: "{{ supervisor_agent_id }}"
        table:
          name: "{{ name }}"
        tool_id: "{{ tool_id }}"
        uc_connection:
          name: "{{ name }}"
        uc_function:
          name: "{{ name }}"
        uc_mcp:
          name: "{{ name }}"
        uc_table:
          name: "{{ name }}"
        vector_search_index:
          name: "{{ name }}"
          columns:
            - "{{ columns }}"
        volume:
          name: "{{ name }}"
        web_search: "{{ web_search }}"
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

Updates a Tool. Only the ``description`` field can be updated. To change immutable fields such as tool

```sql
UPDATE databricks_workspace.supervisoragents.tools
SET 
tool = '{{ tool }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND tool = '{{ tool }}' --required
RETURNING
id,
name,
tool_id,
app,
catalog,
dashboard,
description,
genie_space,
knowledge_assistant,
lakeview_dashboard,
schema,
serving_endpoint,
skill,
supervisor_agent,
table,
tool_type,
uc_connection,
uc_function,
uc_mcp,
uc_table,
vector_search_index,
volume,
web_search;
```
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

Deletes a Tool.

```sql
DELETE FROM databricks_workspace.supervisoragents.tools
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
