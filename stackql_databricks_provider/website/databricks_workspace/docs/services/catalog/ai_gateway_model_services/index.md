---
title: ai_gateway_model_services
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_model_services
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

Creates, updates, deletes, gets or lists an <code>ai_gateway_model_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_model_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_model_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name of the model service. Format: ``model-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``model_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the model service."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Whether the caller sees only metadata available through the BROWSE privilege."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Operational configuration: destinations, routing, rate limits, inference table. Required on CreateModelService; on UpdateModelService it is required only when ``config`` (or a ``config.*`` subpath) appears in ``update_mask``.",
    "children": [
      {
        "name": "inference_table",
        "type": "object",
        "description": "Inference table config for payload logging.",
        "children": [
          {
            "name": "parent",
            "type": "string",
            "description": "Parent UC schema where the inference table is created. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Set at create time and immutable thereafter; changing it on an existing service is rejected."
          },
          {
            "name": "disabled",
            "type": "boolean",
            "description": "Indicates whether payload logging is disabled (opt-out). Unset means that payload logging is active (the on-by-default state coincides with the proto zero-value, so the server never fills this field for a client that leaves it unset). Set ``disabled = true`` to pause runtime logging while keeping the sub-message attached (preserving ``parent`` and ``table_name_prefix`` for a later flip back to active). ``parent`` remains required either way."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "True when the bound inference TABLE has been deleted but the parent service still references it. The dangling reference is surfaced (not silently dropped) so callers can see the broken dependency. AI Gateway payload logging fails closed in this state."
          },
          {
            "name": "table",
            "type": "string",
            "description": "Resolved UC table for payload logs. Format: ``tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;``."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix for the inference-table's UC-registered name. The actual leaf name UC stores is ``&lt;table_name_prefix&gt;_payload``; the ``_payload`` suffix is appended automatically. To find the actual UC table after Create, read the ``table`` field on the response. Defaults to ``&lt;model_service_name&gt;_payload`` when unset. Set at create time and immutable thereafter; changing it on an existing service is rejected."
          }
        ]
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits applied to requests routed through this model service.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": "Scope key. Determines whether ``principal`` is required. (RATE_LIMIT_KEY_REQUEST_TAG, RATE_LIMIT_KEY_SERVICE, RATE_LIMIT_KEY_SERVICE_PRINCIPAL, RATE_LIMIT_KEY_USER, RATE_LIMIT_KEY_USER_DEFAULT, RATE_LIMIT_KEY_USER_GROUP)"
          },
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Renewal period. (RATE_LIMIT_RENEWAL_PERIOD_HOUR, RATE_LIMIT_RENEWAL_PERIOD_MINUTE)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal this limit applies to: user email, group name, or service principal application ID. Required unless ``key`` is ``RATE_LIMIT_KEY_SERVICE``, ``RATE_LIMIT_KEY_USER_DEFAULT``, or ``RATE_LIMIT_KEY_REQUEST_TAG`` (which must not set a principal)."
          },
          {
            "name": "request_tag_key",
            "type": "string",
            "description": "Request tag key this limit applies to. Required when ``key`` is ``RATE_LIMIT_KEY_REQUEST_TAG``, forbidden otherwise."
          },
          {
            "name": "request_tag_value",
            "type": "string",
            "description": "Request tag value this limit applies to. Only valid when ``key`` is ``RATE_LIMIT_KEY_REQUEST_TAG``. Leave unset to apply the limit to every value of ``request_tag_key`` (an any-value default); a set value is a specific override for that value."
          },
          {
            "name": "requests",
            "type": "integer",
            "description": "Max requests allowed within a renewal period. Leave unset for no request limit."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Max tokens allowed within a renewal period. Leave unset for no token limit."
          }
        ]
      },
      {
        "name": "routing",
        "type": "object",
        "description": "Routing configuration: destinations, routing strategy, and fallback.",
        "children": [
          {
            "name": "destinations",
            "type": "array",
            "description": "Primary routing destinations. At most 10 are allowed. At least one is required on CreateModelService; on UpdateModelService it is required only when ``config.routing`` (or a ``config.routing.*`` subpath) appears in ``update_mask``.",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": "User-facing label for this destination, used in routing references."
              },
              {
                "name": "destination_type",
                "type": "string",
                "description": "Backing-model category. Determines which oneof variant is populated. (DESTINATION_TYPE_EXTERNAL_FOUNDATION_MODEL, DESTINATION_TYPE_PAY_PER_TOKEN_FOUNDATION_MODEL, DESTINATION_TYPE_PROVISIONED_THROUGHPUT_FOUNDATION_MODEL)"
              },
              {
                "name": "external_model_config",
                "type": "object",
                "description": "Configuration for an external-foundation-model destination. Provider auth and provider-specific<br />    cloud configuration are owned by a separate, governed ModelProviderService entity referenced via<br />    ``model_provider_service``; the platform resolves the provider at invocation time."
              },
              {
                "name": "is_deleted",
                "type": "boolean",
                "description": "True when the destination's backing UC entity (MODEL for foundation-model destinations, MODEL_PROVIDER_SERVICE for external destinations) has been deleted but the destination row still references it. The dangling destination is surfaced (not silently dropped) so callers can see the broken routing. Inference traffic through this destination fails closed (BAD_REQUEST / FAILED_PRECONDITION)."
              },
              {
                "name": "pay_per_token_config",
                "type": "object",
                "description": "Configuration for a pay-per-token foundation-model destination. Identifies the foundation model<br />    by its UC resource name; the platform resolves it to a Model Serving endpoint at request time."
              },
              {
                "name": "provisioned_throughput_config",
                "type": "object",
                "description": "Configuration for a provisioned-throughput foundation-model destination. References a<br />    pre-existing Model Serving endpoint that serves the model; sizing (provisioned throughput, burst<br />    scaling, model version) is owned by the Model Serving endpoint itself, not by this message."
              },
              {
                "name": "traffic_percentage",
                "type": "integer",
                "description": "Share of traffic sent to this destination, 0-100. Optional on fallback destinations; see FallbackConfig."
              }
            ]
          },
          {
            "name": "fallback",
            "type": "object",
            "description": "Fallback routing config, applied after primary destinations fail.",
            "children": [
              {
                "name": "destinations",
                "type": "array",
                "description": "Ordered list of fallback destinations. Traversal is in list order; the attempt count is the length of the list. At most 5 are allowed."
              }
            ]
          },
          {
            "name": "first_token_timeout",
            "type": "string",
            "description": "Timeout for the first token of a streaming response. If a destination does not return its first token within this duration, AI Gateway aborts the attempt and fails over to the next destination. Applies to streaming requests only. Leave unset for no first-token timeout."
          },
          {
            "name": "traffic_splitting",
            "type": "object",
            "description": "Marker message selecting request-based traffic splitting. Traffic is distributed according to each destination's traffic_percentage value; no configuration lives on this message itself."
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the model service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "The resolved owner of the ModelService. Falls back to the caller's identity when ``owner`` is not explicitly set on creation."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency control token. Server-generated from the entity's state and returned on every read. To use it as an if-match precondition on a mutation, echo the last-read value back via the dedicated ``etag`` field on the Update / Delete request; the server rejects the mutation if the stored etag differs."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the model service. Write-only; read owner via effective_owner."
  },
  {
    "name": "supported_api_types",
    "type": "array",
    "description": "Unified API types this endpoint supports (e.g. \"chat\", \"embeddings\", \"completions\"). Derived from the destinations' backing models / providers at read time."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the model service was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Identity of the last updater."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name of the model service. Format: ``model-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``model_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the model service."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Whether the caller sees only metadata available through the BROWSE privilege."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Operational configuration: destinations, routing, rate limits, inference table. Required on CreateModelService; on UpdateModelService it is required only when ``config`` (or a ``config.*`` subpath) appears in ``update_mask``.",
    "children": [
      {
        "name": "inference_table",
        "type": "object",
        "description": "Inference table config for payload logging.",
        "children": [
          {
            "name": "parent",
            "type": "string",
            "description": "Parent UC schema where the inference table is created. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Set at create time and immutable thereafter; changing it on an existing service is rejected."
          },
          {
            "name": "disabled",
            "type": "boolean",
            "description": "Indicates whether payload logging is disabled (opt-out). Unset means that payload logging is active (the on-by-default state coincides with the proto zero-value, so the server never fills this field for a client that leaves it unset). Set ``disabled = true`` to pause runtime logging while keeping the sub-message attached (preserving ``parent`` and ``table_name_prefix`` for a later flip back to active). ``parent`` remains required either way."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "True when the bound inference TABLE has been deleted but the parent service still references it. The dangling reference is surfaced (not silently dropped) so callers can see the broken dependency. AI Gateway payload logging fails closed in this state."
          },
          {
            "name": "table",
            "type": "string",
            "description": "Resolved UC table for payload logs. Format: ``tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;``."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix for the inference-table's UC-registered name. The actual leaf name UC stores is ``&lt;table_name_prefix&gt;_payload``; the ``_payload`` suffix is appended automatically. To find the actual UC table after Create, read the ``table`` field on the response. Defaults to ``&lt;model_service_name&gt;_payload`` when unset. Set at create time and immutable thereafter; changing it on an existing service is rejected."
          }
        ]
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits applied to requests routed through this model service.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": "Scope key. Determines whether ``principal`` is required. (RATE_LIMIT_KEY_REQUEST_TAG, RATE_LIMIT_KEY_SERVICE, RATE_LIMIT_KEY_SERVICE_PRINCIPAL, RATE_LIMIT_KEY_USER, RATE_LIMIT_KEY_USER_DEFAULT, RATE_LIMIT_KEY_USER_GROUP)"
          },
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Renewal period. (RATE_LIMIT_RENEWAL_PERIOD_HOUR, RATE_LIMIT_RENEWAL_PERIOD_MINUTE)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal this limit applies to: user email, group name, or service principal application ID. Required unless ``key`` is ``RATE_LIMIT_KEY_SERVICE``, ``RATE_LIMIT_KEY_USER_DEFAULT``, or ``RATE_LIMIT_KEY_REQUEST_TAG`` (which must not set a principal)."
          },
          {
            "name": "request_tag_key",
            "type": "string",
            "description": "Request tag key this limit applies to. Required when ``key`` is ``RATE_LIMIT_KEY_REQUEST_TAG``, forbidden otherwise."
          },
          {
            "name": "request_tag_value",
            "type": "string",
            "description": "Request tag value this limit applies to. Only valid when ``key`` is ``RATE_LIMIT_KEY_REQUEST_TAG``. Leave unset to apply the limit to every value of ``request_tag_key`` (an any-value default); a set value is a specific override for that value."
          },
          {
            "name": "requests",
            "type": "integer",
            "description": "Max requests allowed within a renewal period. Leave unset for no request limit."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Max tokens allowed within a renewal period. Leave unset for no token limit."
          }
        ]
      },
      {
        "name": "routing",
        "type": "object",
        "description": "Routing configuration: destinations, routing strategy, and fallback.",
        "children": [
          {
            "name": "destinations",
            "type": "array",
            "description": "Primary routing destinations. At most 10 are allowed. At least one is required on CreateModelService; on UpdateModelService it is required only when ``config.routing`` (or a ``config.routing.*`` subpath) appears in ``update_mask``.",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": "User-facing label for this destination, used in routing references."
              },
              {
                "name": "destination_type",
                "type": "string",
                "description": "Backing-model category. Determines which oneof variant is populated. (DESTINATION_TYPE_EXTERNAL_FOUNDATION_MODEL, DESTINATION_TYPE_PAY_PER_TOKEN_FOUNDATION_MODEL, DESTINATION_TYPE_PROVISIONED_THROUGHPUT_FOUNDATION_MODEL)"
              },
              {
                "name": "external_model_config",
                "type": "object",
                "description": "Configuration for an external-foundation-model destination. Provider auth and provider-specific<br />    cloud configuration are owned by a separate, governed ModelProviderService entity referenced via<br />    ``model_provider_service``; the platform resolves the provider at invocation time."
              },
              {
                "name": "is_deleted",
                "type": "boolean",
                "description": "True when the destination's backing UC entity (MODEL for foundation-model destinations, MODEL_PROVIDER_SERVICE for external destinations) has been deleted but the destination row still references it. The dangling destination is surfaced (not silently dropped) so callers can see the broken routing. Inference traffic through this destination fails closed (BAD_REQUEST / FAILED_PRECONDITION)."
              },
              {
                "name": "pay_per_token_config",
                "type": "object",
                "description": "Configuration for a pay-per-token foundation-model destination. Identifies the foundation model<br />    by its UC resource name; the platform resolves it to a Model Serving endpoint at request time."
              },
              {
                "name": "provisioned_throughput_config",
                "type": "object",
                "description": "Configuration for a provisioned-throughput foundation-model destination. References a<br />    pre-existing Model Serving endpoint that serves the model; sizing (provisioned throughput, burst<br />    scaling, model version) is owned by the Model Serving endpoint itself, not by this message."
              },
              {
                "name": "traffic_percentage",
                "type": "integer",
                "description": "Share of traffic sent to this destination, 0-100. Optional on fallback destinations; see FallbackConfig."
              }
            ]
          },
          {
            "name": "fallback",
            "type": "object",
            "description": "Fallback routing config, applied after primary destinations fail.",
            "children": [
              {
                "name": "destinations",
                "type": "array",
                "description": "Ordered list of fallback destinations. Traversal is in list order; the attempt count is the length of the list. At most 5 are allowed."
              }
            ]
          },
          {
            "name": "first_token_timeout",
            "type": "string",
            "description": "Timeout for the first token of a streaming response. If a destination does not return its first token within this duration, AI Gateway aborts the attempt and fails over to the next destination. Applies to streaming requests only. Leave unset for no first-token timeout."
          },
          {
            "name": "traffic_splitting",
            "type": "object",
            "description": "Marker message selecting request-based traffic splitting. Traffic is distributed according to each destination's traffic_percentage value; no configuration lives on this message itself."
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the model service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "The resolved owner of the ModelService. Falls back to the caller's identity when ``owner`` is not explicitly set on creation."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency control token. Server-generated from the entity's state and returned on every read. To use it as an if-match precondition on a mutation, echo the last-read value back via the dedicated ``etag`` field on the Update / Delete request; the server rejects the mutation if the stored etag differs."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the model service. Write-only; read owner via effective_owner."
  },
  {
    "name": "supported_api_types",
    "type": "array",
    "description": "Unified API types this endpoint supports (e.g. \"chat\", \"embeddings\", \"completions\"). Derived from the destinations' backing models / providers at read time."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the model service was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Identity of the last updater."
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
    <td><a href="#parameter-include_browse"><code>include_browse</code></a></td>
    <td>Returns the model service identified by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>Lists the model services in a Unity Catalog schema. Provide ``parent`` as</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-model_service_id"><code>model_service_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-model_service"><code>model_service</code></a></td>
    <td></td>
    <td>Creates a model service in a Unity Catalog schema. A model service is a governed AI Gateway endpoint</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-model_service"><code>model_service</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Updates a model service. Only the fields named in ``update_mask`` are changed; the resource name is</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Deletes the model service identified by its resource name. Optionally supply an ``etag`` to make the</td>
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
<tr id="parameter-model_service_id">
    <td><CopyableCode code="model_service_id" /></td>
    <td><code>string</code></td>
    <td>Leaf identifier for the model service (the unqualified name within the parent schema, e.g. "my_model_service").</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name of the model service. Format: ``model-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Resource name of the parent schema. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The list of fields to update. The framework validates each path against the ``model_service`` field above. Wildcard paths (``paths: ["*"]``) are not supported; list each field path explicitly.</td>
</tr>
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>If-match precondition: when set, the delete proceeds only if the current server-side etag matches. Empty means unconditional delete.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include model services for which the principal can only access selective metadata.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of model services to return. Defaults to 100 when unset or 0; the maximum is 1000. Use ``next_page_token`` to retrieve additional pages.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from a previous request.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Resource name of the parent schema to list within, as ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>View selector controlling which fields are populated per row.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns the model service identified by its resource name.

```sql
SELECT
name,
metastore_id,
browse_only,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
owner,
supported_api_types,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_model_services
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
;
```
</TabItem>
<TabItem value="list">

Lists the model services in a Unity Catalog schema. Provide ``parent`` as

```sql
SELECT
name,
metastore_id,
browse_only,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
owner,
supported_api_types,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_model_services
WHERE deployment_name = '{{ deployment_name }}' -- required
AND include_browse = '{{ include_browse }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND parent = '{{ parent }}'
AND view = '{{ view }}'
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

Creates a model service in a Unity Catalog schema. A model service is a governed AI Gateway endpoint

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_model_services (
model_service,
parent,
model_service_id,
deployment_name
)
SELECT 
'{{ model_service }}' /* required */,
'{{ parent }}',
'{{ model_service_id }}',
'{{ deployment_name }}'
RETURNING
name,
metastore_id,
browse_only,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
owner,
supported_api_types,
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_model_services
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the ai_gateway_model_services resource.
    - name: model_service_id
      value: "{{ model_service_id }}"
      description: Required parameter for the ai_gateway_model_services resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_model_services resource.
    - name: model_service
      description: |
        The model service to create. The server populates \`\`name\`\` from \`\`parent\`\` + \`\`model_service_id\`\`; clients should leave it unset.
      value:
        browse_only: {{ browse_only }}
        comment: "{{ comment }}"
        config:
          inference_table:
            parent: "{{ parent }}"
            disabled: {{ disabled }}
            is_deleted: {{ is_deleted }}
            table: "{{ table }}"
            table_name_prefix: "{{ table_name_prefix }}"
          rate_limits:
            - key: "{{ key }}"
              renewal_period: "{{ renewal_period }}"
              principal: "{{ principal }}"
              request_tag_key: "{{ request_tag_key }}"
              request_tag_value: "{{ request_tag_value }}"
              requests: {{ requests }}
              tokens: {{ tokens }}
          routing:
            destinations:
              - name: "{{ name }}"
                destination_type: "{{ destination_type }}"
                external_model_config:
                  model_provider_service: "{{ model_provider_service }}"
                  target: "{{ target }}"
                is_deleted: {{ is_deleted }}
                pay_per_token_config:
                  model: "{{ model }}"
                provisioned_throughput_config:
                  model_serving_endpoint: "{{ model_serving_endpoint }}"
                  model: "{{ model }}"
                traffic_percentage: {{ traffic_percentage }}
            fallback:
              destinations:
                - name: "{{ name }}"
                  destination_type: "{{ destination_type }}"
                  external_model_config:
                    model_provider_service: "{{ model_provider_service }}"
                    target: "{{ target }}"
                  is_deleted: {{ is_deleted }}
                  pay_per_token_config:
                    model: "{{ model }}"
                  provisioned_throughput_config:
                    model_serving_endpoint: "{{ model_serving_endpoint }}"
                    model: "{{ model }}"
                  traffic_percentage: {{ traffic_percentage }}
            first_token_timeout: "{{ first_token_timeout }}"
            traffic_splitting: "{{ traffic_splitting }}"
        create_time: "{{ create_time }}"
        created_by: "{{ created_by }}"
        effective_owner: "{{ effective_owner }}"
        etag: "{{ etag }}"
        metastore_id: "{{ metastore_id }}"
        name: "{{ name }}"
        owner: "{{ owner }}"
        supported_api_types:
          - "{{ supported_api_types }}"
        update_time: "{{ update_time }}"
        updated_by: "{{ updated_by }}"
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

Updates a model service. Only the fields named in ``update_mask`` are changed; the resource name is

```sql
UPDATE databricks_workspace.catalog.ai_gateway_model_services
SET 
model_service = '{{ model_service }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND model_service = '{{ model_service }}' --required
AND etag = '{{ etag}}'
RETURNING
name,
metastore_id,
browse_only,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
owner,
supported_api_types,
update_time,
updated_by;
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

Deletes the model service identified by its resource name. Optionally supply an ``etag`` to make the

```sql
DELETE FROM databricks_workspace.catalog.ai_gateway_model_services
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>
