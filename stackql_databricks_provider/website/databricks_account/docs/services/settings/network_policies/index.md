---
title: network_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - network_policies
  - settings
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>network_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.network_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_network_policy_rpc"
    values={[
        { label: 'get_network_policy_rpc', value: 'get_network_policy_rpc' },
        { label: 'list_network_policies_rpc', value: 'list_network_policies_rpc' }
    ]}
>
<TabItem value="get_network_policy_rpc">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "network_policy_id",
    "type": "string",
    "description": "The unique identifier for the network policy."
  },
  {
    "name": "egress",
    "type": "object",
    "description": "The network policies applying for egress traffic.",
    "children": [
      {
        "name": "network_access",
        "type": "object",
        "description": "The access policy enforced for egress traffic to the internet.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "At which level can Databricks and Databricks managed compute access Internet. FULL_ACCESS:<br />Databricks can access Internet. No blocking rules will apply. RESTRICTED_ACCESS: Databricks can<br />only access explicitly allowed internet and storage destinations, as well as UC connections and<br />external locations. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allowed_databricks_destinations",
            "type": "array",
            "description": "List of Databricks workspace destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "workspace_ids",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "allowed_internet_destinations",
            "type": "array",
            "description": "List of internet destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "The internet destination to which access will be allowed. Format dependent on the destination type."
              },
              {
                "name": "internet_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DNS_NAME)"
              }
            ]
          },
          {
            "name": "allowed_storage_destinations",
            "type": "array",
            "description": "List of storage destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "azure_storage_account",
                "type": "string",
                "description": "The Azure storage account name."
              },
              {
                "name": "azure_storage_service",
                "type": "string",
                "description": "The Azure storage service type (blob, dfs, etc.)."
              },
              {
                "name": "bucket_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "region",
                "type": "string",
                "description": ""
              },
              {
                "name": "storage_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (AWS_S3, AZURE_STORAGE, GOOGLE_CLOUD_STORAGE)"
              }
            ]
          },
          {
            "name": "blocked_internet_destinations",
            "type": "array",
            "description": "List of internet destinations that serverless workloads are blocked from accessing. These destinations are enforced when restriction mode is RESTRICTED_ACCESS or DRY_RUN. Currently supports DNS_NAME type only; IP_RANGE support is planned.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "The internet destination to which access will be allowed. Format dependent on the destination type."
              },
              {
                "name": "internet_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DNS_NAME)"
              }
            ]
          },
          {
            "name": "policy_enforcement",
            "type": "object",
            "description": "Optional. When policy_enforcement is not provided, we default to ENFORCE_MODE_ALL_SERVICES",
            "children": [
              {
                "name": "dry_run_mode_product_filter",
                "type": "array",
                "description": ""
              },
              {
                "name": "enforcement_mode",
                "type": "string",
                "description": "The mode of policy enforcement. ENFORCED blocks traffic that violates policy, while DRY_RUN only logs violations without blocking. When not specified, defaults to ENFORCED. (DRY_RUN, ENFORCED)"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "ingress",
    "type": "object",
    "description": "The network policies applying for ingress traffic.",
    "children": [
      {
        "name": "cross_workspace_access",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "private_access",
        "type": "object",
        "description": "The network policy restrictions for private access. Configures how requests arriving over private connectivity are governed.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "The restriction mode for private access. (ALLOW_ALL_REGISTERED_ENDPOINTS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "Allow rules are evaluated after deny rules. A request matching any allow rule is allowed; a request matching no rule is denied by default. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "Deny rules are evaluated first. A request matching any deny rule is denied, regardless of allow rules. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          }
        ]
      },
      {
        "name": "public_access",
        "type": "object",
        "description": "The network policy restrictions for public access to the workspace. Configures how public internet traffic is allowed or denied access.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "ingress_dry_run",
    "type": "object",
    "description": "The ingress policy for dry run mode. Dry run will always run even if the request is allowed by the ingress policy. When this field is set, the policy will be evaluated and emit logs only without blocking requests.",
    "children": [
      {
        "name": "cross_workspace_access",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "private_access",
        "type": "object",
        "description": "The network policy restrictions for private access. Configures how requests arriving over private connectivity are governed.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "The restriction mode for private access. (ALLOW_ALL_REGISTERED_ENDPOINTS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "Allow rules are evaluated after deny rules. A request matching any allow rule is allowed; a request matching no rule is denied by default. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "Deny rules are evaluated first. A request matching any deny rule is denied, regardless of allow rules. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          }
        ]
      },
      {
        "name": "public_access",
        "type": "object",
        "description": "The network policy restrictions for public access to the workspace. Configures how public internet traffic is allowed or denied access.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list_network_policies_rpc">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "network_policy_id",
    "type": "string",
    "description": "The unique identifier for the network policy."
  },
  {
    "name": "egress",
    "type": "object",
    "description": "The network policies applying for egress traffic.",
    "children": [
      {
        "name": "network_access",
        "type": "object",
        "description": "The access policy enforced for egress traffic to the internet.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "At which level can Databricks and Databricks managed compute access Internet. FULL_ACCESS:<br />Databricks can access Internet. No blocking rules will apply. RESTRICTED_ACCESS: Databricks can<br />only access explicitly allowed internet and storage destinations, as well as UC connections and<br />external locations. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allowed_databricks_destinations",
            "type": "array",
            "description": "List of Databricks workspace destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "workspace_ids",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "allowed_internet_destinations",
            "type": "array",
            "description": "List of internet destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "The internet destination to which access will be allowed. Format dependent on the destination type."
              },
              {
                "name": "internet_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DNS_NAME)"
              }
            ]
          },
          {
            "name": "allowed_storage_destinations",
            "type": "array",
            "description": "List of storage destinations that serverless workloads are allowed to access when in RESTRICTED_ACCESS mode.",
            "children": [
              {
                "name": "azure_storage_account",
                "type": "string",
                "description": "The Azure storage account name."
              },
              {
                "name": "azure_storage_service",
                "type": "string",
                "description": "The Azure storage service type (blob, dfs, etc.)."
              },
              {
                "name": "bucket_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "region",
                "type": "string",
                "description": ""
              },
              {
                "name": "storage_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (AWS_S3, AZURE_STORAGE, GOOGLE_CLOUD_STORAGE)"
              }
            ]
          },
          {
            "name": "blocked_internet_destinations",
            "type": "array",
            "description": "List of internet destinations that serverless workloads are blocked from accessing. These destinations are enforced when restriction mode is RESTRICTED_ACCESS or DRY_RUN. Currently supports DNS_NAME type only; IP_RANGE support is planned.",
            "children": [
              {
                "name": "destination",
                "type": "string",
                "description": "The internet destination to which access will be allowed. Format dependent on the destination type."
              },
              {
                "name": "internet_destination_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DNS_NAME)"
              }
            ]
          },
          {
            "name": "policy_enforcement",
            "type": "object",
            "description": "Optional. When policy_enforcement is not provided, we default to ENFORCE_MODE_ALL_SERVICES",
            "children": [
              {
                "name": "dry_run_mode_product_filter",
                "type": "array",
                "description": ""
              },
              {
                "name": "enforcement_mode",
                "type": "string",
                "description": "The mode of policy enforcement. ENFORCED blocks traffic that violates policy, while DRY_RUN only logs violations without blocking. When not specified, defaults to ENFORCED. (DRY_RUN, ENFORCED)"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "ingress",
    "type": "object",
    "description": "The network policies applying for ingress traffic.",
    "children": [
      {
        "name": "cross_workspace_access",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "private_access",
        "type": "object",
        "description": "The network policy restrictions for private access. Configures how requests arriving over private connectivity are governed.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "The restriction mode for private access. (ALLOW_ALL_REGISTERED_ENDPOINTS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "Allow rules are evaluated after deny rules. A request matching any allow rule is allowed; a request matching no rule is denied by default. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "Deny rules are evaluated first. A request matching any deny rule is denied, regardless of allow rules. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          }
        ]
      },
      {
        "name": "public_access",
        "type": "object",
        "description": "The network policy restrictions for public access to the workspace. Configures how public internet traffic is allowed or denied access.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "ingress_dry_run",
    "type": "object",
    "description": "The ingress policy for dry run mode. Dry run will always run even if the request is allowed by the ingress policy. When this field is set, the policy will be evaluated and emit logs only without blocking requests.",
    "children": [
      {
        "name": "cross_workspace_access",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "private_access",
        "type": "object",
        "description": "The network policy restrictions for private access. Configures how requests arriving over private connectivity are governed.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "The restriction mode for private access. (ALLOW_ALL_REGISTERED_ENDPOINTS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "Allow rules are evaluated after deny rules. A request matching any allow rule is allowed; a request matching no rule is denied by default. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "Deny rules are evaluated first. A request matching any deny rule is denied, regardless of allow rules. Only applies when restriction_mode is RESTRICTED_ACCESS.",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": "The authenticated identity the request must match. When unset, the rule matches all users and service principals. On the account-level network policy, scoping to specific identities is not currently supported, so this field must be unset (the rule matches all users and service principals)."
              },
              {
                "name": "destination",
                "type": "object",
                "description": "The destination the request must match — the resource being accessed, for example the workspace UI, workspace APIs, or account-level APIs. See RequestDestination."
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": "The origin the request must match — the private connectivity the request arrives through, for example a specific set of registered endpoints or any endpoint registered to the account. See PrivateRequestOrigin."
              }
            ]
          }
        ]
      },
      {
        "name": "public_access",
        "type": "object",
        "description": "The network policy restrictions for public access to the workspace. Configures how public internet traffic is allowed or denied access.",
        "children": [
          {
            "name": "restriction_mode",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FULL_ACCESS, RESTRICTED_ACCESS)"
          },
          {
            "name": "allow_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "deny_rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "authentication",
                "type": "object",
                "description": ""
              },
              {
                "name": "destination",
                "type": "object",
                "description": ""
              },
              {
                "name": "label",
                "type": "string",
                "description": "The label for this ingress rule."
              },
              {
                "name": "origin",
                "type": "object",
                "description": ""
              }
            ]
          }
        ]
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
    <td><a href="#get_network_policy_rpc"><CopyableCode code="get_network_policy_rpc" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_policy_id"><code>network_policy_id</code></a></td>
    <td></td>
    <td>Gets a network policy.</td>
</tr>
<tr>
    <td><a href="#list_network_policies_rpc"><CopyableCode code="list_network_policies_rpc" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets an array of network policies.</td>
</tr>
<tr>
    <td><a href="#create_network_policy_rpc"><CopyableCode code="create_network_policy_rpc" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_policy"><code>network_policy</code></a></td>
    <td></td>
    <td>Creates a new network policy to manage which network destinations can be accessed from the Databricks</td>
</tr>
<tr>
    <td><a href="#update_network_policy_rpc"><CopyableCode code="update_network_policy_rpc" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_policy_id"><code>network_policy_id</code></a>, <a href="#parameter-network_policy"><code>network_policy</code></a></td>
    <td></td>
    <td>Updates a network policy. This allows you to modify the configuration of a network policy.</td>
</tr>
<tr>
    <td><a href="#delete_network_policy_rpc"><CopyableCode code="delete_network_policy_rpc" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network_policy_id"><code>network_policy_id</code></a></td>
    <td></td>
    <td>Deletes a network policy. Cannot be called on 'default-policy'.</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-network_policy_id">
    <td><CopyableCode code="network_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the network policy to delete.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to next page based on previous query.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_network_policy_rpc"
    values={[
        { label: 'get_network_policy_rpc', value: 'get_network_policy_rpc' },
        { label: 'list_network_policies_rpc', value: 'list_network_policies_rpc' }
    ]}
>
<TabItem value="get_network_policy_rpc">

Gets a network policy.

```sql
SELECT
account_id,
network_policy_id,
egress,
ingress,
ingress_dry_run
FROM databricks_account.settings.network_policies
WHERE account_id = '{{ account_id }}' -- required
AND network_policy_id = '{{ network_policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list_network_policies_rpc">

Gets an array of network policies.

```sql
SELECT
account_id,
network_policy_id,
egress,
ingress,
ingress_dry_run
FROM databricks_account.settings.network_policies
WHERE account_id = '{{ account_id }}' -- required
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_network_policy_rpc"
    values={[
        { label: 'create_network_policy_rpc', value: 'create_network_policy_rpc' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_network_policy_rpc">

Creates a new network policy to manage which network destinations can be accessed from the Databricks

```sql
INSERT INTO databricks_account.settings.network_policies (
network_policy,
account_id
)
SELECT 
'{{ network_policy }}' /* required */,
'{{ account_id }}'
RETURNING
account_id,
network_policy_id,
egress,
ingress,
ingress_dry_run
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_policies
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the network_policies resource.
    - name: network_policy
      description: |
        Network policy configuration details.
      value:
        account_id: "{{ account_id }}"
        egress:
          network_access:
            restriction_mode: "{{ restriction_mode }}"
            allowed_databricks_destinations:
              - workspace_ids: "{{ workspace_ids }}"
            allowed_internet_destinations:
              - destination: "{{ destination }}"
                internet_destination_type: "{{ internet_destination_type }}"
            allowed_storage_destinations:
              - azure_storage_account: "{{ azure_storage_account }}"
                azure_storage_service: "{{ azure_storage_service }}"
                bucket_name: "{{ bucket_name }}"
                region: "{{ region }}"
                storage_destination_type: "{{ storage_destination_type }}"
            blocked_internet_destinations:
              - destination: "{{ destination }}"
                internet_destination_type: "{{ internet_destination_type }}"
            policy_enforcement:
              dry_run_mode_product_filter:
                - "{{ dry_run_mode_product_filter }}"
              enforcement_mode: "{{ enforcement_mode }}"
        ingress:
          cross_workspace_access:
            restriction_mode: "{{ restriction_mode }}"
            allow_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_source_workspaces: {{ all_source_workspaces }}
                  selected_workspaces: "{{ selected_workspaces }}"
            deny_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_source_workspaces: {{ all_source_workspaces }}
                  selected_workspaces: "{{ selected_workspaces }}"
          private_access:
            restriction_mode: "{{ restriction_mode }}"
            allow_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_private_access: {{ all_private_access }}
                  all_registered_endpoints: {{ all_registered_endpoints }}
                  azure_workspace_private_link: {{ azure_workspace_private_link }}
                  endpoints: "{{ endpoints }}"
            deny_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_private_access: {{ all_private_access }}
                  all_registered_endpoints: {{ all_registered_endpoints }}
                  azure_workspace_private_link: {{ azure_workspace_private_link }}
                  endpoints: "{{ endpoints }}"
          public_access:
            restriction_mode: "{{ restriction_mode }}"
            allow_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_ip_ranges: {{ all_ip_ranges }}
                  excluded_ip_ranges: "{{ excluded_ip_ranges }}"
                  included_ip_ranges: "{{ included_ip_ranges }}"
                  managed_ip_range: "{{ managed_ip_range }}"
            deny_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_ip_ranges: {{ all_ip_ranges }}
                  excluded_ip_ranges: "{{ excluded_ip_ranges }}"
                  included_ip_ranges: "{{ included_ip_ranges }}"
                  managed_ip_range: "{{ managed_ip_range }}"
        ingress_dry_run:
          cross_workspace_access:
            restriction_mode: "{{ restriction_mode }}"
            allow_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_source_workspaces: {{ all_source_workspaces }}
                  selected_workspaces: "{{ selected_workspaces }}"
            deny_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_source_workspaces: {{ all_source_workspaces }}
                  selected_workspaces: "{{ selected_workspaces }}"
          private_access:
            restriction_mode: "{{ restriction_mode }}"
            allow_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_private_access: {{ all_private_access }}
                  all_registered_endpoints: {{ all_registered_endpoints }}
                  azure_workspace_private_link: {{ azure_workspace_private_link }}
                  endpoints: "{{ endpoints }}"
            deny_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_private_access: {{ all_private_access }}
                  all_registered_endpoints: {{ all_registered_endpoints }}
                  azure_workspace_private_link: {{ azure_workspace_private_link }}
                  endpoints: "{{ endpoints }}"
          public_access:
            restriction_mode: "{{ restriction_mode }}"
            allow_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_ip_ranges: {{ all_ip_ranges }}
                  excluded_ip_ranges: "{{ excluded_ip_ranges }}"
                  included_ip_ranges: "{{ included_ip_ranges }}"
                  managed_ip_range: "{{ managed_ip_range }}"
            deny_rules:
              - authentication:
                  identities: "{{ identities }}"
                  identity_type: "{{ identity_type }}"
                destination:
                  account_api: "{{ account_api }}"
                  account_databricks_one: "{{ account_databricks_one }}"
                  account_ui: "{{ account_ui }}"
                  all_destinations: {{ all_destinations }}
                  apps_runtime: "{{ apps_runtime }}"
                  lakebase_runtime: "{{ lakebase_runtime }}"
                  workspace_api: "{{ workspace_api }}"
                  workspace_ui: "{{ workspace_ui }}"
                label: "{{ label }}"
                origin:
                  all_ip_ranges: {{ all_ip_ranges }}
                  excluded_ip_ranges: "{{ excluded_ip_ranges }}"
                  included_ip_ranges: "{{ included_ip_ranges }}"
                  managed_ip_range: "{{ managed_ip_range }}"
        network_policy_id: "{{ network_policy_id }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_network_policy_rpc"
    values={[
        { label: 'update_network_policy_rpc', value: 'update_network_policy_rpc' }
    ]}
>
<TabItem value="update_network_policy_rpc">

Updates a network policy. This allows you to modify the configuration of a network policy.

```sql
REPLACE databricks_account.settings.network_policies
SET 
network_policy = '{{ network_policy }}'
WHERE 
account_id = '{{ account_id }}' --required
AND network_policy_id = '{{ network_policy_id }}' --required
AND network_policy = '{{ network_policy }}' --required
RETURNING
account_id,
network_policy_id,
egress,
ingress,
ingress_dry_run;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_network_policy_rpc"
    values={[
        { label: 'delete_network_policy_rpc', value: 'delete_network_policy_rpc' }
    ]}
>
<TabItem value="delete_network_policy_rpc">

Deletes a network policy. Cannot be called on 'default-policy'.

```sql
DELETE FROM databricks_account.settings.network_policies
WHERE account_id = '{{ account_id }}' --required
AND network_policy_id = '{{ network_policy_id }}' --required
;
```
</TabItem>
</Tabs>
