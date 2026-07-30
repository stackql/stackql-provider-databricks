---
title: ai_gateway_model_provider_services
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_model_provider_services
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

Creates, updates, deletes, gets or lists an <code>ai_gateway_model_provider_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_model_provider_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_model_provider_services" /></td></tr>
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
    "description": "Resource name of the provider service. Format: ``model-provider-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_provider_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``model_provider_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the provider service."
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
    "description": "Behavioral configuration: provider connection, model catalog, and passthrough policy. See ``ModelProviderServiceConfig`` for the per-field contract. Required on CreateModelProviderService; on Update it is required only when ``config`` (or a ``config.*`` subpath) appears in ``update_mask``.",
    "children": [
      {
        "name": "allow_all_targets",
        "type": "boolean",
        "description": "When true, accepts any model exposed by the upstream provider; ``targets`` is not required and does not restrict routability. When false, only models listed in ``targets`` are routable."
      },
      {
        "name": "amazon_bedrock",
        "type": "object",
        "description": "Amazon Bedrock provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct form of Amazon Bedrock provider config.<br /><br />    Authentication is one of two mutually exclusive modes, exactly one of which must be supplied on<br />    Create:<br /><br />    - Access keys: set ``aws_access_key``, leave ``service_credential`` unset.<br />    - UC service credential: set ``service_credential.name`` to the AIP-122 resource-name form<br />      ``credentials/&#123;name&#125;``, leave ``aws_access_key`` unset. The credential value lives in UC and<br />      is referenced by name, not held on this message. Setting more than one mode is rejected.",
            "children": [
              {
                "name": "aws_access_key",
                "type": "object",
                "description": "AWS access-key-pair auth. Mutually exclusive with ``service_credential``. Supersedes the flat ``aws_access_key_id`` / ``aws_secret_access_key`` fields."
              },
              {
                "name": "aws_access_key_id",
                "type": "string",
                "description": "Deprecated flat AWS access key ID. Superseded by ``aws_access_key.access_key_id``. Kept for one migration cycle; the handler mirrors it to/from ``aws_access_key``. Treated as username-equivalent (not a secret value): round-trips on reads and is scrubbed from audit logs."
              },
              {
                "name": "aws_secret_access_key",
                "type": "object",
                "description": "Deprecated flat AWS secret access key. Superseded by ``aws_access_key.secret_access_key``. Kept for one migration cycle; the handler mirrors it to/from ``aws_access_key``. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              },
              {
                "name": "region",
                "type": "string",
                "description": "AWS region where the Bedrock endpoint is hosted (e.g., ``us-east-1``). Required on Create."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a UC service credential authorizing Bedrock requests. On Create the caller supplies ``service_credential.name`` in the AIP-122 resource-name form ``credentials/&#123;name&#125;``. Required on Create when using UC-service-credential auth; mutually exclusive with ``aws_access_key``. The credential is referenced by name; its value is not carried here. On read the resolved ``id`` and ``is_deleted`` are also populated. Only supported on AWS-hosted workspaces; Create requests from other clouds are rejected with INVALID_PARAMETER_VALUE."
              }
            ]
          }
        ]
      },
      {
        "name": "anthropic",
        "type": "object",
        "description": "Anthropic provider configuration. Exactly one of ``direct`` or ``relayed`` must be set on<br />    Create; the two are mutually exclusive.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct (inline-credentials) form: caller supplies the API key in the request body. Required on Create unless ``relayed`` is set.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Anthropic API key. Required on Create. Sent as the ``x-api-key`` header on outbound requests. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              }
            ]
          },
          {
            "name": "relayed",
            "type": "object",
            "description": "Relayed (credential-less) form: no Anthropic credential is stored. Each inference request instead carries the caller's own OAuth token, which the platform forwards to Anthropic on outbound requests. Mutually exclusive with ``direct``; no ``api_key`` is required or persisted.",
            "children": [
              {
                "name": "plan_type",
                "type": "string",
                "description": "Which Anthropic subscription tier the relayed token belongs to. Optional; when unset the MPS gets the full governance surface (see TEAM_ENTERPRISE). Immutable after Create, so the tier cannot be flipped in place. (ANTHROPIC_RELAYED_PLAN_TYPE_MAX, ANTHROPIC_RELAYED_PLAN_TYPE_TEAM_ENTERPRISE)"
              }
            ]
          }
        ]
      },
      {
        "name": "azure_openai",
        "type": "object",
        "description": "Azure OpenAI provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct form of Azure OpenAI provider config. Exactly one of three mutually-exclusive auth modes<br />    must be supplied on Create:<br /><br />    - API key: set ``api_key``, leave ``entra_service_principal`` and ``service_credential`` unset.<br />    - Entra ID (service principal): set ``entra_service_principal``, leave ``api_key`` and<br />      ``service_credential`` unset.<br />    - UC service credential: set ``service_credential.name`` to the AIP-122 resource-name form<br />      ``credentials/&#123;name&#125;``, leave ``api_key`` and ``entra_service_principal`` unset. The<br />      credential value lives in UC and is referenced by name, not held on this message. Only<br />      supported on Azure-hosted workspaces. Setting more than one mode is rejected.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Azure OpenAI API key. Mutually exclusive with the Entra and service-credential modes. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Full Azure OpenAI endpoint base URL, e.g. ``https://myresource.openai.azure.com``. Required on Create."
              },
              {
                "name": "client_id",
                "type": "string",
                "description": "Deprecated flat Entra client ID. Superseded by ``entra_service_principal.client_id``. Kept for one migration cycle; the handler mirrors it to/from ``entra_service_principal``."
              },
              {
                "name": "client_secret",
                "type": "object",
                "description": "Deprecated flat Entra client secret. Superseded by ``entra_service_principal.client_secret``. Kept for one migration cycle; the handler mirrors it to/from ``entra_service_principal``. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              },
              {
                "name": "entra_service_principal",
                "type": "object",
                "description": "Entra ID (service principal) auth. Mutually exclusive with ``api_key`` and ``service_credential``. Supersedes the flat ``tenant_id`` / ``client_id`` / ``client_secret`` fields."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a UC service credential authorizing Azure OpenAI requests. On Create the caller supplies ``service_credential.name`` in the AIP-122 resource-name form ``credentials/&#123;name&#125;``. Required on Create when using UC-service-credential auth; mutually exclusive with ``api_key`` and ``entra_service_principal``. The credential is referenced by name; its value is not carried here. On read the resolved ``id`` and ``is_deleted`` are also populated. Only supported on Azure-hosted workspaces; Create requests from other clouds are rejected with INVALID_PARAMETER_VALUE."
              },
              {
                "name": "tenant_id",
                "type": "string",
                "description": "Deprecated flat Entra tenant ID. Superseded by ``entra_service_principal.tenant_id``. Kept for one migration cycle; the handler mirrors it to/from ``entra_service_principal``."
              }
            ]
          }
        ]
      },
      {
        "name": "custom",
        "type": "object",
        "description": "Custom provider configuration: arbitrary HTTP endpoint with bearer-token auth.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct form of custom provider config.<br /><br />    Authentication is one of two mutually exclusive modes, exactly one of which must be supplied on<br />    Create:<br /><br />    - Bearer: set ``api_key``, leave ``header_auth`` unset. The secret is forwarded as<br />      ``Authorization: Bearer &lt;secret&gt;``.<br />    - Header: set ``header_auth``, leave ``api_key`` unset. The secret is forwarded as<br />      ``&lt;api_key_name&gt;: &lt;api_key_value&gt;``. Setting both modes or neither mode is rejected.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Bearer token forwarded as the ``Authorization: Bearer ...`` header on outbound requests. Supplied as inline plaintext via ``ProviderSecret.plaintext``. Set this for bearer-token auth."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Endpoint URL of the OpenAI-compatible service (e.g., ``https://api.example.com/v1``). Required on Create."
              }
            ]
          }
        ]
      },
      {
        "name": "forward_headers",
        "type": "boolean",
        "description": "Whether to forward incoming request headers to the upstream provider. Applies to managed (multi-model) requests as well as passthrough requests served by this provider service. Governance-level decision by the provider service owner; not selectable per inference call."
      },
      {
        "name": "forward_query_parameters",
        "type": "boolean",
        "description": "Whether to forward incoming request query parameters to the upstream provider. Same trust-boundary semantics as ``forward_headers``."
      },
      {
        "name": "forward_unmanaged_paths",
        "type": "boolean",
        "description": "Whether to forward request paths that fall outside this service's managed API set to the upstream provider as opaque passthrough. When true, requests addressed to subpaths not recognized by the managed API surface are proxied to the upstream provider over the same provider connection. When false, only managed-API paths are served. Governance-level decision by the provider service owner; expanding this expands the trust boundary that the ModelProviderService exposes."
      },
      {
        "name": "gemini_enterprise",
        "type": "object",
        "description": "Gemini Enterprise provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct form of Gemini Enterprise provider config.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Google Gemini Enterprise API key. Required on Create. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              },
              {
                "name": "project_id",
                "type": "string",
                "description": "GCP project ID hosting the Gemini Enterprise endpoint. Required on Create."
              },
              {
                "name": "region",
                "type": "string",
                "description": "GCP region of the Gemini Enterprise endpoint (e.g., ``us-central1``). Required on Create."
              }
            ]
          }
        ]
      },
      {
        "name": "inference_table",
        "type": "object",
        "description": "Inference table configuration for payload logging when this provider service is invoked directly. When it is invoked through a model service, the model service's own inference table captures the invocation instead. Mirrors ``ModelServiceConfig.inference_table`` / ``AgentServiceConfig.inference_table``.",
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
        "name": "microsoft_foundry",
        "type": "object",
        "description": "Microsoft Foundry provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct form of Microsoft Foundry provider config.<br /><br />    Authentication is one of three mutually exclusive modes, exactly one of which must be supplied<br />    on Create:<br /><br />    - API key: set ``api_key``, leave ``entra_service_principal`` and ``service_credential`` unset.<br />    - Entra ID (service principal): set ``entra_service_principal``, leave ``api_key`` and<br />      ``service_credential`` unset. AI Gateway exchanges these for an Entra bearer token on outbound<br />      requests via the OAuth2 client-credentials grant.<br />    - UC service credential: set ``service_credential.name`` to the AIP-122 resource-name form<br />      ``credentials/&#123;name&#125;``, leave ``api_key`` and ``entra_service_principal`` unset. The<br />      credential value lives in UC and is referenced by name, not held on this message. Only<br />      supported on Azure-hosted workspaces. Setting more than one mode is rejected.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Microsoft AI Foundry API key. Mutually exclusive with the Entra and service-credential modes. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Microsoft AI Foundry endpoint URL. Required on Create."
              },
              {
                "name": "client_id",
                "type": "string",
                "description": "Deprecated flat Entra client ID. Superseded by ``entra_service_principal.client_id``. Kept for one migration cycle; the handler mirrors it to/from ``entra_service_principal``."
              },
              {
                "name": "client_secret",
                "type": "object",
                "description": "Deprecated flat Entra client secret. Superseded by ``entra_service_principal.client_secret``. Kept for one migration cycle; the handler mirrors it to/from ``entra_service_principal``. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              },
              {
                "name": "entra_service_principal",
                "type": "object",
                "description": "Entra ID (service principal) auth. Mutually exclusive with ``api_key`` and ``service_credential``. Supersedes the flat ``tenant_id`` / ``client_id`` / ``client_secret`` fields."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a UC service credential authorizing Microsoft Foundry requests. On Create the caller supplies ``service_credential.name`` in the AIP-122 resource-name form ``credentials/&#123;name&#125;``. Required on Create when using UC-service-credential auth; mutually exclusive with ``api_key`` and ``entra_service_principal``. The credential is referenced by name; its value is not carried here. On read the resolved ``id`` and ``is_deleted`` are also populated. Only supported on Azure-hosted workspaces; Create requests from other clouds are rejected with INVALID_PARAMETER_VALUE."
              },
              {
                "name": "tenant_id",
                "type": "string",
                "description": "Deprecated flat Entra tenant ID. Superseded by ``entra_service_principal.tenant_id``. Kept for one migration cycle; the handler mirrors it to/from ``entra_service_principal``."
              }
            ]
          }
        ]
      },
      {
        "name": "openai",
        "type": "object",
        "description": "OpenAI provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct (inline-credentials) form of the OpenAI provider config.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "OpenAI API key. Required on Create. Supplied as inline plaintext via ``ProviderSecret.plaintext``."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Optional custom base URL. Defaults to ``https://api.openai.com/v1``. Use for OpenAI-API-compatible third-party endpoints or in-network proxies."
              },
              {
                "name": "organization",
                "type": "string",
                "description": "Optional OpenAI organization ID. When set, the platform forwards it as the ``OpenAI-Organization`` header."
              }
            ]
          }
        ]
      },
      {
        "name": "provider_type",
        "type": "string",
        "description": "Provider type discriminator. Required at create time; immutable after. Determines which variant of the ``provider`` oneof must be set. May not be changed via Update; attempts to include ``config.provider_type`` in ``UpdateModelProviderServiceRequest.update_mask`` are rejected. Required on CreateModelProviderService and immutable thereafter. (EXTERNAL_MODEL_PROVIDER_TYPE_AMAZON_BEDROCK, EXTERNAL_MODEL_PROVIDER_TYPE_ANTHROPIC, EXTERNAL_MODEL_PROVIDER_TYPE_AZURE_OPENAI, EXTERNAL_MODEL_PROVIDER_TYPE_CUSTOM, EXTERNAL_MODEL_PROVIDER_TYPE_GEMINI_ENTERPRISE, EXTERNAL_MODEL_PROVIDER_TYPE_MICROSOFT_FOUNDRY, EXTERNAL_MODEL_PROVIDER_TYPE_OPENAI)"
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits applied when this provider service is invoked directly. When it is invoked through a model service, the model service's own ``rate_limits`` apply instead. Mirrors ``ModelServiceConfig.rate_limits`` / ``McpServiceConfig.rate_limits``.",
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
        "name": "targets",
        "type": "array",
        "description": "Routing targets this provider service exposes (provider-side model identifier + unified API types per entry). Required (&gt;=1) when ``allow_all_targets = false``; optional and additive when ``allow_all_targets = true``. References from ``ExternalModelConfig.target`` must match an entry here unless ``allow_all_targets = true``.",
        "children": [
          {
            "name": "model",
            "type": "string",
            "description": "Provider-side model identifier (e.g. \"gpt-5\", \"claude-opus-4-7\"). This is a string on the LLM provider's side, not a UC entity. The UC governance hook for external destinations is the ModelProviderService referenced by ``ExternalModelConfig.model_provider_service``, not the model itself."
          },
          {
            "name": "native_api_types",
            "type": "array",
            "description": "Provider-native API types the model supports (e.g. \"openai/v1/chat/completions\"). Used by the platform for request/response translation from the unified API type. At most 64 entries of at most 256 characters each; the list is persisted into the destination binding's bounded storage envelope."
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the provider service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "The resolved owner of the model provider service. Falls back to the caller's identity when ``owner`` is not explicitly set on creation."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency control token. Server-generated from the entity's state and returned on every read. To use it as an if-match precondition on a mutation, echo the last-read value back via the dedicated ``etag`` field on the Update / Delete request; the server rejects the mutation if the stored etag differs."
  },
  {
    "name": "owner",
    "type": "string",
    "description": "The owner of the model provider service. Write-only; read owner via effective_owner."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the provider service was last modified."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_browse"><code>include_browse</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>Lists the model provider services in a Unity Catalog schema. Provide ``parent`` as</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-model_provider_service_id"><code>model_provider_service_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-model_provider_service"><code>model_provider_service</code></a></td>
    <td></td>
    <td>Creates a model provider service in a Unity Catalog schema. A model provider service is a governed</td>
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
<tr id="parameter-model_provider_service_id">
    <td><CopyableCode code="model_provider_service_id" /></td>
    <td><code>string</code></td>
    <td>Leaf identifier for the provider service (the unqualified name within the parent schema, e.g. "openai_prod").</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Resource name of the parent schema. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-include_browse">
    <td><CopyableCode code="include_browse" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include provider services for which the principal can only access selective metadata.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of provider services to return. Defaults to 100 when unset or 0; the maximum is 1000. Use ``next_page_token`` to retrieve additional pages.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists the model provider services in a Unity Catalog schema. Provide ``parent`` as

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
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_model_provider_services
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

Creates a model provider service in a Unity Catalog schema. A model provider service is a governed

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_model_provider_services (
model_provider_service,
parent,
model_provider_service_id,
deployment_name
)
SELECT 
'{{ model_provider_service }}' /* required */,
'{{ parent }}',
'{{ model_provider_service_id }}',
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
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_model_provider_services
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the ai_gateway_model_provider_services resource.
    - name: model_provider_service_id
      value: "{{ model_provider_service_id }}"
      description: Required parameter for the ai_gateway_model_provider_services resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_model_provider_services resource.
    - name: model_provider_service
      description: |
        The model provider service to create. The server populates \`\`name\`\` from \`\`parent\`\` + \`\`model_provider_service_id\`\`; clients should leave it unset.
      value:
        browse_only: {{ browse_only }}
        comment: "{{ comment }}"
        config:
          allow_all_targets: {{ allow_all_targets }}
          amazon_bedrock:
            direct:
              aws_access_key:
                access_key_id: "{{ access_key_id }}"
                secret_access_key: "{{ secret_access_key }}"
              aws_access_key_id: "{{ aws_access_key_id }}"
              aws_secret_access_key:
                plaintext: "{{ plaintext }}"
              region: "{{ region }}"
              service_credential:
                name: "{{ name }}"
          anthropic:
            direct:
              api_key:
                plaintext: "{{ plaintext }}"
            relayed:
              plan_type: "{{ plan_type }}"
          azure_openai:
            direct:
              api_key:
                plaintext: "{{ plaintext }}"
              base_url: "{{ base_url }}"
              client_id: "{{ client_id }}"
              client_secret:
                plaintext: "{{ plaintext }}"
              entra_service_principal:
                client_id: "{{ client_id }}"
                client_secret: "{{ client_secret }}"
                tenant_id: "{{ tenant_id }}"
              service_credential:
                name: "{{ name }}"
              tenant_id: "{{ tenant_id }}"
          custom:
            direct:
              api_key:
                plaintext: "{{ plaintext }}"
              base_url: "{{ base_url }}"
          forward_headers: {{ forward_headers }}
          forward_query_parameters: {{ forward_query_parameters }}
          forward_unmanaged_paths: {{ forward_unmanaged_paths }}
          gemini_enterprise:
            direct:
              api_key:
                plaintext: "{{ plaintext }}"
              project_id: "{{ project_id }}"
              region: "{{ region }}"
          inference_table:
            parent: "{{ parent }}"
            disabled: {{ disabled }}
            is_deleted: {{ is_deleted }}
            table: "{{ table }}"
            table_name_prefix: "{{ table_name_prefix }}"
          microsoft_foundry:
            direct:
              api_key:
                plaintext: "{{ plaintext }}"
              base_url: "{{ base_url }}"
              client_id: "{{ client_id }}"
              client_secret:
                plaintext: "{{ plaintext }}"
              entra_service_principal:
                client_id: "{{ client_id }}"
                client_secret: "{{ client_secret }}"
                tenant_id: "{{ tenant_id }}"
              service_credential:
                name: "{{ name }}"
              tenant_id: "{{ tenant_id }}"
          openai:
            direct:
              api_key:
                plaintext: "{{ plaintext }}"
              base_url: "{{ base_url }}"
              organization: "{{ organization }}"
          provider_type: "{{ provider_type }}"
          rate_limits:
            - key: "{{ key }}"
              renewal_period: "{{ renewal_period }}"
              principal: "{{ principal }}"
              request_tag_key: "{{ request_tag_key }}"
              request_tag_value: "{{ request_tag_value }}"
              requests: {{ requests }}
              tokens: {{ tokens }}
          targets:
            - model: "{{ model }}"
              native_api_types: "{{ native_api_types }}"
        create_time: "{{ create_time }}"
        created_by: "{{ created_by }}"
        effective_owner: "{{ effective_owner }}"
        etag: "{{ etag }}"
        metastore_id: "{{ metastore_id }}"
        name: "{{ name }}"
        owner: "{{ owner }}"
        update_time: "{{ update_time }}"
        updated_by: "{{ updated_by }}"
`}</CodeBlock>

</TabItem>
</Tabs>
