---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
  - aisearch
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

Creates, updates, deletes, gets or lists an <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indexes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.aisearch.indexes" /></td></tr>
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
    "description": "Name of the AI Search index. Server-assigned full resource path (``workspaces/&#123;workspace&#125;/endpoints/&#123;endpoint&#125;/indexes/&#123;index&#125;``) on output, where ``&#123;index&#125;`` is the index's Unity Catalog table name. On create, the user-supplied UC table name is conveyed via ``CreateIndexRequest.index_id``; the server composes the full ``name`` and returns it on the response."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "Creator of the index."
  },
  {
    "name": "delta_sync_index_spec",
    "type": "object",
    "description": "Specification for a Delta Sync index. Set when ``index_type`` is ``DELTA_SYNC``.",
    "children": [
      {
        "name": "pipeline_type",
        "type": "string",
        "description": "Pipeline execution mode. Required on create — the backend rejects an unset value. Storage Optimized endpoints accept only ``TRIGGERED``; Standard endpoints accept both. No explicit ``stage`` — a REQUIRED field staged below its service would be dropped from combined specs while remaining in ``required``, tripping the OpenAPI required-vs-properties consistency check. The field inherits the service's launch stage. (CONTINUOUS, TRIGGERED)"
      },
      {
        "name": "columns_to_sync",
        "type": "array",
        "description": "[Optional] Select the columns to sync with the index. If left blank, all columns from the source table are synced. The primary key column and embedding source or vector column are always synced."
      },
      {
        "name": "embedding_source_columns",
        "type": "array",
        "description": "The columns that contain the embedding source.",
        "children": [
          {
            "name": "embedding_model_endpoint",
            "type": "string",
            "description": "Name of the embedding model endpoint, used by default for both ingestion and querying."
          },
          {
            "name": "model_endpoint_name_for_query",
            "type": "string",
            "description": "Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the source column."
          }
        ]
      },
      {
        "name": "embedding_vector_columns",
        "type": "array",
        "description": "The columns that contain the embedding vectors.",
        "children": [
          {
            "name": "embedding_dimension",
            "type": "integer",
            "description": "Dimension of the embedding vector."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column."
          }
        ]
      },
      {
        "name": "embedding_writeback_table",
        "type": "string",
        "description": "[Optional] Name of the Delta table to sync the index contents and computed embeddings to."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "The ID of the pipeline that is used to sync the index."
      },
      {
        "name": "source_table",
        "type": "string",
        "description": "The full name of the source Delta table."
      }
    ]
  },
  {
    "name": "direct_access_index_spec",
    "type": "object",
    "description": "Specification for a Direct Access index. Set when ``index_type`` is ``DIRECT_ACCESS``.",
    "children": [
      {
        "name": "embedding_source_columns",
        "type": "array",
        "description": "The columns that contain the embedding source.",
        "children": [
          {
            "name": "embedding_model_endpoint",
            "type": "string",
            "description": "Name of the embedding model endpoint, used by default for both ingestion and querying."
          },
          {
            "name": "model_endpoint_name_for_query",
            "type": "string",
            "description": "Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the source column."
          }
        ]
      },
      {
        "name": "embedding_vector_columns",
        "type": "array",
        "description": "The columns that contain the embedding vectors.",
        "children": [
          {
            "name": "embedding_dimension",
            "type": "integer",
            "description": "Dimension of the embedding vector."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column."
          }
        ]
      },
      {
        "name": "requested_schema_json",
        "type": "string",
        "description": "The index schema exactly as the user supplied it on create, preserving the original type spellings (e.g. ``integer``) rather than Unity Catalog's canonical names (e.g. ``int``) that ``schema_json`` returns."
      },
      {
        "name": "schema_json",
        "type": "string",
        "description": "The schema of the index in JSON format. Supported types are ``integer``, ``long``, ``float``, ``double``, ``boolean``, ``string``, ``date``, ``timestamp``. Supported types for vector columns: ``array&lt;float&gt;``, ``array&lt;double&gt;``."
      }
    ]
  },
  {
    "name": "endpoint",
    "type": "string",
    "description": "Name of the endpoint associated with the index. Ignored on create — the endpoint is taken from ``CreateIndexRequest.parent``; populated only on output."
  },
  {
    "name": "index_subtype",
    "type": "string",
    "description": "The subtype of the index. Set on create and immutable thereafter. (FULL_TEXT, HYBRID, VECTOR)"
  },
  {
    "name": "index_type",
    "type": "string",
    "description": "Type of index. Required on create and immutable thereafter. (DELTA_SYNC, DIRECT_ACCESS)"
  },
  {
    "name": "primary_key",
    "type": "string",
    "description": "Primary key of the index. Set on create and immutable thereafter."
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current status of the index.",
    "children": [
      {
        "name": "index_url",
        "type": "string",
        "description": "Index API URL used to perform operations on the index."
      },
      {
        "name": "indexed_row_count",
        "type": "integer",
        "description": "Number of rows indexed."
      },
      {
        "name": "message",
        "type": "string",
        "description": "Human-readable detail about the index's current state."
      },
      {
        "name": "ready",
        "type": "boolean",
        "description": "Whether the index is ready for search."
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
    "description": "Name of the AI Search index. Server-assigned full resource path (``workspaces/&#123;workspace&#125;/endpoints/&#123;endpoint&#125;/indexes/&#123;index&#125;``) on output, where ``&#123;index&#125;`` is the index's Unity Catalog table name. On create, the user-supplied UC table name is conveyed via ``CreateIndexRequest.index_id``; the server composes the full ``name`` and returns it on the response."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "Creator of the index."
  },
  {
    "name": "delta_sync_index_spec",
    "type": "object",
    "description": "Specification for a Delta Sync index. Set when ``index_type`` is ``DELTA_SYNC``.",
    "children": [
      {
        "name": "pipeline_type",
        "type": "string",
        "description": "Pipeline execution mode. Required on create — the backend rejects an unset value. Storage Optimized endpoints accept only ``TRIGGERED``; Standard endpoints accept both. No explicit ``stage`` — a REQUIRED field staged below its service would be dropped from combined specs while remaining in ``required``, tripping the OpenAPI required-vs-properties consistency check. The field inherits the service's launch stage. (CONTINUOUS, TRIGGERED)"
      },
      {
        "name": "columns_to_sync",
        "type": "array",
        "description": "[Optional] Select the columns to sync with the index. If left blank, all columns from the source table are synced. The primary key column and embedding source or vector column are always synced."
      },
      {
        "name": "embedding_source_columns",
        "type": "array",
        "description": "The columns that contain the embedding source.",
        "children": [
          {
            "name": "embedding_model_endpoint",
            "type": "string",
            "description": "Name of the embedding model endpoint, used by default for both ingestion and querying."
          },
          {
            "name": "model_endpoint_name_for_query",
            "type": "string",
            "description": "Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the source column."
          }
        ]
      },
      {
        "name": "embedding_vector_columns",
        "type": "array",
        "description": "The columns that contain the embedding vectors.",
        "children": [
          {
            "name": "embedding_dimension",
            "type": "integer",
            "description": "Dimension of the embedding vector."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column."
          }
        ]
      },
      {
        "name": "embedding_writeback_table",
        "type": "string",
        "description": "[Optional] Name of the Delta table to sync the index contents and computed embeddings to."
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "The ID of the pipeline that is used to sync the index."
      },
      {
        "name": "source_table",
        "type": "string",
        "description": "The full name of the source Delta table."
      }
    ]
  },
  {
    "name": "direct_access_index_spec",
    "type": "object",
    "description": "Specification for a Direct Access index. Set when ``index_type`` is ``DIRECT_ACCESS``.",
    "children": [
      {
        "name": "embedding_source_columns",
        "type": "array",
        "description": "The columns that contain the embedding source.",
        "children": [
          {
            "name": "embedding_model_endpoint",
            "type": "string",
            "description": "Name of the embedding model endpoint, used by default for both ingestion and querying."
          },
          {
            "name": "model_endpoint_name_for_query",
            "type": "string",
            "description": "Name of the embedding model endpoint which, if specified, is used for querying (not ingestion)."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the source column."
          }
        ]
      },
      {
        "name": "embedding_vector_columns",
        "type": "array",
        "description": "The columns that contain the embedding vectors.",
        "children": [
          {
            "name": "embedding_dimension",
            "type": "integer",
            "description": "Dimension of the embedding vector."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the column."
          }
        ]
      },
      {
        "name": "requested_schema_json",
        "type": "string",
        "description": "The index schema exactly as the user supplied it on create, preserving the original type spellings (e.g. ``integer``) rather than Unity Catalog's canonical names (e.g. ``int``) that ``schema_json`` returns."
      },
      {
        "name": "schema_json",
        "type": "string",
        "description": "The schema of the index in JSON format. Supported types are ``integer``, ``long``, ``float``, ``double``, ``boolean``, ``string``, ``date``, ``timestamp``. Supported types for vector columns: ``array&lt;float&gt;``, ``array&lt;double&gt;``."
      }
    ]
  },
  {
    "name": "endpoint",
    "type": "string",
    "description": "Name of the endpoint associated with the index. Ignored on create — the endpoint is taken from ``CreateIndexRequest.parent``; populated only on output."
  },
  {
    "name": "index_subtype",
    "type": "string",
    "description": "The subtype of the index. Set on create and immutable thereafter. (FULL_TEXT, HYBRID, VECTOR)"
  },
  {
    "name": "index_type",
    "type": "string",
    "description": "Type of index. Required on create and immutable thereafter. (DELTA_SYNC, DIRECT_ACCESS)"
  },
  {
    "name": "primary_key",
    "type": "string",
    "description": "Primary key of the index. Set on create and immutable thereafter."
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current status of the index.",
    "children": [
      {
        "name": "index_url",
        "type": "string",
        "description": "Index API URL used to perform operations on the index."
      },
      {
        "name": "indexed_row_count",
        "type": "integer",
        "description": "Number of rows indexed."
      },
      {
        "name": "message",
        "type": "string",
        "description": "Human-readable detail about the index's current state."
      },
      {
        "name": "ready",
        "type": "boolean",
        "description": "Whether the index is ready for search."
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
    <td><a href="#parameter-debug_level"><code>debug_level</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List AI Search indexes on an endpoint.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get details for a single AI Search index.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-index"><code>index</code></a></td>
    <td><a href="#parameter-index_id"><code>index_id</code></a></td>
    <td>Create a new AI Search index.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete an AI Search index.</td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-columns"><code>columns</code></a></td>
    <td></td>
    <td>Query (search) an AI Search index. Read-only, so a read-scoped token may invoke it.</td>
</tr>
<tr>
    <td><a href="#remove_data"><CopyableCode code="remove_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-primary_keys"><code>primary_keys</code></a></td>
    <td></td>
    <td>Remove rows by primary key from a Direct Access AI Search index.</td>
</tr>
<tr>
    <td><a href="#scan"><CopyableCode code="scan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Scan (paginate over) the rows of an AI Search index.</td>
</tr>
<tr>
    <td><a href="#sync"><CopyableCode code="sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Synchronize a Delta Sync AI Search index with its source Delta table. Applies only to Delta Sync</td>
</tr>
<tr>
    <td><a href="#upsert_data"><CopyableCode code="upsert_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-inputs_json"><code>inputs_json</code></a></td>
    <td></td>
    <td>Upsert rows into a Direct Access AI Search index.</td>
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
    <td>Full resource name of the index. Must be a Direct Access index. Format: ``workspaces/&#123;workspace_id&#125;/endpoints/&#123;endpoint_id&#125;/indexes/&#123;index_id&#125;``</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>The Endpoint where this Index will be created. Format: ``workspaces/&#123;workspace_id&#125;/endpoints/&#123;endpoint_id&#125;``</td>
</tr>
<tr id="parameter-debug_level">
    <td><CopyableCode code="debug_level" /></td>
    <td><code>integer</code></td>
    <td>Opt-in debug level. When set to 1 or higher, the backend computes per-index routing eligibility and populates ``can_use_optimized_route`` on each returned index. When unset (0), that field is left unpopulated and the eligibility computation is skipped. Matches the ``debug_level`` convention on the query path.</td>
</tr>
<tr id="parameter-index_id">
    <td><CopyableCode code="index_id" /></td>
    <td><code>string</code></td>
    <td>The user-supplied Unity Catalog table name for the Index, per AIP-133. The server composes the full ``Index.name`` as ``&#123;parent&#125;/indexes/&#123;index_id&#125;``. AIP-133 does not list ``index_id`` as a fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects empty values with INVALID_PARAMETER_VALUE.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Best-effort upper bound on the number of results to return. Honored as an upper bound by the shim: ``page_size`` only narrows the legacy backend's response, never widens it, so the practical cap is ``min(page_size, legacy_fixed_page_size)``.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
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

List AI Search indexes on an endpoint.

```sql
SELECT
name,
creator,
delta_sync_index_spec,
direct_access_index_spec,
endpoint,
index_subtype,
index_type,
primary_key,
status
FROM databricks_workspace.aisearch.indexes
WHERE parent = '{{ parent }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND debug_level = '{{ debug_level }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="get">

Get details for a single AI Search index.

```sql
SELECT
name,
creator,
delta_sync_index_spec,
direct_access_index_spec,
endpoint,
index_subtype,
index_type,
primary_key,
status
FROM databricks_workspace.aisearch.indexes
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

Create a new AI Search index.

```sql
INSERT INTO databricks_workspace.aisearch.indexes (
index,
parent,
deployment_name,
index_id
)
SELECT 
'{{ index }}' /* required */,
'{{ parent }}',
'{{ deployment_name }}',
'{{ index_id }}'
RETURNING
name,
creator,
delta_sync_index_spec,
direct_access_index_spec,
endpoint,
index_subtype,
index_type,
primary_key,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: indexes
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the indexes resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the indexes resource.
    - name: index
      description: |
        The Index resource to create. Fields other than \`\`index.name\`\` carry the desired configuration; \`\`index.name\`\` is server-assigned from \`\`parent\`\` and \`\`index_id\`\`.
      value:
        primary_key: "{{ primary_key }}"
        index_type: "{{ index_type }}"
        creator: "{{ creator }}"
        delta_sync_index_spec:
          pipeline_type: "{{ pipeline_type }}"
          columns_to_sync:
            - "{{ columns_to_sync }}"
          embedding_source_columns:
            - embedding_model_endpoint: "{{ embedding_model_endpoint }}"
              model_endpoint_name_for_query: "{{ model_endpoint_name_for_query }}"
              name: "{{ name }}"
          embedding_vector_columns:
            - embedding_dimension: {{ embedding_dimension }}
              name: "{{ name }}"
          embedding_writeback_table: "{{ embedding_writeback_table }}"
          pipeline_id: "{{ pipeline_id }}"
          source_table: "{{ source_table }}"
        direct_access_index_spec:
          embedding_source_columns:
            - embedding_model_endpoint: "{{ embedding_model_endpoint }}"
              model_endpoint_name_for_query: "{{ model_endpoint_name_for_query }}"
              name: "{{ name }}"
          embedding_vector_columns:
            - embedding_dimension: {{ embedding_dimension }}
              name: "{{ name }}"
          requested_schema_json: "{{ requested_schema_json }}"
          schema_json: "{{ schema_json }}"
        endpoint: "{{ endpoint }}"
        index_subtype: "{{ index_subtype }}"
        name: "{{ name }}"
        status:
          index_url: "{{ index_url }}"
          indexed_row_count: {{ indexed_row_count }}
          message: "{{ message }}"
          ready: {{ ready }}
    - name: index_id
      value: "{{ index_id }}"
      description: The user-supplied Unity Catalog table name for the Index, per AIP-133. The server composes the full \`\`Index.name\`\` as \`\`{parent}/indexes/{index_id}\`\`. AIP-133 does not list \`\`index_id\`\` as a fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects empty values with INVALID_PARAMETER_VALUE.
      description: The user-supplied Unity Catalog table name for the Index, per AIP-133. The server composes the full \`\`Index.name\`\` as \`\`{parent}/indexes/{index_id}\`\`. AIP-133 does not list \`\`index_id\`\` as a fields-may-be-required entry, so we annotate it OPTIONAL on the wire; the server still rejects empty values with INVALID_PARAMETER_VALUE.
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

Delete an AI Search index.

```sql
DELETE FROM databricks_workspace.aisearch.indexes
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="query"
    values={[
        { label: 'query', value: 'query' },
        { label: 'remove_data', value: 'remove_data' },
        { label: 'scan', value: 'scan' },
        { label: 'sync', value: 'sync' },
        { label: 'upsert_data', value: 'upsert_data' }
    ]}
>
<TabItem value="query">

Query (search) an AI Search index. Read-only, so a read-scoped token may invoke it.

```sql
EXEC databricks_workspace.aisearch.indexes.query 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"columns": "{{ columns }}", 
"columns_to_rerank": "{{ columns_to_rerank }}", 
"facets": "{{ facets }}", 
"filters_json": "{{ filters_json }}", 
"max_results": {{ max_results }}, 
"query_columns": "{{ query_columns }}", 
"query_text": "{{ query_text }}", 
"query_type": "{{ query_type }}", 
"query_vector": "{{ query_vector }}", 
"reranker": "{{ reranker }}", 
"score_threshold": {{ score_threshold }}, 
"sort_columns": "{{ sort_columns }}"
}'
;
```
</TabItem>
<TabItem value="remove_data">

Remove rows by primary key from a Direct Access AI Search index.

```sql
EXEC databricks_workspace.aisearch.indexes.remove_data 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"primary_keys": "{{ primary_keys }}"
}'
;
```
</TabItem>
<TabItem value="scan">

Scan (paginate over) the rows of an AI Search index.

```sql
EXEC databricks_workspace.aisearch.indexes.scan 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"page_size": {{ page_size }}, 
"page_token": "{{ page_token }}"
}'
;
```
</TabItem>
<TabItem value="sync">

Synchronize a Delta Sync AI Search index with its source Delta table. Applies only to Delta Sync

```sql
EXEC databricks_workspace.aisearch.indexes.sync 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="upsert_data">

Upsert rows into a Direct Access AI Search index.

```sql
EXEC databricks_workspace.aisearch.indexes.upsert_data 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"inputs_json": "{{ inputs_json }}"
}'
;
```
</TabItem>
</Tabs>
