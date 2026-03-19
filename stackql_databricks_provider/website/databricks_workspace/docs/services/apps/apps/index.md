---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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

Creates, updates, deletes, gets or lists an <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'apps_get_space', value: 'apps_get_space' },
        { label: 'apps_get_space_operation', value: 'apps_get_space_operation' },
        { label: 'list', value: 'list' },
        { label: 'apps_list_spaces', value: 'apps_list_spaces' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The unique identifier of the app."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_integration_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "active_deployment",
    "type": "object",
    "description": "The active deployment of the app. A deployment is considered active when it has been deployed to the app compute.",
    "children": [
      {
        "name": "command",
        "type": "array",
        "description": ""
      },
      {
        "name": "create_time",
        "type": "string",
        "description": "The creation time of the deployment. Formatted timestamp in ISO 6801."
      },
      {
        "name": "creator",
        "type": "string",
        "description": "The email of the user creates the deployment."
      },
      {
        "name": "deployment_artifacts",
        "type": "object",
        "description": "The deployment artifacts for an app.",
        "children": [
          {
            "name": "source_code_path",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
      },
      {
        "name": "env_vars",
        "type": "array",
        "description": "The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value for the environment variable."
          },
          {
            "name": "value_from",
            "type": "string",
            "description": "The name of an external Databricks resource that contains the value, such as a secret or a database table."
          }
        ]
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "Git repository to use as the source for the app deployment.",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": "Git branch to checkout."
          },
          {
            "name": "commit",
            "type": "string",
            "description": "Git commit SHA to checkout."
          },
          {
            "name": "git_repository",
            "type": "object",
            "description": "Git repository configuration. Populated from the app's git_repository configuration.",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": "URL of the Git repository."
              },
              {
                "name": "provider",
                "type": "string",
                "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
              }
            ]
          },
          {
            "name": "resolved_commit",
            "type": "string",
            "description": "The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time."
          },
          {
            "name": "source_code_path",
            "type": "string",
            "description": "Relative path to the app source code within the Git repository. If not specified, the root of the repository is used."
          },
          {
            "name": "tag",
            "type": "string",
            "description": "Git tag to checkout."
          }
        ]
      },
      {
        "name": "mode",
        "type": "string",
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
      },
      {
        "name": "source_code_path",
        "type": "string",
        "description": "The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment."
      },
      {
        "name": "status",
        "type": "object",
        "description": "Status and status message of the deployment",
        "children": [
          {
            "name": "message",
            "type": "string",
            "description": ""
          },
          {
            "name": "state",
            "type": "string",
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "app_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the application. (CRASHED, DEPLOYING, RUNNING, UNAVAILABLE)"
      }
    ]
  },
  {
    "name": "compute_size",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (LARGE, MEDIUM)"
  },
  {
    "name": "compute_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "active_instances",
        "type": "integer",
        "description": ""
      },
      {
        "name": "message",
        "type": "string",
        "description": "Compute status message"
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the app compute. (ACTIVE, DELETING, ERROR, STARTING, STOPPED, STOPPING, UPDATING)"
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The creation time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user that created the app."
  },
  {
    "name": "default_source_code_path",
    "type": "string",
    "description": "The default workspace file system path of the source code from which app deployment are created. This field tracks the workspace source code path of the last active deployment."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the app."
  },
  {
    "name": "effective_user_api_scopes",
    "type": "array",
    "description": "The effective api scopes granted to the user access token."
  },
  {
    "name": "git_repository",
    "type": "object",
    "description": "Git repository configuration for app deployments. When specified, deployments can reference code from this repository by providing only the git reference (branch, tag, or commit).",
    "children": [
      {
        "name": "url",
        "type": "string",
        "description": "URL of the Git repository."
      },
      {
        "name": "provider",
        "type": "string",
        "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
      }
    ]
  },
  {
    "name": "pending_deployment",
    "type": "object",
    "description": "The pending deployment of the app. A deployment is considered pending when it is being prepared for deployment to the app compute.",
    "children": [
      {
        "name": "command",
        "type": "array",
        "description": ""
      },
      {
        "name": "create_time",
        "type": "string",
        "description": "The creation time of the deployment. Formatted timestamp in ISO 6801."
      },
      {
        "name": "creator",
        "type": "string",
        "description": "The email of the user creates the deployment."
      },
      {
        "name": "deployment_artifacts",
        "type": "object",
        "description": "The deployment artifacts for an app.",
        "children": [
          {
            "name": "source_code_path",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
      },
      {
        "name": "env_vars",
        "type": "array",
        "description": "The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value for the environment variable."
          },
          {
            "name": "value_from",
            "type": "string",
            "description": "The name of an external Databricks resource that contains the value, such as a secret or a database table."
          }
        ]
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "Git repository to use as the source for the app deployment.",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": "Git branch to checkout."
          },
          {
            "name": "commit",
            "type": "string",
            "description": "Git commit SHA to checkout."
          },
          {
            "name": "git_repository",
            "type": "object",
            "description": "Git repository configuration. Populated from the app's git_repository configuration.",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": "URL of the Git repository."
              },
              {
                "name": "provider",
                "type": "string",
                "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
              }
            ]
          },
          {
            "name": "resolved_commit",
            "type": "string",
            "description": "The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time."
          },
          {
            "name": "source_code_path",
            "type": "string",
            "description": "Relative path to the app source code within the Git repository. If not specified, the root of the repository is used."
          },
          {
            "name": "tag",
            "type": "string",
            "description": "Git tag to checkout."
          }
        ]
      },
      {
        "name": "mode",
        "type": "string",
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
      },
      {
        "name": "source_code_path",
        "type": "string",
        "description": "The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment."
      },
      {
        "name": "status",
        "type": "object",
        "description": "Status and status message of the deployment",
        "children": [
          {
            "name": "message",
            "type": "string",
            "description": ""
          },
          {
            "name": "state",
            "type": "string",
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "resources",
    "type": "array",
    "description": "Resources for the app.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "app",
        "type": "object",
        "description": ""
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "postgres",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": ""
          },
          {
            "name": "database",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
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
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MODIFY, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          },
          {
            "name": "securable_kind",
            "type": "string",
            "description": "The securable kind from Unity Catalog. See https://docs.databricks.com/api/workspace/tables/get#securable_kind_manifest-securable_kind."
          }
        ]
      }
    ]
  },
  {
    "name": "space",
    "type": "string",
    "description": "Name of the space this app belongs to."
  },
  {
    "name": "telemetry_export_destinations",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "unity_catalog",
        "type": "object",
        "description": "Unity Catalog Destinations for OTEL telemetry export.",
        "children": [
          {
            "name": "logs_table",
            "type": "string",
            "description": "Unity Catalog table for OTEL logs."
          },
          {
            "name": "metrics_table",
            "type": "string",
            "description": "Unity Catalog table for OTEL metrics."
          },
          {
            "name": "traces_table",
            "type": "string",
            "description": "Unity Catalog table for OTEL traces (spans)."
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The update time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "updater",
    "type": "string",
    "description": "The email of the user that last updated the app."
  },
  {
    "name": "url",
    "type": "string",
    "description": "The URL of the app once it is deployed."
  },
  {
    "name": "user_api_scopes",
    "type": "array",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="apps_get_space">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The unique identifier of the app space."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The effective usage policy ID used by apps in the space."
  },
  {
    "name": "service_principal_client_id",
    "type": "string",
    "description": "The service principal client ID for the app space."
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": "The service principal ID for the app space."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The usage policy ID for managing cost at the space level."
  },
  {
    "name": "service_principal_name",
    "type": "string",
    "description": "The service principal name for the app space."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "The creation time of the app space. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user that created the app space."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the app space."
  },
  {
    "name": "effective_user_api_scopes",
    "type": "array",
    "description": "The effective api scopes granted to the user access token."
  },
  {
    "name": "resources",
    "type": "array",
    "description": "Resources for the app space. Resources configured at the space level are available to all apps in the space.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "app",
        "type": "object",
        "description": ""
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "postgres",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": ""
          },
          {
            "name": "database",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
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
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MODIFY, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          },
          {
            "name": "securable_kind",
            "type": "string",
            "description": "The securable kind from Unity Catalog. See https://docs.databricks.com/api/workspace/tables/get#securable_kind_manifest-securable_kind."
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The status of the app space.",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "The state of the app space. (SPACE_ACTIVE, SPACE_CREATING, SPACE_DELETED, SPACE_DELETING, SPACE_ERROR, SPACE_UPDATING)"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "The update time of the app space. Formatted timestamp in ISO 6801."
  },
  {
    "name": "updater",
    "type": "string",
    "description": "The email of the user that last updated the app space."
  },
  {
    "name": "user_api_scopes",
    "type": "array",
    "description": "OAuth scopes for apps in the space."
  }
]} />
</TabItem>
<TabItem value="apps_get_space_operation">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/&#123;unique_id&#125;`."
  },
  {
    "name": "done",
    "type": "boolean",
    "description": "If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available."
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
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The unique identifier of the app."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_integration_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "active_deployment",
    "type": "object",
    "description": "The active deployment of the app. A deployment is considered active when it has been deployed to the app compute.",
    "children": [
      {
        "name": "command",
        "type": "array",
        "description": ""
      },
      {
        "name": "create_time",
        "type": "string",
        "description": "The creation time of the deployment. Formatted timestamp in ISO 6801."
      },
      {
        "name": "creator",
        "type": "string",
        "description": "The email of the user creates the deployment."
      },
      {
        "name": "deployment_artifacts",
        "type": "object",
        "description": "The deployment artifacts for an app.",
        "children": [
          {
            "name": "source_code_path",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
      },
      {
        "name": "env_vars",
        "type": "array",
        "description": "The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value for the environment variable."
          },
          {
            "name": "value_from",
            "type": "string",
            "description": "The name of an external Databricks resource that contains the value, such as a secret or a database table."
          }
        ]
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "Git repository to use as the source for the app deployment.",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": "Git branch to checkout."
          },
          {
            "name": "commit",
            "type": "string",
            "description": "Git commit SHA to checkout."
          },
          {
            "name": "git_repository",
            "type": "object",
            "description": "Git repository configuration. Populated from the app's git_repository configuration.",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": "URL of the Git repository."
              },
              {
                "name": "provider",
                "type": "string",
                "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
              }
            ]
          },
          {
            "name": "resolved_commit",
            "type": "string",
            "description": "The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time."
          },
          {
            "name": "source_code_path",
            "type": "string",
            "description": "Relative path to the app source code within the Git repository. If not specified, the root of the repository is used."
          },
          {
            "name": "tag",
            "type": "string",
            "description": "Git tag to checkout."
          }
        ]
      },
      {
        "name": "mode",
        "type": "string",
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
      },
      {
        "name": "source_code_path",
        "type": "string",
        "description": "The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment."
      },
      {
        "name": "status",
        "type": "object",
        "description": "Status and status message of the deployment",
        "children": [
          {
            "name": "message",
            "type": "string",
            "description": ""
          },
          {
            "name": "state",
            "type": "string",
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "app_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the application. (CRASHED, DEPLOYING, RUNNING, UNAVAILABLE)"
      }
    ]
  },
  {
    "name": "compute_size",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (LARGE, MEDIUM)"
  },
  {
    "name": "compute_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "active_instances",
        "type": "integer",
        "description": ""
      },
      {
        "name": "message",
        "type": "string",
        "description": "Compute status message"
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the app compute. (ACTIVE, DELETING, ERROR, STARTING, STOPPED, STOPPING, UPDATING)"
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The creation time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user that created the app."
  },
  {
    "name": "default_source_code_path",
    "type": "string",
    "description": "The default workspace file system path of the source code from which app deployment are created. This field tracks the workspace source code path of the last active deployment."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the app."
  },
  {
    "name": "effective_user_api_scopes",
    "type": "array",
    "description": "The effective api scopes granted to the user access token."
  },
  {
    "name": "git_repository",
    "type": "object",
    "description": "Git repository configuration for app deployments. When specified, deployments can reference code from this repository by providing only the git reference (branch, tag, or commit).",
    "children": [
      {
        "name": "url",
        "type": "string",
        "description": "URL of the Git repository."
      },
      {
        "name": "provider",
        "type": "string",
        "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
      }
    ]
  },
  {
    "name": "pending_deployment",
    "type": "object",
    "description": "The pending deployment of the app. A deployment is considered pending when it is being prepared for deployment to the app compute.",
    "children": [
      {
        "name": "command",
        "type": "array",
        "description": ""
      },
      {
        "name": "create_time",
        "type": "string",
        "description": "The creation time of the deployment. Formatted timestamp in ISO 6801."
      },
      {
        "name": "creator",
        "type": "string",
        "description": "The email of the user creates the deployment."
      },
      {
        "name": "deployment_artifacts",
        "type": "object",
        "description": "The deployment artifacts for an app.",
        "children": [
          {
            "name": "source_code_path",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
      },
      {
        "name": "env_vars",
        "type": "array",
        "description": "The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value for the environment variable."
          },
          {
            "name": "value_from",
            "type": "string",
            "description": "The name of an external Databricks resource that contains the value, such as a secret or a database table."
          }
        ]
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "Git repository to use as the source for the app deployment.",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": "Git branch to checkout."
          },
          {
            "name": "commit",
            "type": "string",
            "description": "Git commit SHA to checkout."
          },
          {
            "name": "git_repository",
            "type": "object",
            "description": "Git repository configuration. Populated from the app's git_repository configuration.",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": "URL of the Git repository."
              },
              {
                "name": "provider",
                "type": "string",
                "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
              }
            ]
          },
          {
            "name": "resolved_commit",
            "type": "string",
            "description": "The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time."
          },
          {
            "name": "source_code_path",
            "type": "string",
            "description": "Relative path to the app source code within the Git repository. If not specified, the root of the repository is used."
          },
          {
            "name": "tag",
            "type": "string",
            "description": "Git tag to checkout."
          }
        ]
      },
      {
        "name": "mode",
        "type": "string",
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
      },
      {
        "name": "source_code_path",
        "type": "string",
        "description": "The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment."
      },
      {
        "name": "status",
        "type": "object",
        "description": "Status and status message of the deployment",
        "children": [
          {
            "name": "message",
            "type": "string",
            "description": ""
          },
          {
            "name": "state",
            "type": "string",
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "resources",
    "type": "array",
    "description": "Resources for the app.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "app",
        "type": "object",
        "description": ""
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "postgres",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": ""
          },
          {
            "name": "database",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
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
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MODIFY, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          },
          {
            "name": "securable_kind",
            "type": "string",
            "description": "The securable kind from Unity Catalog. See https://docs.databricks.com/api/workspace/tables/get#securable_kind_manifest-securable_kind."
          }
        ]
      }
    ]
  },
  {
    "name": "space",
    "type": "string",
    "description": "Name of the space this app belongs to."
  },
  {
    "name": "telemetry_export_destinations",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "unity_catalog",
        "type": "object",
        "description": "Unity Catalog Destinations for OTEL telemetry export.",
        "children": [
          {
            "name": "logs_table",
            "type": "string",
            "description": "Unity Catalog table for OTEL logs."
          },
          {
            "name": "metrics_table",
            "type": "string",
            "description": "Unity Catalog table for OTEL metrics."
          },
          {
            "name": "traces_table",
            "type": "string",
            "description": "Unity Catalog table for OTEL traces (spans)."
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The update time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "updater",
    "type": "string",
    "description": "The email of the user that last updated the app."
  },
  {
    "name": "url",
    "type": "string",
    "description": "The URL of the app once it is deployed."
  },
  {
    "name": "user_api_scopes",
    "type": "array",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="apps_list_spaces">

<SchemaTable fields={[
  {
    "name": "next_page_token",
    "type": "string",
    "description": ""
  },
  {
    "name": "spaces",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "create_time",
        "type": "string (date-time)",
        "description": "The creation time of the app space. Formatted timestamp in ISO 6801."
      },
      {
        "name": "creator",
        "type": "string",
        "description": "The email of the user that created the app space."
      },
      {
        "name": "description",
        "type": "string",
        "description": "The description of the app space."
      },
      {
        "name": "effective_usage_policy_id",
        "type": "string",
        "description": "The effective usage policy ID used by apps in the space."
      },
      {
        "name": "effective_user_api_scopes",
        "type": "array",
        "description": "The effective api scopes granted to the user access token."
      },
      {
        "name": "id",
        "type": "string",
        "description": "The unique identifier of the app space."
      },
      {
        "name": "resources",
        "type": "array",
        "description": "Resources for the app space. Resources configured at the space level are available to all apps in the space.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "app",
            "type": "object",
            "description": ""
          },
          {
            "name": "database",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "instance_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "database_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
              }
            ]
          },
          {
            "name": "description",
            "type": "string",
            "description": "Description of the App Resource."
          },
          {
            "name": "experiment",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "experiment_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
              }
            ]
          },
          {
            "name": "genie_space",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "space_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
              }
            ]
          },
          {
            "name": "job",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
              }
            ]
          },
          {
            "name": "postgres",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "branch",
                "type": "string",
                "description": ""
              },
              {
                "name": "database",
                "type": "string",
                "description": ""
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
              }
            ]
          },
          {
            "name": "secret",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "scope",
                "type": "string",
                "description": ""
              },
              {
                "name": "key",
                "type": "string",
                "description": "Key of the secret to grant permission on."
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
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
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
              }
            ]
          },
          {
            "name": "sql_warehouse",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
              }
            ]
          },
          {
            "name": "uc_securable",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "securable_full_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "securable_type",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
              },
              {
                "name": "permission",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MODIFY, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
              },
              {
                "name": "securable_kind",
                "type": "string",
                "description": "The securable kind from Unity Catalog. See https://docs.databricks.com/api/workspace/tables/get#securable_kind_manifest-securable_kind."
              }
            ]
          }
        ]
      },
      {
        "name": "service_principal_client_id",
        "type": "string",
        "description": "The service principal client ID for the app space."
      },
      {
        "name": "service_principal_id",
        "type": "integer",
        "description": "The service principal ID for the app space."
      },
      {
        "name": "service_principal_name",
        "type": "string",
        "description": "The service principal name for the app space."
      },
      {
        "name": "status",
        "type": "object",
        "description": "The status of the app space.",
        "children": [
          {
            "name": "message",
            "type": "string",
            "description": ""
          },
          {
            "name": "state",
            "type": "string",
            "description": "The state of the app space. (SPACE_ACTIVE, SPACE_CREATING, SPACE_DELETED, SPACE_DELETING, SPACE_ERROR, SPACE_UPDATING)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string (date-time)",
        "description": "The update time of the app space. Formatted timestamp in ISO 6801."
      },
      {
        "name": "updater",
        "type": "string",
        "description": "The email of the user that last updated the app space."
      },
      {
        "name": "usage_policy_id",
        "type": "string",
        "description": "The usage policy ID for managing cost at the space level."
      },
      {
        "name": "user_api_scopes",
        "type": "array",
        "description": "OAuth scopes for apps in the space."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves information for the app with the supplied name.</td>
</tr>
<tr>
    <td><a href="#apps_get_space"><CopyableCode code="apps_get_space" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves information for the app space with the supplied name.</td>
</tr>
<tr>
    <td><a href="#apps_get_space_operation"><CopyableCode code="apps_get_space_operation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets the status of an app space update operation.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-space"><code>space</code></a></td>
    <td>Lists all apps in the workspace.</td>
</tr>
<tr>
    <td><a href="#apps_list_spaces"><CopyableCode code="apps_list_spaces" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all app spaces in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-app"><code>app</code></a></td>
    <td><a href="#parameter-no_compute"><code>no_compute</code></a></td>
    <td>Creates a new app.</td>
</tr>
<tr>
    <td><a href="#apps_create_space"><CopyableCode code="apps_create_space" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-space"><code>space</code></a></td>
    <td></td>
    <td>Creates a new app space.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-app"><code>app</code></a></td>
    <td></td>
    <td>Updates the app with the supplied name.</td>
</tr>
<tr>
    <td><a href="#apps_update_space"><CopyableCode code="apps_update_space" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-space"><code>space</code></a></td>
    <td></td>
    <td>Updates an app space. The update process is asynchronous and the status of the update can be checked</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an app.</td>
</tr>
<tr>
    <td><a href="#apps_delete_space"><CopyableCode code="apps_delete_space" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes an app space.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Start the last active deployment of the app in the workspace.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Stops the active deployment of the app in the workspace.</td>
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
    <td>The name of the app.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The field mask must be a single string, with multiple fields separated by commas (no spaces). The field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g., `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only the entire collection field can be specified. Field names must exactly match the resource field names. A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API changes in the future.</td>
</tr>
<tr id="parameter-no_compute">
    <td><CopyableCode code="no_compute" /></td>
    <td><code>boolean</code></td>
    <td>If true, the app will not be started after creation.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of app spaces. Requests first page if absent.</td>
</tr>
<tr id="parameter-space">
    <td><CopyableCode code="space" /></td>
    <td><code>string</code></td>
    <td>Filter apps by app space name. When specified, only apps belonging to this space are returned.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'apps_get_space', value: 'apps_get_space' },
        { label: 'apps_get_space_operation', value: 'apps_get_space_operation' },
        { label: 'list', value: 'list' },
        { label: 'apps_list_spaces', value: 'apps_list_spaces' }
    ]}
>
<TabItem value="get">

Retrieves information for the app with the supplied name.

```sql
SELECT
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
space,
telemetry_export_destinations,
update_time,
updater,
url,
user_api_scopes
FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="apps_get_space">

Retrieves information for the app space with the supplied name.

```sql
SELECT
id,
name,
effective_usage_policy_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
create_time,
creator,
description,
effective_user_api_scopes,
resources,
status,
update_time,
updater,
user_api_scopes
FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="apps_get_space_operation">

Gets the status of an app space update operation.

```sql
SELECT
name,
done,
error,
metadata,
response
FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all apps in the workspace.

```sql
SELECT
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
space,
telemetry_export_destinations,
update_time,
updater,
url,
user_api_scopes
FROM databricks_workspace.apps.apps
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND space = '{{ space }}'
;
```
</TabItem>
<TabItem value="apps_list_spaces">

Lists all app spaces in the workspace.

```sql
SELECT
next_page_token,
spaces
FROM databricks_workspace.apps.apps
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'apps_create_space', value: 'apps_create_space' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new app.

```sql
INSERT INTO databricks_workspace.apps.apps (
app,
deployment_name,
no_compute
)
SELECT 
'{{ app }}' /* required */,
'{{ deployment_name }}',
'{{ no_compute }}'
RETURNING
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
space,
telemetry_export_destinations,
update_time,
updater,
url,
user_api_scopes
;
```
</TabItem>
<TabItem value="apps_create_space">

Creates a new app space.

```sql
INSERT INTO databricks_workspace.apps.apps (
space,
deployment_name
)
SELECT 
'{{ space }}' /* required */,
'{{ deployment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: apps
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the apps resource.
    - name: app
      value:
        name: "{{ name }}"
        active_deployment:
          command:
            - "{{ command }}"
          create_time: "{{ create_time }}"
          creator: "{{ creator }}"
          deployment_artifacts:
            source_code_path: "{{ source_code_path }}"
          deployment_id: "{{ deployment_id }}"
          env_vars:
            - name: "{{ name }}"
              value: "{{ value }}"
              value_from: "{{ value_from }}"
          git_source:
            branch: "{{ branch }}"
            commit: "{{ commit }}"
            git_repository:
              url: "{{ url }}"
              provider: "{{ provider }}"
            resolved_commit: "{{ resolved_commit }}"
            source_code_path: "{{ source_code_path }}"
            tag: "{{ tag }}"
          mode: "{{ mode }}"
          source_code_path: "{{ source_code_path }}"
          status:
            message: "{{ message }}"
            state: "{{ state }}"
          update_time: "{{ update_time }}"
        app_status:
          message: "{{ message }}"
          state: "{{ state }}"
        budget_policy_id: "{{ budget_policy_id }}"
        compute_size: "{{ compute_size }}"
        compute_status:
          active_instances: {{ active_instances }}
          message: "{{ message }}"
          state: "{{ state }}"
        create_time: "{{ create_time }}"
        creator: "{{ creator }}"
        default_source_code_path: "{{ default_source_code_path }}"
        description: "{{ description }}"
        effective_budget_policy_id: "{{ effective_budget_policy_id }}"
        effective_usage_policy_id: "{{ effective_usage_policy_id }}"
        effective_user_api_scopes:
          - "{{ effective_user_api_scopes }}"
        git_repository:
          url: "{{ url }}"
          provider: "{{ provider }}"
        id: "{{ id }}"
        oauth2_app_client_id: "{{ oauth2_app_client_id }}"
        oauth2_app_integration_id: "{{ oauth2_app_integration_id }}"
        pending_deployment:
          command:
            - "{{ command }}"
          create_time: "{{ create_time }}"
          creator: "{{ creator }}"
          deployment_artifacts:
            source_code_path: "{{ source_code_path }}"
          deployment_id: "{{ deployment_id }}"
          env_vars:
            - name: "{{ name }}"
              value: "{{ value }}"
              value_from: "{{ value_from }}"
          git_source:
            branch: "{{ branch }}"
            commit: "{{ commit }}"
            git_repository:
              url: "{{ url }}"
              provider: "{{ provider }}"
            resolved_commit: "{{ resolved_commit }}"
            source_code_path: "{{ source_code_path }}"
            tag: "{{ tag }}"
          mode: "{{ mode }}"
          source_code_path: "{{ source_code_path }}"
          status:
            message: "{{ message }}"
            state: "{{ state }}"
          update_time: "{{ update_time }}"
        resources:
          - name: "{{ name }}"
            app: "{{ app }}"
            database:
              instance_name: "{{ instance_name }}"
              database_name: "{{ database_name }}"
              permission: "{{ permission }}"
            description: "{{ description }}"
            experiment:
              experiment_id: "{{ experiment_id }}"
              permission: "{{ permission }}"
            genie_space:
              name: "{{ name }}"
              space_id: "{{ space_id }}"
              permission: "{{ permission }}"
            job:
              id: "{{ id }}"
              permission: "{{ permission }}"
            postgres:
              branch: "{{ branch }}"
              database: "{{ database }}"
              permission: "{{ permission }}"
            secret:
              scope: "{{ scope }}"
              key: "{{ key }}"
              permission: "{{ permission }}"
            serving_endpoint:
              name: "{{ name }}"
              permission: "{{ permission }}"
            sql_warehouse:
              id: "{{ id }}"
              permission: "{{ permission }}"
            uc_securable:
              securable_full_name: "{{ securable_full_name }}"
              securable_type: "{{ securable_type }}"
              permission: "{{ permission }}"
              securable_kind: "{{ securable_kind }}"
        service_principal_client_id: "{{ service_principal_client_id }}"
        service_principal_id: {{ service_principal_id }}
        service_principal_name: "{{ service_principal_name }}"
        space: "{{ space }}"
        telemetry_export_destinations:
          - unity_catalog:
              logs_table: "{{ logs_table }}"
              metrics_table: "{{ metrics_table }}"
              traces_table: "{{ traces_table }}"
        update_time: "{{ update_time }}"
        updater: "{{ updater }}"
        url: "{{ url }}"
        usage_policy_id: "{{ usage_policy_id }}"
        user_api_scopes:
          - "{{ user_api_scopes }}"
    - name: space
      value:
        name: "{{ name }}"
        create_time: "{{ create_time }}"
        creator: "{{ creator }}"
        description: "{{ description }}"
        effective_usage_policy_id: "{{ effective_usage_policy_id }}"
        effective_user_api_scopes:
          - "{{ effective_user_api_scopes }}"
        id: "{{ id }}"
        resources:
          - name: "{{ name }}"
            app: "{{ app }}"
            database:
              instance_name: "{{ instance_name }}"
              database_name: "{{ database_name }}"
              permission: "{{ permission }}"
            description: "{{ description }}"
            experiment:
              experiment_id: "{{ experiment_id }}"
              permission: "{{ permission }}"
            genie_space:
              name: "{{ name }}"
              space_id: "{{ space_id }}"
              permission: "{{ permission }}"
            job:
              id: "{{ id }}"
              permission: "{{ permission }}"
            postgres:
              branch: "{{ branch }}"
              database: "{{ database }}"
              permission: "{{ permission }}"
            secret:
              scope: "{{ scope }}"
              key: "{{ key }}"
              permission: "{{ permission }}"
            serving_endpoint:
              name: "{{ name }}"
              permission: "{{ permission }}"
            sql_warehouse:
              id: "{{ id }}"
              permission: "{{ permission }}"
            uc_securable:
              securable_full_name: "{{ securable_full_name }}"
              securable_type: "{{ securable_type }}"
              permission: "{{ permission }}"
              securable_kind: "{{ securable_kind }}"
        service_principal_client_id: "{{ service_principal_client_id }}"
        service_principal_id: {{ service_principal_id }}
        service_principal_name: "{{ service_principal_name }}"
        status:
          message: "{{ message }}"
          state: "{{ state }}"
        update_time: "{{ update_time }}"
        updater: "{{ updater }}"
        usage_policy_id: "{{ usage_policy_id }}"
        user_api_scopes:
          - "{{ user_api_scopes }}"
    - name: no_compute
      value: {{ no_compute }}
      description: If true, the app will not be started after creation.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'apps_update_space', value: 'apps_update_space' }
    ]}
>
<TabItem value="update">

Updates the app with the supplied name.

```sql
UPDATE databricks_workspace.apps.apps
SET 
app = '{{ app }}'
WHERE 
name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND app = '{{ app }}' --required
RETURNING
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
space,
telemetry_export_destinations,
update_time,
updater,
url,
user_api_scopes;
```
</TabItem>
<TabItem value="apps_update_space">

Updates an app space. The update process is asynchronous and the status of the update can be checked

```sql
UPDATE databricks_workspace.apps.apps
SET 
space = '{{ space }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND space = '{{ space }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'apps_delete_space', value: 'apps_delete_space' }
    ]}
>
<TabItem value="delete">

Deletes an app.

```sql
DELETE FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="apps_delete_space">

Deletes an app space.

```sql
DELETE FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Start the last active deployment of the app in the workspace.

```sql
EXEC databricks_workspace.apps.apps.start 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops the active deployment of the app in the workspace.

```sql
EXEC databricks_workspace.apps.apps.stop 
@name='{{ name }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
