---
title: job_run_output
hide_title: false
hide_table_of_contents: false
keywords:
  - job_run_output
  - jobs
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

Creates, updates, deletes, gets or lists a <code>job_run_output</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_run_output" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.jobs.job_run_output" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_output"
    values={[
        { label: 'get_output', value: 'get_output' }
    ]}
>
<TabItem value="get_output">

<SchemaTable fields={[
  {
    "name": "agentic_task_output",
    "type": "object",
    "description": "The output of an agentic task, if available",
    "children": [
      {
        "name": "conversation_id",
        "type": "string",
        "description": "The conversation ID generated during this task execution."
      },
      {
        "name": "created_at",
        "type": "number",
        "description": "Deprecated. Run timestamps are exposed on the surrounding job-run."
      },
      {
        "name": "genie_code",
        "type": "object",
        "description": "Genie Code execution output (conversation notebook reference).",
        "children": [
          {
            "name": "thread_id",
            "type": "string",
            "description": "Identifier of the Genie Code conversation thread for this run. In Genie Code, threads are backed by workspace notebooks, so this value also identifies the notebook a UI can deep-link to for the conversation transcript."
          }
        ]
      },
      {
        "name": "id",
        "type": "string",
        "description": "Deprecated. Run-level identity already lives on the surrounding ``RunOutput``; ``SupervisorOutput.response_id`` is the canonical handle for the structured response."
      },
      {
        "name": "response",
        "type": "string",
        "description": "Deprecated. The final text response is now surfaced in ``task_output[\"response\"]``; new callers should read it from there."
      },
      {
        "name": "status",
        "type": "string",
        "description": "Deprecated. Run lifecycle state is exposed on the surrounding job-run."
      },
      {
        "name": "supervisor",
        "type": "object",
        "description": "Supervisor (tile or inlined) execution output.",
        "children": [
          {
            "name": "response_id",
            "type": "string",
            "description": "The Responses-API ``response.id`` produced by the supervisor. Use this ID with the Responses API to fetch the full structured response (assistant messages, function calls, function-call outputs)."
          }
        ]
      },
      {
        "name": "task_output",
        "type": "object",
        "description": "Custom output values from the agent. When the caller specified a ``task_output_schema`` / ``output_schema``, this carries those user-defined keys. When no schema is specified, this carries default supervisor keys (``response``, ``truncated``, ...)."
      }
    ]
  },
  {
    "name": "ai_runtime_task_output",
    "type": "object",
    "description": "The output of an AiRuntimeTask, if available — MLflow identifiers, artifact paths, and per-replica allocated compute. Run lifecycle / termination status lives on the surrounding framework ``RunTask.status`` (``runs.proto:RunTask.status`` of type ``RunStatus``), not on this output. See ``tasks/genai/ai_runtime_task.proto:AiRuntimeTaskOutput``.",
    "children": [
      {
        "name": "mlflow_experiment_id",
        "type": "string",
        "description": "MLflow experiment ID the run was logged to. Use it to look up the experiment in MLflow APIs or the workspace MLflow UI."
      },
      {
        "name": "mlflow_run_id",
        "type": "string",
        "description": "MLflow run ID for this task execution. Use it to look up the run in MLflow APIs or the workspace MLflow UI."
      },
      {
        "name": "status_message",
        "type": "string",
        "description": "Human-readable status message for this run, suitable for display to the user (for example, that the run is still waiting for GPU compute). Set by the server only when there is something to surface; empty otherwise."
      }
    ]
  },
  {
    "name": "alert_output",
    "type": "object",
    "description": "The output of an alert task, if available",
    "children": [
      {
        "name": "alert_state",
        "type": "string",
        "description": "Same alert evaluation state as in redash-v2/api/proto/alertsv2/alerts.proto (ERROR, OK, TRIGGERED, UNKNOWN)"
      }
    ]
  },
  {
    "name": "clean_rooms_notebook_output",
    "type": "object",
    "description": "The output of a clean rooms notebook task, if available",
    "children": [
      {
        "name": "clean_room_job_run_state",
        "type": "object",
        "description": "Stores the run state of the clean rooms notebook task.",
        "children": [
          {
            "name": "life_cycle_state",
            "type": "string",
            "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases. (BLOCKED, INTERNAL_ERROR, PENDING, QUEUED, RUNNING, RUN_LIFE_CYCLE_STATE_UNSPECIFIED, SKIPPED, TERMINATED, TERMINATING, WAITING_FOR_RETRY)"
          },
          {
            "name": "result_state",
            "type": "string",
            "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases. (CANCELED, DISABLED, EVICTED, EXCLUDED, FAILED, MAXIMUM_CONCURRENT_RUNS_REACHED, RUN_RESULT_STATE_UNSPECIFIED, SUCCESS, SUCCESS_WITH_FAILURES, TIMEDOUT, UPSTREAM_CANCELED, UPSTREAM_EVICTED, UPSTREAM_FAILED)"
          }
        ]
      },
      {
        "name": "notebook_output",
        "type": "object",
        "description": "The notebook output for the clean room run",
        "children": [
          {
            "name": "result",
            "type": "string",
            "description": ""
          },
          {
            "name": "truncated",
            "type": "boolean",
            "description": "Whether or not the result was truncated."
          }
        ]
      },
      {
        "name": "output_schema_info",
        "type": "object",
        "description": "Information on how to access the output schema for the clean room run",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "expiration_time",
            "type": "integer",
            "description": "The expiration time for the output schema as a Unix timestamp in milliseconds."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "shared_output_schema_info",
        "type": "object",
        "description": "Information on how to access the shared output schema for the clean room run",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "expiration_time",
            "type": "integer",
            "description": "The expiration time for the output schema as a Unix timestamp in milliseconds."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "dashboard_output",
    "type": "object",
    "description": "The output of a dashboard task, if available",
    "children": [
      {
        "name": "page_snapshots",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "page_display_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "widget_error_details",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "message",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "dbt_cloud_output",
    "type": "object",
    "description": "Deprecated in favor of the new dbt_platform_output",
    "children": [
      {
        "name": "dbt_cloud_job_run_id",
        "type": "integer",
        "description": "Id of the job run in dbt Cloud"
      },
      {
        "name": "dbt_cloud_job_run_output",
        "type": "array",
        "description": "Steps of the job run as received from dbt Cloud",
        "children": [
          {
            "name": "index",
            "type": "integer",
            "description": "Orders the steps in the job"
          },
          {
            "name": "logs",
            "type": "string",
            "description": "Output of the step"
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the step in the job"
          },
          {
            "name": "status",
            "type": "string",
            "description": "State of the step (CANCELLED, ERROR, QUEUED, RUNNING, STARTING, SUCCESS)"
          }
        ]
      },
      {
        "name": "dbt_cloud_job_run_url",
        "type": "string",
        "description": "Url where full run details can be viewed"
      }
    ]
  },
  {
    "name": "dbt_output",
    "type": "object",
    "description": "The output of a dbt task, if available.",
    "children": [
      {
        "name": "artifacts_headers",
        "type": "object",
        "description": ""
      },
      {
        "name": "artifacts_link",
        "type": "string",
        "description": "A pre-signed URL to download the (compressed) dbt artifacts. This link is valid for a limited time (30 minutes). This information is only available after the run has finished."
      }
    ]
  },
  {
    "name": "dbt_platform_output",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "dbt_platform_job_run_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "dbt_platform_job_run_output",
        "type": "array",
        "description": "Steps of the job run as received from dbt platform",
        "children": [
          {
            "name": "index",
            "type": "integer",
            "description": "Orders the steps in the job"
          },
          {
            "name": "logs",
            "type": "string",
            "description": "Output of the step"
          },
          {
            "name": "logs_truncated",
            "type": "boolean",
            "description": "Whether the logs of this step have been truncated. If true, the logs has been truncated to 10000 characters."
          },
          {
            "name": "name",
            "type": "string",
            "description": "Name of the step in the job"
          },
          {
            "name": "name_truncated",
            "type": "boolean",
            "description": "Whether the name of the job has been truncated. If true, the name has been truncated to 100 characters."
          },
          {
            "name": "status",
            "type": "string",
            "description": "State of the step (CANCELLED, ERROR, QUEUED, RUNNING, STARTING, SUCCESS)"
          }
        ]
      },
      {
        "name": "dbt_platform_job_run_url",
        "type": "string",
        "description": "Url where full run details can be viewed"
      },
      {
        "name": "steps_truncated",
        "type": "boolean",
        "description": "Whether the number of steps in the output has been truncated. If true, the output will contain the first 20 steps of the output."
      }
    ]
  },
  {
    "name": "error",
    "type": "string",
    "description": "An error message indicating why a task failed or why output is not available. The message is unstructured, and its exact format is subject to change."
  },
  {
    "name": "error_trace",
    "type": "string",
    "description": "If there was an error executing the run, this field contains any available stack traces."
  },
  {
    "name": "genie_task_output",
    "type": "object",
    "description": "The output of a Genie task, if available",
    "children": [
      {
        "name": "conversation_id",
        "type": "string",
        "description": "The conversation ID of the agent run, used to retrieve the full conversation history and results."
      }
    ]
  },
  {
    "name": "info",
    "type": "string",
    "description": ""
  },
  {
    "name": "logs",
    "type": "string",
    "description": "The output from tasks that write to standard streams (stdout/stderr) such as spark_jar_task, spark_python_task, python_wheel_task. It's not supported for the notebook_task, pipeline_task or spark_submit_task. Databricks restricts this API to return the last 5 MB of these logs."
  },
  {
    "name": "logs_truncated",
    "type": "boolean",
    "description": "Whether the logs are truncated."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Run was retrieved successfully",
    "children": [
      {
        "name": "attempt_number",
        "type": "integer",
        "description": "The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0. If the initial run attempt fails, and the job has a retry policy (``max_retries`` &gt; 0), subsequent runs are created with an ``original_attempt_run_id`` of the original attempt’s ID and an incrementing ``attempt_number``. Runs are retried only until they succeed, and the maximum ``attempt_number`` is the same as the ``max_retries`` value for the job."
      },
      {
        "name": "cleanup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``cleanup_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
      },
      {
        "name": "cluster_instance",
        "type": "object",
        "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
        "children": [
          {
            "name": "cluster_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "spark_context_id",
            "type": "string",
            "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to ``/#setting/sparkui/$cluster_id/$spark_context_id``. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
          }
        ]
      },
      {
        "name": "cluster_spec",
        "type": "object",
        "description": "A snapshot of the job’s cluster specification when this run was created.",
        "children": [
          {
            "name": "existing_cluster_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "job_cluster_key",
            "type": "string",
            "description": "If job_cluster_key, this task is executed reusing the cluster specified in ``job.settings.job_clusters``."
          },
          {
            "name": "libraries",
            "type": "string",
            "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
          },
          {
            "name": "new_cluster",
            "type": "string",
            "description": "If new_cluster, a description of a new cluster that is created for each run."
          }
        ]
      },
      {
        "name": "creator_user_name",
        "type": "string",
        "description": "The creator user name. This field won’t be included in the response if the user has already been deleted."
      },
      {
        "name": "deployment_id",
        "type": "string",
        "description": "ID of the deployment that produced the job when this run was created. Used to look up deployment metadata from the Deployment Metadata service. Only set for job runs of jobs with a ``BUNDLE`` deployment."
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the run"
      },
      {
        "name": "effective_performance_target",
        "type": "string",
        "description": "The actual performance target used by the serverless run during execution. This can differ from the client-set performance target on the request depending on whether the performance mode is supported by the job type. - ``STANDARD``: Enables cost-efficient execution of serverless workloads. - ``PERFORMANCE_OPTIMIZED``: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance. (PERFORMANCE_OPTIMIZED, STANDARD)"
      },
      {
        "name": "effective_usage_policy_id",
        "type": "string",
        "description": "The id of the usage policy used by this run for cost attribution purposes."
      },
      {
        "name": "end_time",
        "type": "integer",
        "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
      },
      {
        "name": "environment_variables",
        "type": "array",
        "description": "Snapshot of ``JobSettings.environment_variables`` as it was at run launch — the full list of named env-var profiles the job defined. Per-profile resolved contents are not preserved here; only the customer-defined ``variables`` and ``files`` paths. To find which profile a given task ran with, look at ``RunTaskSettings.environment_variables_key``.",
        "children": [
          {
            "name": "environment_variables_key",
            "type": "string",
            "description": "Identifier for this entry. Must be unique within ``JobSettings.environment_variables``. Tasks reference it from ``TaskSettings.environment_variables_key``."
          },
          {
            "name": "files",
            "type": "array",
            "description": "Workspace (``/Workspace/...``) or UC Volumes (``/Volumes/...``) paths to ``.env`` files. Maximum 5 files. Files are read, parsed, and merged at task execution time, not at job creation or update API call time. File format: each line must be exactly ``KEY=VALUE``. Keys must match the same regex as inlined variable names (``^[A-Za-z_][A-Za-z0-9_]*$``); the value continues to the end of the line. No other syntax is supported — no comments, no quoted values, no escape sequences, no variable interpolation. Any line that does not match the ``KEY=VALUE`` shape fails the run. Size limits: maximum 1,048,576 bytes (1 MiB) per file on disk; maximum 131,072 bytes (128 KiB) per ``KEY=VALUE`` line combined. Caps are enforced at read time in jobs-runner — files exceeding the per-file cap, or lines exceeding the per-line cap, fail the run. On a duplicate key, the later file wins; ``variables`` override values from any file. Values may contain &#123;&#123;secrets/scope/key&#125;&#125; references; those are resolved at task execution time and never persisted in resolved form. Do not use these files to store raw secret values; consult `secret management <https://docs.databricks.com/aws/en/security/secrets/>`__ for the right way to pass sensitive values."
          },
          {
            "name": "variables",
            "type": "object",
            "description": "Environment variables specified directly as key/value pairs (as opposed to ``files``, which are read from ``.env`` file paths). Maximum 100 entries. Each key must match ``^[A-Za-z_][A-Za-z0-9_]*$`` and be 1 to 256 characters long. Each value is up to 512 characters; larger values should be moved into a ``.env`` file referenced from ``files``. On a duplicate key, ``variables`` override values from any file in ``files``. Values may contain &#123;&#123;secrets/scope/key&#125;&#125; references; those are resolved at task execution time and never persisted in resolved form. Do not use this field to store a raw secret value; consult `secret management <https://docs.databricks.com/aws/en/security/secrets/>`__ for the right way to pass sensitive values."
          }
        ]
      },
      {
        "name": "execution_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``execution_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
      },
      {
        "name": "git_source",
        "type": "object",
        "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If ``git_source`` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting ``source`` to ``WORKSPACE`` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, ``git_source`` must be defined on the job.",
        "children": [
          {
            "name": "git_url",
            "type": "string",
            "description": "URL of the repository to be cloned by this job."
          },
          {
            "name": "git_provider",
            "type": "string",
            "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive. (awsCodeCommit, azureDevOpsServices, bitbucketCloud, bitbucketServer, gitHub, gitHubEnterprise, gitLab, gitLabEnterpriseEdition)"
          },
          {
            "name": "git_branch",
            "type": "string",
            "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
          },
          {
            "name": "git_commit",
            "type": "string",
            "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
          },
          {
            "name": "git_snapshot",
            "type": "object",
            "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs.",
            "children": [
              {
                "name": "used_commit",
                "type": "string",
                "description": "Commit that was used to execute the run. If git_branch was specified, this points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the tag points to."
              }
            ]
          },
          {
            "name": "git_tag",
            "type": "string",
            "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
          },
          {
            "name": "job_source",
            "type": "object",
            "description": "The source of the job specification in the remote repository when the job is source controlled.",
            "children": [
              {
                "name": "job_config_path",
                "type": "string",
                "description": "Path of the job YAML file that contains the job specification."
              },
              {
                "name": "import_from_git_branch",
                "type": "string",
                "description": "Name of the branch which the job is imported from."
              },
              {
                "name": "dirty_state",
                "type": "string",
                "description": "Dirty state indicates the job is not fully synced with the job specification in the remote repository. Possible values are: - ``NOT_SYNCED``: The job is not yet synced with the remote job specification. Import the remote job specification from UI to make the job fully synced. - ``DISCONNECTED``: The job is temporary disconnected from the remote job specification and is allowed for live edit. Import the remote job specification again from UI to make the job fully synced. (DISCONNECTED, NOT_SYNCED)"
              }
            ]
          },
          {
            "name": "sparse_checkout",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "patterns",
                "type": "array",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "has_more",
        "type": "boolean",
        "description": "Indicates if the run has more array properties (``tasks``, ``job_clusters``) that are not shown. They can be accessed via :method:jobs/getrun endpoint. It is only relevant for API 2.2 :method:jobs/listruns requests with ``expand_tasks=true``."
      },
      {
        "name": "iterations",
        "type": "array",
        "description": "Only populated by for-each iterations. The parent for-each task is located in tasks array.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": "A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset."
          },
          {
            "name": "agentic_task",
            "type": "object",
            "description": "Agentic Task for job-based multi-agent execution",
            "children": [
              {
                "name": "context",
                "type": "object",
                "description": "Optional. Context input providing conversation history and instructions."
              },
              {
                "name": "genie_code_api",
                "type": "object",
                "description": "Inline Genie Code conversation driven by a single prompt. Mutually exclusive with the supervisor variants."
              },
              {
                "name": "goal",
                "type": "string",
                "description": "Deprecated. Use ``input`` (field 7) instead. Kept for backwards compatibility with existing callers; will be removed in a future revision."
              },
              {
                "name": "input",
                "type": "string",
                "description": "Optional. The user query / task input the agent must accomplish. Mirrors the OpenAI Responses API ``input`` field. Replaces the deprecated ``goal`` field; new callers should populate ``input`` going forward."
              },
              {
                "name": "output_schema",
                "type": "object",
                "description": "Optional. JSON-Schema-style declaration of the structured output the agent should produce. Replaces the deprecated ``task_output_schema`` map; new callers should populate ``output_schema`` going forward."
              },
              {
                "name": "supervisor_agent",
                "type": "object",
                "description": "A Supervisor Agent that orchestrates sub-agents and tools, referenced by tile_id."
              },
              {
                "name": "supervisor_api",
                "type": "object",
                "description": "Inlined Responses-API supervisor configuration (model + instructions + tools). Mutually exclusive with ``supervisor_agent``."
              },
              {
                "name": "task_output_schema",
                "type": "object",
                "description": "Deprecated. Use ``output_schema`` (field 8) instead. Kept for backwards compatibility with existing callers; will be removed in a future revision."
              },
              {
                "name": "trace_destination",
                "type": "object",
                "description": "Optional. Where MLflow traces produced by this task run should be persisted. When unset, traces follow the workspace default destination."
              }
            ]
          },
          {
            "name": "ai_runtime_task",
            "type": "object",
            "description": "The task runs a multi-gpu compute workload on Databricks AI Runtime. Specify the accelerator type and count, the command to run, and where the workload's code and MLflow output are stored.",
            "children": [
              {
                "name": "experiment",
                "type": "string",
                "description": "MLflow experiment name for this run. If an experiment with this name already exists under the calling user, the run is appended to it; otherwise a new experiment is created. To target a specific MLflow storage location (for example, when running as a service principal), set ``mlflow_experiment_directory``."
              },
              {
                "name": "deployments",
                "type": "array",
                "description": "Deployment specs for this task. Exactly one deployment is currently supported (a single entry where every node runs the same command); this is a current-Preview constraint. Role-split workloads (driver + worker, parameter server, separate eval node, etc.) with multiple entries are the eventual intent but not yet supported."
              },
              {
                "name": "code_source_path",
                "type": "string",
                "description": "Workspace or UC volume path of the code-source archive, unpacked on each node and exposed through ``$CODE_SOURCE``. Set by first-party tooling; not for direct callers."
              },
              {
                "name": "docker_image_url",
                "type": "string",
                "description": "Optional Docker image URL for a custom container image. When set, the task runs on the specified container image instead of the default Databricks client image. Format: ``&#123;organization&#125;/&#123;repository&#125;:&#123;tag&#125;``"
              },
              {
                "name": "mlflow_experiment_directory",
                "type": "string",
                "description": "Optional workspace directory under which the MLflow experiment named in ``experiment`` is created. Must start with ``/Workspace``. Set this when running as a service principal that has no default user directory; for regular users the experiment defaults to the user's home directory."
              },
              {
                "name": "mlflow_run",
                "type": "string",
                "description": "Optional display name for the MLflow run created under ``experiment``. If omitted, MLflow generates a default name."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Optional named parameters passed to each deployment's command. Keys are parameter names, values the corresponding arguments (for example, ``&#123;\"epochs\": \"3\", \"dataset\": \"s3://bucket/train\"&#125;``). Values may contain dynamic references such as ``&#123;&#123;job.trigger.time.iso_date&#125;&#125;`` or ``&#123;&#123;tasks.&lt;task_key&gt;.values.&lt;name&gt;&#125;&#125;``, which Jobs substitutes before execution (see ``AiRuntimeTaskResolvedValues.parameters`` in runs.proto)."
              }
            ]
          },
          {
            "name": "alert_task",
            "type": "object",
            "description": "The task evaluates a Databricks alert and sends notifications to subscribers when the ``alert_task`` field is present.",
            "children": [
              {
                "name": "alert_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Per-run parameter overrides, keyed by parameter name, applied onto the alert's stored query parameters before the query is executed. Only scalar values are supported. Values may reference job parameters with ``&#123;&#123;job.parameters.*&#125;&#125;``, which are resolved before the task runs. An override whose key does not match a stored parameter fails the task run. Limited to 10000 characters when serialized as JSON; keys must be 1-100 characters and contain only letters, digits, underscores, dashes, and periods."
              },
              {
                "name": "subscribers",
                "type": "array",
                "description": "The subscribers receive alert evaluation result notifications after the alert task is completed. The number of subscriptions is limited to 100."
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "The warehouse_id identifies the warehouse settings used by the alert task."
              },
              {
                "name": "workspace_path",
                "type": "string",
                "description": "The workspace_path is the path to the alert file in the workspace. The path: - must start with \"/Workspace\" - must be a normalized path. User has to select only one of alert_id or workspace_path to identify the alert."
              }
            ]
          },
          {
            "name": "attempt_number",
            "type": "integer",
            "description": "The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0. If the initial run attempt fails, and the job has a retry policy (``max_retries`` &gt; 0), subsequent runs are created with an ``original_attempt_run_id`` of the original attempt’s ID and an incrementing ``attempt_number``. Runs are retried only until they succeed, and the maximum ``attempt_number`` is the same as the ``max_retries`` value for the job."
          },
          {
            "name": "clean_rooms_notebook_task",
            "type": "object",
            "description": "The task runs a `clean rooms <https://docs.databricks.com/clean-rooms/index.html>`__ notebook when the ``clean_rooms_notebook_task`` field is present.",
            "children": [
              {
                "name": "clean_room_name",
                "type": "string",
                "description": "The clean room that the notebook belongs to."
              },
              {
                "name": "notebook_name",
                "type": "string",
                "description": "Name of the notebook being run."
              },
              {
                "name": "etag",
                "type": "string",
                "description": "Checksum to validate the freshness of the notebook resource (i.e. the notebook being run is the latest version). It can be fetched by calling the :method:cleanroomassets/get API."
              },
              {
                "name": "notebook_base_parameters",
                "type": "object",
                "description": "Base parameters to be used for the clean room notebook job."
              }
            ]
          },
          {
            "name": "cleanup_duration",
            "type": "integer",
            "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``cleanup_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
          },
          {
            "name": "cluster_instance",
            "type": "object",
            "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
            "children": [
              {
                "name": "cluster_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "spark_context_id",
                "type": "string",
                "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to ``/#setting/sparkui/$cluster_id/$spark_context_id``. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
              }
            ]
          },
          {
            "name": "compute",
            "type": "object",
            "description": "Task level compute configuration.",
            "children": [
              {
                "name": "hardware_accelerator",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "condition_task",
            "type": "object",
            "description": "The task evaluates a condition that can be used to control the execution of other tasks when the ``condition_task`` field is present. The condition task does not require a cluster to execute and does not support retries or notifications.",
            "children": [
              {
                "name": "op",
                "type": "string",
                "description": "- ``EQUAL_TO``, ``NOT_EQUAL`` operators perform string comparison of their operands. This means<br />  that ``“12.0” == “12”`` will evaluate to ``false``.<br />- ``GREATER_THAN``, ``GREATER_THAN_OR_EQUAL``, ``LESS_THAN``, ``LESS_THAN_OR_EQUAL`` operators<br />  perform numeric comparison of their operands. ``“12.0” &gt;= “12”`` will evaluate to<br />  ``true``, ``“10.0” &gt;= “12”`` will evaluate to ``false``.<br /><br />The boolean comparison to task values can be implemented with operators ``EQUAL_TO``,<br />``NOT_EQUAL``. If a task value was set to a boolean value, it will be serialized to<br />``“true”`` or ``“false”`` for the comparison. (EQUAL_TO, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
              },
              {
                "name": "left",
                "type": "string",
                "description": "The left operand of the condition task. Can be either a string value or a job state or parameter reference."
              },
              {
                "name": "right",
                "type": "string",
                "description": "The right operand of the condition task. Can be either a string value or a job state or parameter reference."
              },
              {
                "name": "outcome",
                "type": "string",
                "description": "The condition expression evaluation result. Filled in if the task was successfully completed. Can be ``\"true\"`` or ``\"false\"``"
              }
            ]
          },
          {
            "name": "dashboard_task",
            "type": "object",
            "description": "The task refreshes a dashboard and sends a snapshot to subscribers.",
            "children": [
              {
                "name": "dashboard_id",
                "type": "string",
                "description": "The identifier of the dashboard to refresh."
              },
              {
                "name": "filters",
                "type": "object",
                "description": "Dashboard task parameters. Used to apply dashboard filter values during dashboard task execution. Parameter values get applied to any dashboard filters that have a matching URL identifier as the parameter key. The parameter value format is dependent on the filter type: - For text and single-select filters, provide a single value (e.g. ``\"value\"``) - For date and datetime filters, provide the value in ISO 8601 format (e.g. ``\"2000-01-01T00:00:00\"``) - For multi-select filters, provide a JSON array of values (e.g. ``\"[\\\"value1\\\",\\\"value2\\\"]\"``) - For range and date range filters, provide a JSON object with ``start`` and ``end`` (e.g. ``\"&#123;\\\"start\\\":\\\"1\\\",\\\"end\\\":\\\"10\\\"&#125;\"``)"
              },
              {
                "name": "subscription",
                "type": "object",
                "description": "Optional: subscription configuration for sending the dashboard snapshot."
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "Optional: The warehouse id to execute the dashboard with for the schedule. If not specified, the default warehouse of the dashboard will be used."
              }
            ]
          },
          {
            "name": "dbt_cloud_task",
            "type": "object",
            "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task",
            "children": [
              {
                "name": "connection_resource_name",
                "type": "string",
                "description": "The resource name of the UC connection that authenticates the dbt Cloud for this task"
              },
              {
                "name": "dbt_cloud_job_id",
                "type": "integer",
                "description": "Id of the dbt Cloud job to be triggered"
              }
            ]
          },
          {
            "name": "dbt_platform_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "connection_resource_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "dbt_platform_job_id",
                "type": "string",
                "description": "Id of the dbt platform job to be triggered. Specified as a string for maximum compatibility with clients."
              }
            ]
          },
          {
            "name": "dbt_task",
            "type": "object",
            "description": "The task runs one or more dbt commands when the ``dbt_task`` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.",
            "children": [
              {
                "name": "commands",
                "type": "array",
                "description": ""
              },
              {
                "name": "catalog",
                "type": "string",
                "description": "Optional name of the catalog to use. The value is the top level in the 3-level namespace of Unity Catalog (catalog / schema / relation). The catalog value can only be specified if a warehouse_id is specified. Requires dbt-databricks &gt;= 1.1.1."
              },
              {
                "name": "profiles_directory",
                "type": "string",
                "description": "Optional (relative) path to the profiles directory. Can only be specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root directory is used."
              },
              {
                "name": "project_directory",
                "type": "string",
                "description": "Path to the project directory. Optional for Git sourced tasks, in which case if no value is provided, the root of the Git repository is used."
              },
              {
                "name": "schema",
                "type": "string",
                "description": "Optional schema to write to. This parameter is only used when a warehouse_id is also provided. If not provided, the ``default`` schema is used."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the project directory. When set to ``WORKSPACE``, the project will be retrieved from the local Databricks workspace. When set to ``GIT``, the project will be retrieved from a Git repository defined in ``git_source``. If the value is empty, the task will use ``GIT`` if ``git_source`` is defined and ``WORKSPACE`` otherwise. - ``WORKSPACE``: Project is located in Databricks workspace. - ``GIT``: Project is located in cloud Git provider. (GIT, WORKSPACE)"
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "ID of the SQL warehouse to connect to. If provided, we automatically generate and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the ``--profiles-dir`` command line argument."
              }
            ]
          },
          {
            "name": "depends_on",
            "type": "array",
            "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is ``task_key``, and the value is the name assigned to the dependent task.",
            "children": [
              {
                "name": "task_key",
                "type": "string",
                "description": ""
              },
              {
                "name": "outcome",
                "type": "string",
                "description": "Can only be specified on condition task dependencies. The outcome of the dependent task that must be met for this task to run."
              }
            ]
          },
          {
            "name": "description",
            "type": "string",
            "description": "An optional description for this task."
          },
          {
            "name": "disable_auto_optimization",
            "type": "boolean",
            "description": "An option to disable auto optimization in serverless"
          },
          {
            "name": "disabled",
            "type": "boolean",
            "description": "An optional flag to disable the task. If set to true, the task will not run even if it is part of a job."
          },
          {
            "name": "effective_performance_target",
            "type": "string",
            "description": "The actual performance target used by the serverless run during execution. This can differ from the client-set performance target on the request depending on whether the performance mode is supported by the job type. - ``STANDARD``: Enables cost-efficient execution of serverless workloads. - ``PERFORMANCE_OPTIMIZED``: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance. (PERFORMANCE_OPTIMIZED, STANDARD)"
          },
          {
            "name": "email_notifications",
            "type": "object",
            "description": "An optional set of email addresses notified when the task run begins or completes. The default behavior is to not send any emails.",
            "children": [
              {
                "name": "no_alert_for_skipped_runs",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "on_duration_warning_threshold_exceeded",
                "type": "array",
                "description": "A list of email addresses to be notified when the duration of a run exceeds the threshold specified for the ``RUN_DURATION_SECONDS`` metric in the ``health`` field. If no rule for the ``RUN_DURATION_SECONDS`` metric is specified in the ``health`` field for the job, notifications are not sent."
              },
              {
                "name": "on_failure",
                "type": "array",
                "description": "A list of email addresses to be notified when a run unsuccessfully completes. A run is considered to have completed unsuccessfully if it ends with an ``INTERNAL_ERROR`` ``life_cycle_state`` or a ``FAILED``, or ``TIMED_OUT`` result_state. If this is not specified on job creation, reset, or update the list is empty, and notifications are not sent."
              },
              {
                "name": "on_maintenance_complete",
                "type": "array",
                "description": "A list of email addresses to notify when platform-initiated maintenance completes for a continuous job."
              },
              {
                "name": "on_maintenance_start",
                "type": "array",
                "description": "A list of email addresses to notify when platform-initiated maintenance starts for a continuous job."
              },
              {
                "name": "on_start",
                "type": "array",
                "description": "A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
              },
              {
                "name": "on_streaming_backlog_exceeded",
                "type": "array",
                "description": "A list of email addresses to notify when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the ``health`` field using the following metrics: ``STREAMING_BACKLOG_BYTES``, ``STREAMING_BACKLOG_RECORDS``, ``STREAMING_BACKLOG_SECONDS``, or ``STREAMING_BACKLOG_FILES``. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes."
              },
              {
                "name": "on_success",
                "type": "array",
                "description": "A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a ``TERMINATED`` ``life_cycle_state`` and a ``SUCCESS`` result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
              }
            ]
          },
          {
            "name": "end_time",
            "type": "integer",
            "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
          },
          {
            "name": "environment_key",
            "type": "string",
            "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
          },
          {
            "name": "environment_variables_key",
            "type": "string",
            "description": "Reference to a ``JobEnvironmentVariables`` entry defined in ``RunSettings.environment_variables``. The selected entry's variables and file contents are applied to this task at execution time. Length and pattern mirror ``environment_key`` so the two references look identical to customers reading task settings."
          },
          {
            "name": "execution_duration",
            "type": "integer",
            "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``execution_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
          },
          {
            "name": "existing_cluster_id",
            "type": "string",
            "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
          },
          {
            "name": "for_each_task",
            "type": "object",
            "description": "The task executes a nested task for every input provided when the ``for_each_task`` field is present.",
            "children": [
              {
                "name": "inputs",
                "type": "string",
                "description": ""
              },
              {
                "name": "task",
                "type": "object",
                "description": "Configuration for the task that will be run for each element in the array"
              },
              {
                "name": "concurrency",
                "type": "integer",
                "description": "An optional maximum allowed number of concurrent runs of the task. Set this value if you want to be able to execute multiple runs of the task concurrently."
              },
              {
                "name": "stats",
                "type": "object",
                "description": "Read only field. Populated for GetRun and ListRuns RPC calls and stores the execution stats of a ``For each`` task."
              }
            ]
          },
          {
            "name": "gen_ai_compute_task",
            "type": "object",
            "description": "DEPRECATED — use ``AiRuntimeTask`` for all new BYOT multi-node GPU workloads (see<br />    ai_runtime_task.proto). ``AiRuntimeTask`` is the only supported BYOT task type for new<br />    workloads; this proto is retained only for AIR CLI (fka SGCLI) pywheel backwards compatibility<br />    and will be removed once the pywheel → databricks-cli migration completes (post- PuPr).",
            "children": [
              {
                "name": "dl_runtime_image",
                "type": "string",
                "description": "Runtime image"
              },
              {
                "name": "client_version",
                "type": "string",
                "description": "Version of the client (e.g., sgcli wheel) that submitted this task. Used by handlers to gate behavior or reject incompatible versions."
              },
              {
                "name": "code_source_tar_path",
                "type": "string",
                "description": "Optional path to a tarball containing the user's workspace contents. When set, the entry script extracts the tarball into the working directory before running the training script, so the training script can import sibling modules and read packaged data files. Must be a workspace path (e.g. ``/Workspace/Users/...``) or volume; ``dbfs:/`` is not supported."
              },
              {
                "name": "command",
                "type": "string",
                "description": "Command launcher to run the actual script, e.g. bash, python etc."
              },
              {
                "name": "compute",
                "type": "object",
                "description": ""
              },
              {
                "name": "docker_image_url",
                "type": "string",
                "description": "Optional custom Docker container image URL for running the training script. Format: organization/repository:tag (e.g., \"pytorch/pytorch:2.0.1\")"
              },
              {
                "name": "mlflow_experiment_name",
                "type": "string",
                "description": "Optional string containing the name of the MLflow experiment to log the run to. If name is not found, backend will create the mlflow experiment using the name."
              },
              {
                "name": "mlflow_run_name",
                "type": "string",
                "description": "Optional name to assign to the MLflow run created for this task. If unset, MLflow auto-generates a name. Used alongside ``mlflow_experiment_name`` to identify the run in the MLflow UI."
              },
              {
                "name": "requirements_yaml_path",
                "type": "string",
                "description": "Optional path to a requirements.yaml file describing pip dependencies to install before running the training script. Consumed by the entry script; format matches the runtime requirements.yaml convention used by sgcli. Must be a workspace path (e.g. ``/Workspace/Users/...``) or volume; ``dbfs:/`` is not supported."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the training script. When set to ``WORKSPACE``, the script will be retrieved from the local Databricks workspace. When set to ``GIT``, the script will be retrieved from a Git repository defined in ``git_source``. If the value is empty, the task will use ``GIT`` if ``git_source`` is defined and ``WORKSPACE`` otherwise. - ``WORKSPACE``: Script is located in Databricks workspace. - ``GIT``: Script is located in cloud Git provider. (GIT, WORKSPACE)"
              },
              {
                "name": "training_script_path",
                "type": "string",
                "description": "The training script file path to be executed. Cloud file URIs (such as dbfs:/, s3:/, adls:/, gcs:/) and workspace paths are supported. For python files stored in the Databricks workspace, the path must be absolute and begin with ``/``. For files stored in a remote repository, the path must be relative. This field is required."
              },
              {
                "name": "yaml_parameters",
                "type": "string",
                "description": "Optional string containing model parameters passed to the training script in yaml format. If present, then the content in yaml_parameters_file_path will be ignored."
              },
              {
                "name": "yaml_parameters_file_path",
                "type": "string",
                "description": "Optional path to a YAML file containing model parameters passed to the training script."
              }
            ]
          },
          {
            "name": "genie_task",
            "type": "object",
            "description": "Runs a Genie or Genie Code agent task.",
            "children": [
              {
                "name": "configuration_id",
                "type": "string",
                "description": "Required. Resource name of the agent task configuration to run."
              }
            ]
          },
          {
            "name": "git_source",
            "type": "object",
            "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If ``git_source`` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting ``source`` to ``WORKSPACE`` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, ``git_source`` must be defined on the job.",
            "children": [
              {
                "name": "git_url",
                "type": "string",
                "description": "URL of the repository to be cloned by this job."
              },
              {
                "name": "git_provider",
                "type": "string",
                "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive. (awsCodeCommit, azureDevOpsServices, bitbucketCloud, bitbucketServer, gitHub, gitHubEnterprise, gitLab, gitLabEnterpriseEdition)"
              },
              {
                "name": "git_branch",
                "type": "string",
                "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
              },
              {
                "name": "git_commit",
                "type": "string",
                "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
              },
              {
                "name": "git_snapshot",
                "type": "object",
                "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs."
              },
              {
                "name": "git_tag",
                "type": "string",
                "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
              },
              {
                "name": "job_source",
                "type": "object",
                "description": "The source of the job specification in the remote repository when the job is source controlled."
              },
              {
                "name": "sparse_checkout",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "job_cluster_key",
            "type": "string",
            "description": "If job_cluster_key, this task is executed reusing the cluster specified in ``job.settings.job_clusters``."
          },
          {
            "name": "libraries",
            "type": "string",
            "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
          },
          {
            "name": "max_retries",
            "type": "integer",
            "description": "An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the ``FAILED`` result_state or ``INTERNAL_ERROR`` ``life_cycle_state``. The value ``-1`` means to retry indefinitely and the value ``0`` means to never retry."
          },
          {
            "name": "min_retry_interval_millis",
            "type": "integer",
            "description": "An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried."
          },
          {
            "name": "new_cluster",
            "type": "string",
            "description": "If new_cluster, a description of a new cluster that is created for each run."
          },
          {
            "name": "notebook_task",
            "type": "object",
            "description": "The task runs a notebook when the ``notebook_task`` field is present.",
            "children": [
              {
                "name": "notebook_path",
                "type": "string",
                "description": ""
              },
              {
                "name": "base_parameters",
                "type": "object",
                "description": "Base parameters to be used for each run of this job. If the run is initiated by a call to :method:jobs/run Now with parameters specified, the two parameters maps are merged. If the same key is specified in ``base_parameters`` and in ``run-now``, the value from ``run-now`` is used. Use `Task parameter variables <https://docs.databricks.com/jobs.html#parameter-variables>`__ to set parameters containing information about job runs. If the notebook takes a parameter that is not specified in the job’s ``base_parameters`` or the ``run-now`` override parameters, the default value from the notebook is used. Retrieve these parameters in a notebook using `dbutils.widgets.get <https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-widgets>`__. The JSON representation of this field cannot exceed 1MB."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the notebook. When set to ``WORKSPACE``, the notebook will be retrieved from the local Databricks workspace. When set to ``GIT``, the notebook will be retrieved from a Git repository defined in ``git_source``. If the value is empty, the task will use ``GIT`` if ``git_source`` is defined and ``WORKSPACE`` otherwise. - ``WORKSPACE``: Notebook is located in Databricks workspace. - ``GIT``: Notebook is located in cloud Git provider. (GIT, WORKSPACE)"
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "Optional ``warehouse_id`` to run the notebook on a SQL warehouse. Classic SQL warehouses are NOT supported, please use serverless or pro SQL warehouses. Note that SQL warehouses only support SQL cells; if the notebook contains non-SQL cells, the run will fail."
              }
            ]
          },
          {
            "name": "notification_settings",
            "type": "object",
            "description": "Optional notification settings that are used when sending notifications to each of the ``email_notifications`` and ``webhook_notifications`` for this task run.",
            "children": [
              {
                "name": "alert_on_last_attempt",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "no_alert_for_canceled_runs",
                "type": "boolean",
                "description": "If true, do not send notifications to recipients specified in ``on_failure`` if the run is canceled."
              },
              {
                "name": "no_alert_for_skipped_runs",
                "type": "boolean",
                "description": "If true, do not send notifications to recipients specified in ``on_failure`` if the run is skipped."
              }
            ]
          },
          {
            "name": "pipeline_task",
            "type": "object",
            "description": "The task triggers a pipeline update when the ``pipeline_task`` field is present. Only pipelines configured to use triggered more are supported.",
            "children": [
              {
                "name": "pipeline_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "full_refresh",
                "type": "boolean",
                "description": "If true, triggers a full refresh on the spark declarative pipeline."
              },
              {
                "name": "full_refresh_selection",
                "type": "array",
                "description": "A list of tables to update with fullRefresh."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Key/value-map of parameters passed to the pipeline execution. Limited to 10k characters in total."
              },
              {
                "name": "refresh_flow_selection",
                "type": "array",
                "description": "Flow names to selectively refresh. These are unioned with other selective refresh options (refresh_selection, full_refresh_selection) to determine the final set of flows to refresh."
              },
              {
                "name": "refresh_selection",
                "type": "array",
                "description": "A list of tables to update without fullRefresh."
              },
              {
                "name": "reset_checkpoint_selection",
                "type": "array",
                "description": "A list of streaming flows to reset checkpoints without clearing data."
              }
            ]
          },
          {
            "name": "power_bi_task",
            "type": "object",
            "description": "The task triggers a Power BI semantic model update when the ``power_bi_task`` field is present.",
            "children": [
              {
                "name": "connection_resource_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "incremental_refresh_config",
                "type": "object",
                "description": "Incremental refresh policy applied to all IMPORT mode tables in the model. Windows and mode are shared; partition columns are set per-table on PowerBiTable."
              },
              {
                "name": "power_bi_model",
                "type": "object",
                "description": "The semantic model to update"
              },
              {
                "name": "refresh_after_update",
                "type": "boolean",
                "description": "Whether the model should be refreshed after the update"
              },
              {
                "name": "tables",
                "type": "array",
                "description": "The tables to be exported to Power BI"
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "The SQL warehouse ID to use as the Power BI data source"
              }
            ]
          },
          {
            "name": "python_operator_task",
            "type": "object",
            "description": "The task runs a Python operator task.",
            "children": [
              {
                "name": "main",
                "type": "string",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "An ordered list of task parameters. TODO(JOBS-30885): Add limits for parameters."
              }
            ]
          },
          {
            "name": "python_wheel_task",
            "type": "object",
            "description": "The task runs a Python wheel when the ``python_wheel_task`` field is present.",
            "children": [
              {
                "name": "package_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "entry_point",
                "type": "string",
                "description": "Named entry point to use, if it does not exist in the metadata of the package it executes the function from the package directly using ``$packageName.$entryPoint()``"
              },
              {
                "name": "named_parameters",
                "type": "object",
                "description": "Command-line parameters passed to Python wheel task in the form of ``[\"--name=task\", \"--data=dbfs:/path/to/data.json\"]``. Leave it empty if ``parameters`` is not null."
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "Command-line parameters passed to Python wheel task. Leave it empty if ``named_parameters`` is not null."
              }
            ]
          },
          {
            "name": "queue_duration",
            "type": "integer",
            "description": "The time in milliseconds that the run has spent in the queue."
          },
          {
            "name": "resolved_values",
            "type": "object",
            "description": "Parameter values including resolved references",
            "children": [
              {
                "name": "agentic_task",
                "type": "object",
                "description": "Resolved values for an agentic task: the ``input`` prompt with parameter references such as<br />    ``&#123;&#123;tasks.&lt;task_key&gt;.values.&lt;name&gt;&#125;&#125;`` replaced by the concrete values produced by upstream<br />    tasks."
              },
              {
                "name": "ai_runtime_task",
                "type": "object",
                "description": "Resolved values for an AI Runtime task — env_vars with ``&#123;&#123;tasks.&lt;key&gt;.values.&lt;name&gt;&#125;&#125;`` references substituted to concrete values before submission to the training service."
              },
              {
                "name": "alert_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "condition_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "dbt_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "notebook_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "pipeline_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "python_wheel_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "run_job_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "simulation_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "spark_jar_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "spark_python_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "spark_submit_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "sql_task",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "retry_on_timeout",
            "type": "boolean",
            "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
          },
          {
            "name": "run_duration",
            "type": "integer",
            "description": "The time in milliseconds it took the job run and all of its repairs to finish."
          },
          {
            "name": "run_id",
            "type": "integer",
            "description": "The ID of the task run."
          },
          {
            "name": "run_if",
            "type": "string",
            "description": "An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to ``ALL_SUCCESS``. See :method:jobs/create for a list of possible values. (ALL_DONE, ALL_FAILED, ALL_SUCCESS, AT_LEAST_ONE_FAILED, AT_LEAST_ONE_SUCCESS, NONE_FAILED)"
          },
          {
            "name": "run_job_task",
            "type": "object",
            "description": "The task triggers another job when the ``run_job_task`` field is present.",
            "children": [
              {
                "name": "job_id",
                "type": "integer",
                "description": ""
              },
              {
                "name": "dbt_commands",
                "type": "array",
                "description": "An array of commands to execute for jobs with the dbt task, for example ``\"dbt_commands\": [\"dbt deps\", \"dbt seed\", \"dbt deps\", \"dbt seed\", \"dbt run\"]`` ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
              },
              {
                "name": "jar_params",
                "type": "array",
                "description": "A list of parameters for jobs with Spark JAR tasks, for example ``\"jar_params\": [\"john doe\", \"35\"]``. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon ``run-now``, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example ``&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
              },
              {
                "name": "job_parameters",
                "type": "object",
                "description": "Job-level parameters used to trigger the job."
              },
              {
                "name": "notebook_params",
                "type": "object",
                "description": "A map from keys to values for jobs with notebook task, for example ``\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;``. The map is passed to the notebook and is accessible through the `dbutils.widgets.get <https://docs.databricks.com/dev-tools/databricks-utils.html>`__ function. If not specified upon ``run-now``, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. The JSON representation of this field (for example ``&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;``) cannot exceed 10,000 bytes."
              },
              {
                "name": "pipeline_params",
                "type": "object",
                "description": "Controls whether the pipeline should perform a full refresh"
              },
              {
                "name": "python_named_params",
                "type": "object",
                "description": ""
              },
              {
                "name": "python_params",
                "type": "array",
                "description": "A list of parameters for jobs with Python tasks, for example ``\"python_params\": [\"john doe\", \"35\"]``. The parameters are passed to Python file as command-line parameters. If specified upon ``run-now``, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example ``&#123;\"python_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis."
              },
              {
                "name": "spark_submit_params",
                "type": "array",
                "description": "A list of parameters for jobs with spark submit task, for example ``\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]``. The parameters are passed to spark-submit script as command-line parameters. If specified upon ``run-now``, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example ``&#123;\"python_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis."
              },
              {
                "name": "sql_params",
                "type": "object",
                "description": "A map from keys to values for jobs with SQL task, for example ``\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;``. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
              }
            ]
          },
          {
            "name": "run_page_url",
            "type": "string",
            "description": ""
          },
          {
            "name": "setup_duration",
            "type": "integer",
            "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``setup_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
          },
          {
            "name": "spark_jar_task",
            "type": "object",
            "description": "The task runs a JAR when the ``spark_jar_task`` field is present.",
            "children": [
              {
                "name": "jar_uri",
                "type": "string",
                "description": ""
              },
              {
                "name": "main_class_name",
                "type": "string",
                "description": "The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library. The code must use ``SparkContext.getOrCreate`` to obtain a Spark context; otherwise, runs of the job fail."
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "Parameters passed to the main method. Use `Task parameter variables <https://docs.databricks.com/jobs.html#parameter-variables>`__ to set parameters containing information about job runs."
              },
              {
                "name": "run_as_repl",
                "type": "boolean",
                "description": "Deprecated. A value of ``false`` is no longer supported."
              }
            ]
          },
          {
            "name": "spark_python_task",
            "type": "object",
            "description": "The task runs a Python file when the ``spark_python_task`` field is present.",
            "children": [
              {
                "name": "python_file",
                "type": "string",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "Command line parameters passed to the Python file. Use `Task parameter variables <https://docs.databricks.com/jobs.html#parameter-variables>`__ to set parameters containing information about job runs."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the Python file. When set to ``WORKSPACE`` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the ``python_file`` has a URI format). When set to ``GIT``, the Python file will be retrieved from a Git repository defined in ``git_source``. - ``WORKSPACE``: The Python file is located in a Databricks workspace or at a cloud filesystem URI. - ``GIT``: The Python file is located in a remote Git repository. (GIT, WORKSPACE)"
              }
            ]
          },
          {
            "name": "spark_submit_task",
            "type": "object",
            "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit).",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "sql_task",
            "type": "object",
            "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the ``sql_task`` field is present.",
            "children": [
              {
                "name": "warehouse_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "alert",
                "type": "object",
                "description": "If alert, indicates that this job must refresh a SQL alert."
              },
              {
                "name": "dashboard",
                "type": "object",
                "description": "If dashboard, indicates that this job must refresh a SQL dashboard."
              },
              {
                "name": "file",
                "type": "object",
                "description": "If file, indicates that this job runs a SQL file in a remote Git repository."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Parameters to be used for each run of this job. The SQL alert task does not support custom parameters."
              },
              {
                "name": "query",
                "type": "object",
                "description": "If query, indicates that this job must execute a SQL query."
              }
            ]
          },
          {
            "name": "start_time",
            "type": "integer",
            "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
          },
          {
            "name": "state",
            "type": "object",
            "description": "Deprecated. Please use the ``status`` field instead.",
            "children": [
              {
                "name": "life_cycle_state",
                "type": "string",
                "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases. (BLOCKED, INTERNAL_ERROR, PENDING, QUEUED, RUNNING, SKIPPED, TERMINATED, TERMINATING, WAITING_FOR_RETRY)"
              },
              {
                "name": "queue_reason",
                "type": "string",
                "description": "The reason indicating why the run was queued."
              },
              {
                "name": "result_state",
                "type": "string",
                "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases. (CANCELED, DISABLED, EXCLUDED, FAILED, MAXIMUM_CONCURRENT_RUNS_REACHED, SUCCESS, SUCCESS_WITH_FAILURES, TIMEDOUT, UPSTREAM_CANCELED, UPSTREAM_FAILED)"
              },
              {
                "name": "state_message",
                "type": "string",
                "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
              },
              {
                "name": "user_cancelled_or_timedout",
                "type": "boolean",
                "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
              }
            ]
          },
          {
            "name": "status",
            "type": "object",
            "description": "The current status of the run",
            "children": [
              {
                "name": "queue_details",
                "type": "object",
                "description": "If the run was queued, details about the reason for queuing the run."
              },
              {
                "name": "state",
                "type": "string",
                "description": "The current state of the run. (BLOCKED, PENDING, QUEUED, RUNNING, TERMINATED, TERMINATING, WAITING)"
              },
              {
                "name": "termination_details",
                "type": "object",
                "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run."
              }
            ]
          },
          {
            "name": "timeout_seconds",
            "type": "integer",
            "description": "An optional timeout applied to each run of this job task. A value of ``0`` means no timeout."
          },
          {
            "name": "webhook_notifications",
            "type": "object",
            "description": "A collection of system notification IDs to notify when the run begins or completes. The default behavior is to not send any system notifications. Task webhooks respect the task notification settings.",
            "children": [
              {
                "name": "on_duration_warning_threshold_exceeded",
                "type": "array",
                "description": ""
              },
              {
                "name": "on_failure",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the ``on_failure`` property."
              },
              {
                "name": "on_maintenance_complete",
                "type": "array",
                "description": "An optional list of system notification IDs to call when platform-initiated maintenance completes for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_complete`` property."
              },
              {
                "name": "on_maintenance_start",
                "type": "array",
                "description": "An optional list of system notification IDs to call when platform-initiated maintenance starts for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_start`` property."
              },
              {
                "name": "on_start",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the ``on_start`` property."
              },
              {
                "name": "on_streaming_backlog_exceeded",
                "type": "array",
                "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the ``health`` field using the following metrics: ``STREAMING_BACKLOG_BYTES``, ``STREAMING_BACKLOG_RECORDS``, ``STREAMING_BACKLOG_SECONDS``, or ``STREAMING_BACKLOG_FILES``. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the ``on_streaming_backlog_exceeded`` property."
              },
              {
                "name": "on_success",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the ``on_success`` property."
              }
            ]
          }
        ]
      },
      {
        "name": "job_clusters",
        "type": "array",
        "description": "A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings. If more than 100 job clusters are available, you can paginate through them using :method:jobs/getrun.",
        "children": [
          {
            "name": "job_cluster_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "new_cluster",
            "type": "string",
            "description": "If new_cluster, a description of a cluster that is created for each task."
          },
          {
            "name": "serverless_compute_id",
            "type": "string",
            "description": "The ID of the serverless compute object to bind this cluster to. At most one JobCluster per job may set this field; the rate limit defined on the referenced serverless compute applies across all tasks bound to this cluster."
          }
        ]
      },
      {
        "name": "job_id",
        "type": "integer",
        "description": "The canonical identifier of the job that contains this run."
      },
      {
        "name": "job_parameters",
        "type": "array",
        "description": "Job-level parameters used in the run",
        "children": [
          {
            "name": "default",
            "type": "string",
            "description": ""
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of the parameter"
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value used in the run"
          }
        ]
      },
      {
        "name": "job_run_id",
        "type": "integer",
        "description": "ID of the job run that this run belongs to. For legacy and single-task job runs the field is populated with the job run ID. For task runs, the field is populated with the ID of the job run that the task run belongs to."
      },
      {
        "name": "next_page_token",
        "type": "string",
        "description": "A token that can be used to list the next page of array properties."
      },
      {
        "name": "number_in_job",
        "type": "integer",
        "description": "A unique identifier for this job run. This is set to the same value as ``run_id``."
      },
      {
        "name": "original_attempt_run_id",
        "type": "integer",
        "description": "If this run is a retry of a prior run attempt, this field contains the run_id of the original attempt; otherwise, it is the same as the run_id."
      },
      {
        "name": "overriding_parameters",
        "type": "object",
        "description": "The parameters used for this run.",
        "children": [
          {
            "name": "dbt_commands",
            "type": "array",
            "description": ""
          },
          {
            "name": "jar_params",
            "type": "array",
            "description": "A list of parameters for jobs with Spark JAR tasks, for example ``\"jar_params\": [\"john doe\", \"35\"]``. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon ``run-now``, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example ``&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
          },
          {
            "name": "notebook_params",
            "type": "object",
            "description": "A map from keys to values for jobs with notebook task, for example ``\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;``. The map is passed to the notebook and is accessible through the `dbutils.widgets.get <https://docs.databricks.com/dev-tools/databricks-utils.html>`__ function. If not specified upon ``run-now``, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. The JSON representation of this field (for example ``&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;``) cannot exceed 10,000 bytes."
          },
          {
            "name": "pipeline_params",
            "type": "object",
            "description": "Controls whether the pipeline should perform a full refresh",
            "children": [
              {
                "name": "full_refresh",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "full_refresh_selection",
                "type": "array",
                "description": "A list of tables to update with fullRefresh."
              },
              {
                "name": "refresh_flow_selection",
                "type": "array",
                "description": "Flow names to selectively refresh. These are unioned with other selective refresh options (refresh_selection, full_refresh_selection) to determine the final set of flows to refresh."
              },
              {
                "name": "refresh_selection",
                "type": "array",
                "description": "A list of tables to update without fullRefresh."
              },
              {
                "name": "reset_checkpoint_selection",
                "type": "array",
                "description": "A list of streaming flows to reset checkpoints without clearing data."
              }
            ]
          },
          {
            "name": "python_named_params",
            "type": "object",
            "description": ""
          },
          {
            "name": "python_params",
            "type": "array",
            "description": "A list of parameters for jobs with Python tasks, for example ``\"python_params\": [\"john doe\", \"35\"]``. The parameters are passed to Python file as command-line parameters. If specified upon ``run-now``, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example ``&#123;\"python_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis."
          },
          {
            "name": "spark_submit_params",
            "type": "array",
            "description": "A list of parameters for jobs with spark submit task, for example ``\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]``. The parameters are passed to spark-submit script as command-line parameters. If specified upon ``run-now``, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example ``&#123;\"python_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis."
          },
          {
            "name": "sql_params",
            "type": "object",
            "description": "A map from keys to values for jobs with SQL task, for example ``\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;``. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
          }
        ]
      },
      {
        "name": "queue_duration",
        "type": "integer",
        "description": "The time in milliseconds that the run has spent in the queue."
      },
      {
        "name": "repair_history",
        "type": "array",
        "description": "The repair history of the run.",
        "children": [
          {
            "name": "effective_performance_target",
            "type": "string",
            "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget). (PERFORMANCE_OPTIMIZED, STANDARD)"
          },
          {
            "name": "end_time",
            "type": "integer",
            "description": "The end time of the (repaired) run."
          },
          {
            "name": "id",
            "type": "integer",
            "description": "The ID of the repair. Only returned for the items that represent a repair in ``repair_history``."
          },
          {
            "name": "start_time",
            "type": "integer",
            "description": "The start time of the (repaired) run."
          },
          {
            "name": "state",
            "type": "object",
            "description": "Deprecated. Please use the ``status`` field instead.",
            "children": [
              {
                "name": "life_cycle_state",
                "type": "string",
                "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases. (BLOCKED, INTERNAL_ERROR, PENDING, QUEUED, RUNNING, SKIPPED, TERMINATED, TERMINATING, WAITING_FOR_RETRY)"
              },
              {
                "name": "queue_reason",
                "type": "string",
                "description": "The reason indicating why the run was queued."
              },
              {
                "name": "result_state",
                "type": "string",
                "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases. (CANCELED, DISABLED, EXCLUDED, FAILED, MAXIMUM_CONCURRENT_RUNS_REACHED, SUCCESS, SUCCESS_WITH_FAILURES, TIMEDOUT, UPSTREAM_CANCELED, UPSTREAM_FAILED)"
              },
              {
                "name": "state_message",
                "type": "string",
                "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
              },
              {
                "name": "user_cancelled_or_timedout",
                "type": "boolean",
                "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
              }
            ]
          },
          {
            "name": "status",
            "type": "object",
            "description": "The current status of the run",
            "children": [
              {
                "name": "queue_details",
                "type": "object",
                "description": "If the run was queued, details about the reason for queuing the run."
              },
              {
                "name": "state",
                "type": "string",
                "description": "The current state of the run. (BLOCKED, PENDING, QUEUED, RUNNING, TERMINATED, TERMINATING, WAITING)"
              },
              {
                "name": "termination_details",
                "type": "object",
                "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run."
              }
            ]
          },
          {
            "name": "task_run_ids",
            "type": "array",
            "description": "The run IDs of the task runs that ran as part of this repair history item."
          },
          {
            "name": "type",
            "type": "string",
            "description": "The repair history item type. Indicates whether a run is the original run or a repair run. (ORIGINAL, REPAIR)"
          }
        ]
      },
      {
        "name": "run_duration",
        "type": "integer",
        "description": "The time in milliseconds it took the job run and all of its repairs to finish."
      },
      {
        "name": "run_id",
        "type": "integer",
        "description": "The canonical identifier of the run. This ID is unique across all runs of all jobs."
      },
      {
        "name": "run_name",
        "type": "string",
        "description": "An optional name for the run. The maximum length is 4096 bytes in UTF-8 encoding."
      },
      {
        "name": "run_page_url",
        "type": "string",
        "description": "The URL to the detail page of the run."
      },
      {
        "name": "run_type",
        "type": "string",
        "description": "The type of a run.<br /><br />- ``JOB_RUN``: Normal job run. A run created with :method:jobs/runNow.<br />- ``WORKFLOW_RUN``: Workflow run. A run created with `dbutils.notebook.run<br />  <https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow>`__.<br />- ``SUBMIT_RUN``: Submit run. A run created with :method:jobs/submit. (JOB_RUN, SUBMIT_RUN, WORKFLOW_RUN)"
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "The cron schedule that triggered this run if it was triggered by the periodic scheduler.",
        "children": [
          {
            "name": "quartz_cron_expression",
            "type": "string",
            "description": ""
          },
          {
            "name": "timezone_id",
            "type": "string",
            "description": "A Java timezone ID. The schedule for a job is resolved with respect to this timezone. See `Java TimeZone <https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html>`__ for details. This field is required."
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Indicate whether this schedule is paused or not. (PAUSED, UNPAUSED)"
          },
          {
            "name": "sql_condition",
            "type": "object",
            "description": "SQL condition that must be satisfied before a scheduled run is triggered. The condition is evaluated after the cron expression fires and must return a truthy result for the run to proceed.",
            "children": [
              {
                "name": "sql_query_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "The canonical identifier of the SQL warehouse to run the condition query against."
              },
              {
                "name": "trigger_mode",
                "type": "string",
                "description": "Determines how the SQL query result is interpreted to decide whether the condition fires. Must be set to a recognized value when provided. When unset on an existing serialized configuration, the server preserves the original semantics by interpreting it as ``QUERY_RETURNS_ROWS``. New configurations should set this explicitly — explicit ``SQL_CONDITION_TRIGGER_MODE_UNSPECIFIED`` is rejected at validation. (QUERY_RETURNS_ROWS, RESULT_VALUE_CHANGES)"
              }
            ]
          }
        ]
      },
      {
        "name": "setup_duration",
        "type": "integer",
        "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``setup_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
      },
      {
        "name": "start_time",
        "type": "integer",
        "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
      },
      {
        "name": "state",
        "type": "object",
        "description": "Deprecated. Please use the ``status`` field instead.",
        "children": [
          {
            "name": "life_cycle_state",
            "type": "string",
            "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases. (BLOCKED, INTERNAL_ERROR, PENDING, QUEUED, RUNNING, SKIPPED, TERMINATED, TERMINATING, WAITING_FOR_RETRY)"
          },
          {
            "name": "queue_reason",
            "type": "string",
            "description": "The reason indicating why the run was queued."
          },
          {
            "name": "result_state",
            "type": "string",
            "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases. (CANCELED, DISABLED, EXCLUDED, FAILED, MAXIMUM_CONCURRENT_RUNS_REACHED, SUCCESS, SUCCESS_WITH_FAILURES, TIMEDOUT, UPSTREAM_CANCELED, UPSTREAM_FAILED)"
          },
          {
            "name": "state_message",
            "type": "string",
            "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
          },
          {
            "name": "user_cancelled_or_timedout",
            "type": "boolean",
            "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
          }
        ]
      },
      {
        "name": "status",
        "type": "object",
        "description": "The current status of the run",
        "children": [
          {
            "name": "queue_details",
            "type": "object",
            "description": "If the run was queued, details about the reason for queuing the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The reason for queuing the run.<br /><br />- ``ACTIVE_RUNS_LIMIT_REACHED``: The run was queued due to reaching the workspace limit of<br />  active task runs.<br />- ``MAX_CONCURRENT_RUNS_REACHED``: The run was queued due to reaching the per-job limit of<br />  concurrent job runs.<br />- ``ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED``: The run was queued due to reaching the workspace limit<br />  of active run job tasks. (ACTIVE_RUNS_LIMIT_REACHED, ACTIVE_RUN_JOB_TASKS_LIMIT_REACHED, MAX_CONCURRENT_RUNS_REACHED)"
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the queuing details. This field is unstructured, and its exact format is subject to change."
              }
            ]
          },
          {
            "name": "state",
            "type": "string",
            "description": "The current state of the run. (BLOCKED, PENDING, QUEUED, RUNNING, TERMINATED, TERMINATING, WAITING)"
          },
          {
            "name": "termination_details",
            "type": "object",
            "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.",
            "children": [
              {
                "name": "code",
                "type": "string",
                "description": "The code indicates why the run was terminated. Additional codes might be introduced in future<br />releases.<br /><br />- ``SUCCESS``: The run was completed successfully.<br />- ``SUCCESS_WITH_FAILURES``: The run was completed successfully but some child runs failed.<br />- ``USER_CANCELED``: The run was successfully canceled during execution by a user.<br />- ``CANCELED``: The run was canceled during execution by the Databricks platform; for example,<br />  if the maximum run duration was exceeded.<br />- ``SKIPPED``: Run was never executed, for example, if the upstream task run failed, the<br />  dependency type condition was not met, or there were no material tasks to execute.<br />- ``INTERNAL_ERROR``: The run encountered an unexpected error. Refer to the state message for<br />  further details.<br />- ``DRIVER_ERROR``: The run encountered an error while communicating with the Spark Driver.<br />- ``CLUSTER_ERROR``: The run failed due to a cluster error. Refer to the state message for<br />  further details.<br />- ``REPOSITORY_CHECKOUT_FAILED``: Failed to complete the checkout due to an error when<br />  communicating with the third party service.<br />- ``INVALID_CLUSTER_REQUEST``: The run failed because it issued an invalid request to start the<br />  cluster.<br />- ``WORKSPACE_RUN_LIMIT_EXCEEDED``: The workspace has reached the quota for the maximum number<br />  of concurrent active runs. Consider scheduling the runs over a larger time frame.<br />- ``FEATURE_DISABLED``: The run failed because it tried to access a feature unavailable for the<br />  workspace.<br />- ``CLUSTER_REQUEST_LIMIT_EXCEEDED``: The number of cluster creation, start, and upsize requests<br />  have exceeded the allotted rate limit. Consider spreading the run execution over a larger time<br />  frame.<br />- ``STORAGE_ACCESS_ERROR``: The run failed due to an error when accessing the customer blob<br />  storage. Refer to the state message for further details.<br />- ``RUN_EXECUTION_ERROR``: The run was completed with task failures. For more details, refer to<br />  the state message or run output.<br />- ``UNAUTHORIZED_ERROR``: The run failed due to a permission issue while accessing a resource.<br />  Refer to the state message for further details.<br />- ``LIBRARY_INSTALLATION_ERROR``: The run failed while installing the user-requested library.<br />  Refer to the state message for further details. The causes might include, but are not limited<br />  to: The provided library is invalid, there are insufficient permissions to install the<br />  library, and so forth.<br />- ``MAX_CONCURRENT_RUNS_EXCEEDED``: The scheduled run exceeds the limit of maximum concurrent<br />  runs set for the job.<br />- ``MAX_SPARK_CONTEXTS_EXCEEDED``: The run is scheduled on a cluster that has already reached<br />  the maximum number of contexts it is configured to create. See: `Link<br />  <https://kb.databricks.com/en_US/notebooks/too-many-execution-contexts-are-open-right-now>`__.<br />- ``RESOURCE_NOT_FOUND``: A resource necessary for run execution does not exist. Refer to the<br />  state message for further details.<br />- ``INVALID_RUN_CONFIGURATION``: The run failed due to an invalid configuration. Refer to the<br />  state message for further details.<br />- ``CLOUD_FAILURE``: The run failed due to a cloud provider issue. Refer to the state message<br />  for further details.<br />- ``MAX_JOB_QUEUE_SIZE_EXCEEDED``: The run was skipped due to reaching the job level queue size<br />  limit.<br />- ``DISABLED``: The run was never executed because it was disabled explicitly by the user.<br />- ``BREAKING_CHANGE``: Run failed because of an intentional breaking change in Spark, but it<br />  will be retried with a mitigation config.<br />- ``CLUSTER_TERMINATED_BY_USER``: The run failed because the externally managed cluster entered<br />  an unusable state, likely due to the user terminating or restarting it outside the jobs<br />  service. (BREAKING_CHANGE, BUDGET_POLICY_LIMIT_EXCEEDED, CANCELED, CLOUD_FAILURE, CLUSTER_ERROR, CLUSTER_REQUEST_LIMIT_EXCEEDED, CLUSTER_TERMINATED_BY_USER, DISABLED, DRIVER_ERROR, FEATURE_DISABLED, INTERNAL_ERROR, INVALID_CLUSTER_REQUEST, INVALID_RUN_CONFIGURATION, LIBRARY_INSTALLATION_ERROR, MAX_CONCURRENT_RUNS_EXCEEDED, MAX_JOB_QUEUE_SIZE_EXCEEDED, MAX_SPARK_CONTEXTS_EXCEEDED, REPOSITORY_CHECKOUT_FAILED, RESOURCE_NOT_FOUND, RUN_EXECUTION_ERROR, SKIPPED, STORAGE_ACCESS_ERROR, SUCCESS, SUCCESS_WITH_FAILURES, UNAUTHORIZED_ERROR, USER_CANCELED, WORKSPACE_RUN_LIMIT_EXCEEDED)"
              },
              {
                "name": "message",
                "type": "string",
                "description": "A descriptive message with the termination details. This field is unstructured and the format might change."
              },
              {
                "name": "type",
                "type": "string",
                "description": "- ``SUCCESS``: The run terminated without any issues<br />- ``INTERNAL_ERROR``: An error occurred in the Databricks platform. Please look at the `status<br />  page <https://status.databricks.com/>`__ or contact support if the issue persists.<br />- ``CLIENT_ERROR``: The run was terminated because of an error caused by user input or the job<br />  configuration.<br />- ``CLOUD_FAILURE``: The run was terminated because of an issue with your cloud provider. (CLIENT_ERROR, CLOUD_FAILURE, INTERNAL_ERROR, SUCCESS)"
              }
            ]
          }
        ]
      },
      {
        "name": "tasks",
        "type": "array",
        "description": "The list of tasks performed by the run. Each task has its own ``run_id`` which you can use to call ``JobsGetOutput`` to retrieve the run results. If more than 100 tasks are available, you can paginate through them using :method:jobs/getrun. Use the ``next_page_token`` field at the object root to determine if more results are available.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": "A unique name for the task. This field is used to refer to this task from other tasks. This field is required and must be unique within its parent job. On Update or Reset, this field is used to reference the tasks to be updated or reset."
          },
          {
            "name": "agentic_task",
            "type": "object",
            "description": "Agentic Task for job-based multi-agent execution",
            "children": [
              {
                "name": "context",
                "type": "object",
                "description": "Optional. Context input providing conversation history and instructions."
              },
              {
                "name": "genie_code_api",
                "type": "object",
                "description": "Inline Genie Code conversation driven by a single prompt. Mutually exclusive with the supervisor variants."
              },
              {
                "name": "goal",
                "type": "string",
                "description": "Deprecated. Use ``input`` (field 7) instead. Kept for backwards compatibility with existing callers; will be removed in a future revision."
              },
              {
                "name": "input",
                "type": "string",
                "description": "Optional. The user query / task input the agent must accomplish. Mirrors the OpenAI Responses API ``input`` field. Replaces the deprecated ``goal`` field; new callers should populate ``input`` going forward."
              },
              {
                "name": "output_schema",
                "type": "object",
                "description": "Optional. JSON-Schema-style declaration of the structured output the agent should produce. Replaces the deprecated ``task_output_schema`` map; new callers should populate ``output_schema`` going forward."
              },
              {
                "name": "supervisor_agent",
                "type": "object",
                "description": "A Supervisor Agent that orchestrates sub-agents and tools, referenced by tile_id."
              },
              {
                "name": "supervisor_api",
                "type": "object",
                "description": "Inlined Responses-API supervisor configuration (model + instructions + tools). Mutually exclusive with ``supervisor_agent``."
              },
              {
                "name": "task_output_schema",
                "type": "object",
                "description": "Deprecated. Use ``output_schema`` (field 8) instead. Kept for backwards compatibility with existing callers; will be removed in a future revision."
              },
              {
                "name": "trace_destination",
                "type": "object",
                "description": "Optional. Where MLflow traces produced by this task run should be persisted. When unset, traces follow the workspace default destination."
              }
            ]
          },
          {
            "name": "ai_runtime_task",
            "type": "object",
            "description": "The task runs a multi-gpu compute workload on Databricks AI Runtime. Specify the accelerator type and count, the command to run, and where the workload's code and MLflow output are stored.",
            "children": [
              {
                "name": "experiment",
                "type": "string",
                "description": "MLflow experiment name for this run. If an experiment with this name already exists under the calling user, the run is appended to it; otherwise a new experiment is created. To target a specific MLflow storage location (for example, when running as a service principal), set ``mlflow_experiment_directory``."
              },
              {
                "name": "deployments",
                "type": "array",
                "description": "Deployment specs for this task. Exactly one deployment is currently supported (a single entry where every node runs the same command); this is a current-Preview constraint. Role-split workloads (driver + worker, parameter server, separate eval node, etc.) with multiple entries are the eventual intent but not yet supported."
              },
              {
                "name": "code_source_path",
                "type": "string",
                "description": "Workspace or UC volume path of the code-source archive, unpacked on each node and exposed through ``$CODE_SOURCE``. Set by first-party tooling; not for direct callers."
              },
              {
                "name": "docker_image_url",
                "type": "string",
                "description": "Optional Docker image URL for a custom container image. When set, the task runs on the specified container image instead of the default Databricks client image. Format: ``&#123;organization&#125;/&#123;repository&#125;:&#123;tag&#125;``"
              },
              {
                "name": "mlflow_experiment_directory",
                "type": "string",
                "description": "Optional workspace directory under which the MLflow experiment named in ``experiment`` is created. Must start with ``/Workspace``. Set this when running as a service principal that has no default user directory; for regular users the experiment defaults to the user's home directory."
              },
              {
                "name": "mlflow_run",
                "type": "string",
                "description": "Optional display name for the MLflow run created under ``experiment``. If omitted, MLflow generates a default name."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Optional named parameters passed to each deployment's command. Keys are parameter names, values the corresponding arguments (for example, ``&#123;\"epochs\": \"3\", \"dataset\": \"s3://bucket/train\"&#125;``). Values may contain dynamic references such as ``&#123;&#123;job.trigger.time.iso_date&#125;&#125;`` or ``&#123;&#123;tasks.&lt;task_key&gt;.values.&lt;name&gt;&#125;&#125;``, which Jobs substitutes before execution (see ``AiRuntimeTaskResolvedValues.parameters`` in runs.proto)."
              }
            ]
          },
          {
            "name": "alert_task",
            "type": "object",
            "description": "The task evaluates a Databricks alert and sends notifications to subscribers when the ``alert_task`` field is present.",
            "children": [
              {
                "name": "alert_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Per-run parameter overrides, keyed by parameter name, applied onto the alert's stored query parameters before the query is executed. Only scalar values are supported. Values may reference job parameters with ``&#123;&#123;job.parameters.*&#125;&#125;``, which are resolved before the task runs. An override whose key does not match a stored parameter fails the task run. Limited to 10000 characters when serialized as JSON; keys must be 1-100 characters and contain only letters, digits, underscores, dashes, and periods."
              },
              {
                "name": "subscribers",
                "type": "array",
                "description": "The subscribers receive alert evaluation result notifications after the alert task is completed. The number of subscriptions is limited to 100."
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "The warehouse_id identifies the warehouse settings used by the alert task."
              },
              {
                "name": "workspace_path",
                "type": "string",
                "description": "The workspace_path is the path to the alert file in the workspace. The path: - must start with \"/Workspace\" - must be a normalized path. User has to select only one of alert_id or workspace_path to identify the alert."
              }
            ]
          },
          {
            "name": "attempt_number",
            "type": "integer",
            "description": "The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt_number of 0. If the initial run attempt fails, and the job has a retry policy (``max_retries`` &gt; 0), subsequent runs are created with an ``original_attempt_run_id`` of the original attempt’s ID and an incrementing ``attempt_number``. Runs are retried only until they succeed, and the maximum ``attempt_number`` is the same as the ``max_retries`` value for the job."
          },
          {
            "name": "clean_rooms_notebook_task",
            "type": "object",
            "description": "The task runs a `clean rooms <https://docs.databricks.com/clean-rooms/index.html>`__ notebook when the ``clean_rooms_notebook_task`` field is present.",
            "children": [
              {
                "name": "clean_room_name",
                "type": "string",
                "description": "The clean room that the notebook belongs to."
              },
              {
                "name": "notebook_name",
                "type": "string",
                "description": "Name of the notebook being run."
              },
              {
                "name": "etag",
                "type": "string",
                "description": "Checksum to validate the freshness of the notebook resource (i.e. the notebook being run is the latest version). It can be fetched by calling the :method:cleanroomassets/get API."
              },
              {
                "name": "notebook_base_parameters",
                "type": "object",
                "description": "Base parameters to be used for the clean room notebook job."
              }
            ]
          },
          {
            "name": "cleanup_duration",
            "type": "integer",
            "description": "The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``cleanup_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
          },
          {
            "name": "cluster_instance",
            "type": "object",
            "description": "The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.",
            "children": [
              {
                "name": "cluster_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "spark_context_id",
                "type": "string",
                "description": "The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to ``/#setting/sparkui/$cluster_id/$spark_context_id``. The Spark UI continues to be available after the run has completed. The response won’t include this field if the identifier is not available yet."
              }
            ]
          },
          {
            "name": "compute",
            "type": "object",
            "description": "Task level compute configuration.",
            "children": [
              {
                "name": "hardware_accelerator",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "condition_task",
            "type": "object",
            "description": "The task evaluates a condition that can be used to control the execution of other tasks when the ``condition_task`` field is present. The condition task does not require a cluster to execute and does not support retries or notifications.",
            "children": [
              {
                "name": "op",
                "type": "string",
                "description": "- ``EQUAL_TO``, ``NOT_EQUAL`` operators perform string comparison of their operands. This means<br />  that ``“12.0” == “12”`` will evaluate to ``false``.<br />- ``GREATER_THAN``, ``GREATER_THAN_OR_EQUAL``, ``LESS_THAN``, ``LESS_THAN_OR_EQUAL`` operators<br />  perform numeric comparison of their operands. ``“12.0” &gt;= “12”`` will evaluate to<br />  ``true``, ``“10.0” &gt;= “12”`` will evaluate to ``false``.<br /><br />The boolean comparison to task values can be implemented with operators ``EQUAL_TO``,<br />``NOT_EQUAL``. If a task value was set to a boolean value, it will be serialized to<br />``“true”`` or ``“false”`` for the comparison. (EQUAL_TO, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
              },
              {
                "name": "left",
                "type": "string",
                "description": "The left operand of the condition task. Can be either a string value or a job state or parameter reference."
              },
              {
                "name": "right",
                "type": "string",
                "description": "The right operand of the condition task. Can be either a string value or a job state or parameter reference."
              },
              {
                "name": "outcome",
                "type": "string",
                "description": "The condition expression evaluation result. Filled in if the task was successfully completed. Can be ``\"true\"`` or ``\"false\"``"
              }
            ]
          },
          {
            "name": "dashboard_task",
            "type": "object",
            "description": "The task refreshes a dashboard and sends a snapshot to subscribers.",
            "children": [
              {
                "name": "dashboard_id",
                "type": "string",
                "description": "The identifier of the dashboard to refresh."
              },
              {
                "name": "filters",
                "type": "object",
                "description": "Dashboard task parameters. Used to apply dashboard filter values during dashboard task execution. Parameter values get applied to any dashboard filters that have a matching URL identifier as the parameter key. The parameter value format is dependent on the filter type: - For text and single-select filters, provide a single value (e.g. ``\"value\"``) - For date and datetime filters, provide the value in ISO 8601 format (e.g. ``\"2000-01-01T00:00:00\"``) - For multi-select filters, provide a JSON array of values (e.g. ``\"[\\\"value1\\\",\\\"value2\\\"]\"``) - For range and date range filters, provide a JSON object with ``start`` and ``end`` (e.g. ``\"&#123;\\\"start\\\":\\\"1\\\",\\\"end\\\":\\\"10\\\"&#125;\"``)"
              },
              {
                "name": "subscription",
                "type": "object",
                "description": "Optional: subscription configuration for sending the dashboard snapshot."
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "Optional: The warehouse id to execute the dashboard with for the schedule. If not specified, the default warehouse of the dashboard will be used."
              }
            ]
          },
          {
            "name": "dbt_cloud_task",
            "type": "object",
            "description": "Task type for dbt cloud, deprecated in favor of the new name dbt_platform_task",
            "children": [
              {
                "name": "connection_resource_name",
                "type": "string",
                "description": "The resource name of the UC connection that authenticates the dbt Cloud for this task"
              },
              {
                "name": "dbt_cloud_job_id",
                "type": "integer",
                "description": "Id of the dbt Cloud job to be triggered"
              }
            ]
          },
          {
            "name": "dbt_platform_task",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "connection_resource_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "dbt_platform_job_id",
                "type": "string",
                "description": "Id of the dbt platform job to be triggered. Specified as a string for maximum compatibility with clients."
              }
            ]
          },
          {
            "name": "dbt_task",
            "type": "object",
            "description": "The task runs one or more dbt commands when the ``dbt_task`` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.",
            "children": [
              {
                "name": "commands",
                "type": "array",
                "description": ""
              },
              {
                "name": "catalog",
                "type": "string",
                "description": "Optional name of the catalog to use. The value is the top level in the 3-level namespace of Unity Catalog (catalog / schema / relation). The catalog value can only be specified if a warehouse_id is specified. Requires dbt-databricks &gt;= 1.1.1."
              },
              {
                "name": "profiles_directory",
                "type": "string",
                "description": "Optional (relative) path to the profiles directory. Can only be specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root directory is used."
              },
              {
                "name": "project_directory",
                "type": "string",
                "description": "Path to the project directory. Optional for Git sourced tasks, in which case if no value is provided, the root of the Git repository is used."
              },
              {
                "name": "schema",
                "type": "string",
                "description": "Optional schema to write to. This parameter is only used when a warehouse_id is also provided. If not provided, the ``default`` schema is used."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the project directory. When set to ``WORKSPACE``, the project will be retrieved from the local Databricks workspace. When set to ``GIT``, the project will be retrieved from a Git repository defined in ``git_source``. If the value is empty, the task will use ``GIT`` if ``git_source`` is defined and ``WORKSPACE`` otherwise. - ``WORKSPACE``: Project is located in Databricks workspace. - ``GIT``: Project is located in cloud Git provider. (GIT, WORKSPACE)"
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "ID of the SQL warehouse to connect to. If provided, we automatically generate and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the ``--profiles-dir`` command line argument."
              }
            ]
          },
          {
            "name": "depends_on",
            "type": "array",
            "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task. The key is ``task_key``, and the value is the name assigned to the dependent task.",
            "children": [
              {
                "name": "task_key",
                "type": "string",
                "description": ""
              },
              {
                "name": "outcome",
                "type": "string",
                "description": "Can only be specified on condition task dependencies. The outcome of the dependent task that must be met for this task to run."
              }
            ]
          },
          {
            "name": "description",
            "type": "string",
            "description": "An optional description for this task."
          },
          {
            "name": "disable_auto_optimization",
            "type": "boolean",
            "description": "An option to disable auto optimization in serverless"
          },
          {
            "name": "disabled",
            "type": "boolean",
            "description": "An optional flag to disable the task. If set to true, the task will not run even if it is part of a job."
          },
          {
            "name": "effective_performance_target",
            "type": "string",
            "description": "The actual performance target used by the serverless run during execution. This can differ from the client-set performance target on the request depending on whether the performance mode is supported by the job type. - ``STANDARD``: Enables cost-efficient execution of serverless workloads. - ``PERFORMANCE_OPTIMIZED``: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance. (PERFORMANCE_OPTIMIZED, STANDARD)"
          },
          {
            "name": "email_notifications",
            "type": "object",
            "description": "An optional set of email addresses notified when the task run begins or completes. The default behavior is to not send any emails.",
            "children": [
              {
                "name": "no_alert_for_skipped_runs",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "on_duration_warning_threshold_exceeded",
                "type": "array",
                "description": "A list of email addresses to be notified when the duration of a run exceeds the threshold specified for the ``RUN_DURATION_SECONDS`` metric in the ``health`` field. If no rule for the ``RUN_DURATION_SECONDS`` metric is specified in the ``health`` field for the job, notifications are not sent."
              },
              {
                "name": "on_failure",
                "type": "array",
                "description": "A list of email addresses to be notified when a run unsuccessfully completes. A run is considered to have completed unsuccessfully if it ends with an ``INTERNAL_ERROR`` ``life_cycle_state`` or a ``FAILED``, or ``TIMED_OUT`` result_state. If this is not specified on job creation, reset, or update the list is empty, and notifications are not sent."
              },
              {
                "name": "on_maintenance_complete",
                "type": "array",
                "description": "A list of email addresses to notify when platform-initiated maintenance completes for a continuous job."
              },
              {
                "name": "on_maintenance_start",
                "type": "array",
                "description": "A list of email addresses to notify when platform-initiated maintenance starts for a continuous job."
              },
              {
                "name": "on_start",
                "type": "array",
                "description": "A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
              },
              {
                "name": "on_streaming_backlog_exceeded",
                "type": "array",
                "description": "A list of email addresses to notify when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the ``health`` field using the following metrics: ``STREAMING_BACKLOG_BYTES``, ``STREAMING_BACKLOG_RECORDS``, ``STREAMING_BACKLOG_SECONDS``, or ``STREAMING_BACKLOG_FILES``. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes."
              },
              {
                "name": "on_success",
                "type": "array",
                "description": "A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a ``TERMINATED`` ``life_cycle_state`` and a ``SUCCESS`` result_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent."
              }
            ]
          },
          {
            "name": "end_time",
            "type": "integer",
            "description": "The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running."
          },
          {
            "name": "environment_key",
            "type": "string",
            "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
          },
          {
            "name": "environment_variables_key",
            "type": "string",
            "description": "Reference to a ``JobEnvironmentVariables`` entry defined in ``RunSettings.environment_variables``. The selected entry's variables and file contents are applied to this task at execution time. Length and pattern mirror ``environment_key`` so the two references look identical to customers reading task settings."
          },
          {
            "name": "execution_duration",
            "type": "integer",
            "description": "The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``execution_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
          },
          {
            "name": "existing_cluster_id",
            "type": "string",
            "description": "If existing_cluster_id, the ID of an existing cluster that is used for all runs. When running jobs or tasks on an existing cluster, you may need to manually restart the cluster if it stops responding. We suggest running jobs and tasks on new clusters for greater reliability"
          },
          {
            "name": "for_each_task",
            "type": "object",
            "description": "The task executes a nested task for every input provided when the ``for_each_task`` field is present.",
            "children": [
              {
                "name": "inputs",
                "type": "string",
                "description": ""
              },
              {
                "name": "task",
                "type": "object",
                "description": "Configuration for the task that will be run for each element in the array"
              },
              {
                "name": "concurrency",
                "type": "integer",
                "description": "An optional maximum allowed number of concurrent runs of the task. Set this value if you want to be able to execute multiple runs of the task concurrently."
              },
              {
                "name": "stats",
                "type": "object",
                "description": "Read only field. Populated for GetRun and ListRuns RPC calls and stores the execution stats of a ``For each`` task."
              }
            ]
          },
          {
            "name": "gen_ai_compute_task",
            "type": "object",
            "description": "DEPRECATED — use ``AiRuntimeTask`` for all new BYOT multi-node GPU workloads (see<br />    ai_runtime_task.proto). ``AiRuntimeTask`` is the only supported BYOT task type for new<br />    workloads; this proto is retained only for AIR CLI (fka SGCLI) pywheel backwards compatibility<br />    and will be removed once the pywheel → databricks-cli migration completes (post- PuPr).",
            "children": [
              {
                "name": "dl_runtime_image",
                "type": "string",
                "description": "Runtime image"
              },
              {
                "name": "client_version",
                "type": "string",
                "description": "Version of the client (e.g., sgcli wheel) that submitted this task. Used by handlers to gate behavior or reject incompatible versions."
              },
              {
                "name": "code_source_tar_path",
                "type": "string",
                "description": "Optional path to a tarball containing the user's workspace contents. When set, the entry script extracts the tarball into the working directory before running the training script, so the training script can import sibling modules and read packaged data files. Must be a workspace path (e.g. ``/Workspace/Users/...``) or volume; ``dbfs:/`` is not supported."
              },
              {
                "name": "command",
                "type": "string",
                "description": "Command launcher to run the actual script, e.g. bash, python etc."
              },
              {
                "name": "compute",
                "type": "object",
                "description": ""
              },
              {
                "name": "docker_image_url",
                "type": "string",
                "description": "Optional custom Docker container image URL for running the training script. Format: organization/repository:tag (e.g., \"pytorch/pytorch:2.0.1\")"
              },
              {
                "name": "mlflow_experiment_name",
                "type": "string",
                "description": "Optional string containing the name of the MLflow experiment to log the run to. If name is not found, backend will create the mlflow experiment using the name."
              },
              {
                "name": "mlflow_run_name",
                "type": "string",
                "description": "Optional name to assign to the MLflow run created for this task. If unset, MLflow auto-generates a name. Used alongside ``mlflow_experiment_name`` to identify the run in the MLflow UI."
              },
              {
                "name": "requirements_yaml_path",
                "type": "string",
                "description": "Optional path to a requirements.yaml file describing pip dependencies to install before running the training script. Consumed by the entry script; format matches the runtime requirements.yaml convention used by sgcli. Must be a workspace path (e.g. ``/Workspace/Users/...``) or volume; ``dbfs:/`` is not supported."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the training script. When set to ``WORKSPACE``, the script will be retrieved from the local Databricks workspace. When set to ``GIT``, the script will be retrieved from a Git repository defined in ``git_source``. If the value is empty, the task will use ``GIT`` if ``git_source`` is defined and ``WORKSPACE`` otherwise. - ``WORKSPACE``: Script is located in Databricks workspace. - ``GIT``: Script is located in cloud Git provider. (GIT, WORKSPACE)"
              },
              {
                "name": "training_script_path",
                "type": "string",
                "description": "The training script file path to be executed. Cloud file URIs (such as dbfs:/, s3:/, adls:/, gcs:/) and workspace paths are supported. For python files stored in the Databricks workspace, the path must be absolute and begin with ``/``. For files stored in a remote repository, the path must be relative. This field is required."
              },
              {
                "name": "yaml_parameters",
                "type": "string",
                "description": "Optional string containing model parameters passed to the training script in yaml format. If present, then the content in yaml_parameters_file_path will be ignored."
              },
              {
                "name": "yaml_parameters_file_path",
                "type": "string",
                "description": "Optional path to a YAML file containing model parameters passed to the training script."
              }
            ]
          },
          {
            "name": "genie_task",
            "type": "object",
            "description": "Runs a Genie or Genie Code agent task.",
            "children": [
              {
                "name": "configuration_id",
                "type": "string",
                "description": "Required. Resource name of the agent task configuration to run."
              }
            ]
          },
          {
            "name": "git_source",
            "type": "object",
            "description": "An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If ``git_source`` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting ``source`` to ``WORKSPACE`` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, ``git_source`` must be defined on the job.",
            "children": [
              {
                "name": "git_url",
                "type": "string",
                "description": "URL of the repository to be cloned by this job."
              },
              {
                "name": "git_provider",
                "type": "string",
                "description": "Unique identifier of the service used to host the Git repository. The value is case insensitive. (awsCodeCommit, azureDevOpsServices, bitbucketCloud, bitbucketServer, gitHub, gitHubEnterprise, gitLab, gitLabEnterpriseEdition)"
              },
              {
                "name": "git_branch",
                "type": "string",
                "description": "Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git_tag or git_commit."
              },
              {
                "name": "git_commit",
                "type": "string",
                "description": "Commit to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_tag."
              },
              {
                "name": "git_snapshot",
                "type": "object",
                "description": "Read-only state of the remote repository at the time the job was run. This field is only<br />    included on job runs."
              },
              {
                "name": "git_tag",
                "type": "string",
                "description": "Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git_branch or git_commit."
              },
              {
                "name": "job_source",
                "type": "object",
                "description": "The source of the job specification in the remote repository when the job is source controlled."
              },
              {
                "name": "sparse_checkout",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "job_cluster_key",
            "type": "string",
            "description": "If job_cluster_key, this task is executed reusing the cluster specified in ``job.settings.job_clusters``."
          },
          {
            "name": "libraries",
            "type": "string",
            "description": "An optional list of libraries to be installed on the cluster. The default value is an empty list."
          },
          {
            "name": "max_retries",
            "type": "integer",
            "description": "An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the ``FAILED`` result_state or ``INTERNAL_ERROR`` ``life_cycle_state``. The value ``-1`` means to retry indefinitely and the value ``0`` means to never retry."
          },
          {
            "name": "min_retry_interval_millis",
            "type": "integer",
            "description": "An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried."
          },
          {
            "name": "new_cluster",
            "type": "string",
            "description": "If new_cluster, a description of a new cluster that is created for each run."
          },
          {
            "name": "notebook_task",
            "type": "object",
            "description": "The task runs a notebook when the ``notebook_task`` field is present.",
            "children": [
              {
                "name": "notebook_path",
                "type": "string",
                "description": ""
              },
              {
                "name": "base_parameters",
                "type": "object",
                "description": "Base parameters to be used for each run of this job. If the run is initiated by a call to :method:jobs/run Now with parameters specified, the two parameters maps are merged. If the same key is specified in ``base_parameters`` and in ``run-now``, the value from ``run-now`` is used. Use `Task parameter variables <https://docs.databricks.com/jobs.html#parameter-variables>`__ to set parameters containing information about job runs. If the notebook takes a parameter that is not specified in the job’s ``base_parameters`` or the ``run-now`` override parameters, the default value from the notebook is used. Retrieve these parameters in a notebook using `dbutils.widgets.get <https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-widgets>`__. The JSON representation of this field cannot exceed 1MB."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the notebook. When set to ``WORKSPACE``, the notebook will be retrieved from the local Databricks workspace. When set to ``GIT``, the notebook will be retrieved from a Git repository defined in ``git_source``. If the value is empty, the task will use ``GIT`` if ``git_source`` is defined and ``WORKSPACE`` otherwise. - ``WORKSPACE``: Notebook is located in Databricks workspace. - ``GIT``: Notebook is located in cloud Git provider. (GIT, WORKSPACE)"
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "Optional ``warehouse_id`` to run the notebook on a SQL warehouse. Classic SQL warehouses are NOT supported, please use serverless or pro SQL warehouses. Note that SQL warehouses only support SQL cells; if the notebook contains non-SQL cells, the run will fail."
              }
            ]
          },
          {
            "name": "notification_settings",
            "type": "object",
            "description": "Optional notification settings that are used when sending notifications to each of the ``email_notifications`` and ``webhook_notifications`` for this task run.",
            "children": [
              {
                "name": "alert_on_last_attempt",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "no_alert_for_canceled_runs",
                "type": "boolean",
                "description": "If true, do not send notifications to recipients specified in ``on_failure`` if the run is canceled."
              },
              {
                "name": "no_alert_for_skipped_runs",
                "type": "boolean",
                "description": "If true, do not send notifications to recipients specified in ``on_failure`` if the run is skipped."
              }
            ]
          },
          {
            "name": "pipeline_task",
            "type": "object",
            "description": "The task triggers a pipeline update when the ``pipeline_task`` field is present. Only pipelines configured to use triggered more are supported.",
            "children": [
              {
                "name": "pipeline_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "full_refresh",
                "type": "boolean",
                "description": "If true, triggers a full refresh on the spark declarative pipeline."
              },
              {
                "name": "full_refresh_selection",
                "type": "array",
                "description": "A list of tables to update with fullRefresh."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Key/value-map of parameters passed to the pipeline execution. Limited to 10k characters in total."
              },
              {
                "name": "refresh_flow_selection",
                "type": "array",
                "description": "Flow names to selectively refresh. These are unioned with other selective refresh options (refresh_selection, full_refresh_selection) to determine the final set of flows to refresh."
              },
              {
                "name": "refresh_selection",
                "type": "array",
                "description": "A list of tables to update without fullRefresh."
              },
              {
                "name": "reset_checkpoint_selection",
                "type": "array",
                "description": "A list of streaming flows to reset checkpoints without clearing data."
              }
            ]
          },
          {
            "name": "power_bi_task",
            "type": "object",
            "description": "The task triggers a Power BI semantic model update when the ``power_bi_task`` field is present.",
            "children": [
              {
                "name": "connection_resource_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "incremental_refresh_config",
                "type": "object",
                "description": "Incremental refresh policy applied to all IMPORT mode tables in the model. Windows and mode are shared; partition columns are set per-table on PowerBiTable."
              },
              {
                "name": "power_bi_model",
                "type": "object",
                "description": "The semantic model to update"
              },
              {
                "name": "refresh_after_update",
                "type": "boolean",
                "description": "Whether the model should be refreshed after the update"
              },
              {
                "name": "tables",
                "type": "array",
                "description": "The tables to be exported to Power BI"
              },
              {
                "name": "warehouse_id",
                "type": "string",
                "description": "The SQL warehouse ID to use as the Power BI data source"
              }
            ]
          },
          {
            "name": "python_operator_task",
            "type": "object",
            "description": "The task runs a Python operator task.",
            "children": [
              {
                "name": "main",
                "type": "string",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "An ordered list of task parameters. TODO(JOBS-30885): Add limits for parameters."
              }
            ]
          },
          {
            "name": "python_wheel_task",
            "type": "object",
            "description": "The task runs a Python wheel when the ``python_wheel_task`` field is present.",
            "children": [
              {
                "name": "package_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "entry_point",
                "type": "string",
                "description": "Named entry point to use, if it does not exist in the metadata of the package it executes the function from the package directly using ``$packageName.$entryPoint()``"
              },
              {
                "name": "named_parameters",
                "type": "object",
                "description": "Command-line parameters passed to Python wheel task in the form of ``[\"--name=task\", \"--data=dbfs:/path/to/data.json\"]``. Leave it empty if ``parameters`` is not null."
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "Command-line parameters passed to Python wheel task. Leave it empty if ``named_parameters`` is not null."
              }
            ]
          },
          {
            "name": "queue_duration",
            "type": "integer",
            "description": "The time in milliseconds that the run has spent in the queue."
          },
          {
            "name": "resolved_values",
            "type": "object",
            "description": "Parameter values including resolved references",
            "children": [
              {
                "name": "agentic_task",
                "type": "object",
                "description": "Resolved values for an agentic task: the ``input`` prompt with parameter references such as<br />    ``&#123;&#123;tasks.&lt;task_key&gt;.values.&lt;name&gt;&#125;&#125;`` replaced by the concrete values produced by upstream<br />    tasks."
              },
              {
                "name": "ai_runtime_task",
                "type": "object",
                "description": "Resolved values for an AI Runtime task — env_vars with ``&#123;&#123;tasks.&lt;key&gt;.values.&lt;name&gt;&#125;&#125;`` references substituted to concrete values before submission to the training service."
              },
              {
                "name": "alert_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "condition_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "dbt_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "notebook_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "pipeline_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "python_wheel_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "run_job_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "simulation_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "spark_jar_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "spark_python_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "spark_submit_task",
                "type": "object",
                "description": ""
              },
              {
                "name": "sql_task",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "retry_on_timeout",
            "type": "boolean",
            "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
          },
          {
            "name": "run_duration",
            "type": "integer",
            "description": "The time in milliseconds it took the job run and all of its repairs to finish."
          },
          {
            "name": "run_id",
            "type": "integer",
            "description": "The ID of the task run."
          },
          {
            "name": "run_if",
            "type": "string",
            "description": "An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to ``ALL_SUCCESS``. See :method:jobs/create for a list of possible values. (ALL_DONE, ALL_FAILED, ALL_SUCCESS, AT_LEAST_ONE_FAILED, AT_LEAST_ONE_SUCCESS, NONE_FAILED)"
          },
          {
            "name": "run_job_task",
            "type": "object",
            "description": "The task triggers another job when the ``run_job_task`` field is present.",
            "children": [
              {
                "name": "job_id",
                "type": "integer",
                "description": ""
              },
              {
                "name": "dbt_commands",
                "type": "array",
                "description": "An array of commands to execute for jobs with the dbt task, for example ``\"dbt_commands\": [\"dbt deps\", \"dbt seed\", \"dbt deps\", \"dbt seed\", \"dbt run\"]`` ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
              },
              {
                "name": "jar_params",
                "type": "array",
                "description": "A list of parameters for jobs with Spark JAR tasks, for example ``\"jar_params\": [\"john doe\", \"35\"]``. The parameters are used to invoke the main function of the main class specified in the Spark JAR task. If not specified upon ``run-now``, it defaults to an empty list. jar_params cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example ``&#123;\"jar_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
              },
              {
                "name": "job_parameters",
                "type": "object",
                "description": "Job-level parameters used to trigger the job."
              },
              {
                "name": "notebook_params",
                "type": "object",
                "description": "A map from keys to values for jobs with notebook task, for example ``\"notebook_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;``. The map is passed to the notebook and is accessible through the `dbutils.widgets.get <https://docs.databricks.com/dev-tools/databricks-utils.html>`__ function. If not specified upon ``run-now``, the triggered run uses the job’s base parameters. notebook_params cannot be specified in conjunction with jar_params. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. The JSON representation of this field (for example ``&#123;\"notebook_params\":&#123;\"name\":\"john doe\",\"age\":\"35\"&#125;&#125;``) cannot exceed 10,000 bytes."
              },
              {
                "name": "pipeline_params",
                "type": "object",
                "description": "Controls whether the pipeline should perform a full refresh"
              },
              {
                "name": "python_named_params",
                "type": "object",
                "description": ""
              },
              {
                "name": "python_params",
                "type": "array",
                "description": "A list of parameters for jobs with Python tasks, for example ``\"python_params\": [\"john doe\", \"35\"]``. The parameters are passed to Python file as command-line parameters. If specified upon ``run-now``, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example ``&#123;\"python_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis."
              },
              {
                "name": "spark_submit_params",
                "type": "array",
                "description": "A list of parameters for jobs with spark submit task, for example ``\"spark_submit_params\": [\"--class\", \"org.apache.spark.examples.SparkPi\"]``. The parameters are passed to spark-submit script as command-line parameters. If specified upon ``run-now``, it would overwrite the parameters specified in job setting. The JSON representation of this field (for example ``&#123;\"python_params\":[\"john doe\",\"35\"]&#125;``) cannot exceed 10,000 bytes. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks. Important These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis."
              },
              {
                "name": "sql_params",
                "type": "object",
                "description": "A map from keys to values for jobs with SQL task, for example ``\"sql_params\": &#123;\"name\": \"john doe\", \"age\": \"35\"&#125;``. The SQL alert task does not support custom parameters. ⚠ **Deprecation note** Use `job parameters <https://docs.databricks.com/jobs/job-parameters.html#job-parameter-pushdown>`__ to pass information down to tasks."
              }
            ]
          },
          {
            "name": "run_page_url",
            "type": "string",
            "description": ""
          },
          {
            "name": "setup_duration",
            "type": "integer",
            "description": "The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the ``setup_duration``, ``execution_duration``, and the ``cleanup_duration``. The ``setup_duration`` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the ``run_duration`` field."
          },
          {
            "name": "spark_jar_task",
            "type": "object",
            "description": "The task runs a JAR when the ``spark_jar_task`` field is present.",
            "children": [
              {
                "name": "jar_uri",
                "type": "string",
                "description": ""
              },
              {
                "name": "main_class_name",
                "type": "string",
                "description": "The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library. The code must use ``SparkContext.getOrCreate`` to obtain a Spark context; otherwise, runs of the job fail."
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "Parameters passed to the main method. Use `Task parameter variables <https://docs.databricks.com/jobs.html#parameter-variables>`__ to set parameters containing information about job runs."
              },
              {
                "name": "run_as_repl",
                "type": "boolean",
                "description": "Deprecated. A value of ``false`` is no longer supported."
              }
            ]
          },
          {
            "name": "spark_python_task",
            "type": "object",
            "description": "The task runs a Python file when the ``spark_python_task`` field is present.",
            "children": [
              {
                "name": "python_file",
                "type": "string",
                "description": ""
              },
              {
                "name": "parameters",
                "type": "array",
                "description": "Command line parameters passed to the Python file. Use `Task parameter variables <https://docs.databricks.com/jobs.html#parameter-variables>`__ to set parameters containing information about job runs."
              },
              {
                "name": "source",
                "type": "string",
                "description": "Optional location type of the Python file. When set to ``WORKSPACE`` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the ``python_file`` has a URI format). When set to ``GIT``, the Python file will be retrieved from a Git repository defined in ``git_source``. - ``WORKSPACE``: The Python file is located in a Databricks workspace or at a cloud filesystem URI. - ``GIT``: The Python file is located in a remote Git repository. (GIT, WORKSPACE)"
              }
            ]
          },
          {
            "name": "spark_submit_task",
            "type": "object",
            "description": "(Legacy) The task runs the spark-submit script when the spark_submit_task field is present. Databricks recommends using the spark_jar_task instead; see [Spark Submit task for jobs](/jobs/spark-submit).",
            "children": [
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              }
            ]
          },
          {
            "name": "sql_task",
            "type": "object",
            "description": "The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the ``sql_task`` field is present.",
            "children": [
              {
                "name": "warehouse_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "alert",
                "type": "object",
                "description": "If alert, indicates that this job must refresh a SQL alert."
              },
              {
                "name": "dashboard",
                "type": "object",
                "description": "If dashboard, indicates that this job must refresh a SQL dashboard."
              },
              {
                "name": "file",
                "type": "object",
                "description": "If file, indicates that this job runs a SQL file in a remote Git repository."
              },
              {
                "name": "parameters",
                "type": "object",
                "description": "Parameters to be used for each run of this job. The SQL alert task does not support custom parameters."
              },
              {
                "name": "query",
                "type": "object",
                "description": "If query, indicates that this job must execute a SQL query."
              }
            ]
          },
          {
            "name": "start_time",
            "type": "integer",
            "description": "The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued."
          },
          {
            "name": "state",
            "type": "object",
            "description": "Deprecated. Please use the ``status`` field instead.",
            "children": [
              {
                "name": "life_cycle_state",
                "type": "string",
                "description": "A value indicating the run's current lifecycle state. This field is always available in the response. Note: Additional states might be introduced in future releases. (BLOCKED, INTERNAL_ERROR, PENDING, QUEUED, RUNNING, SKIPPED, TERMINATED, TERMINATING, WAITING_FOR_RETRY)"
              },
              {
                "name": "queue_reason",
                "type": "string",
                "description": "The reason indicating why the run was queued."
              },
              {
                "name": "result_state",
                "type": "string",
                "description": "A value indicating the run's result. This field is only available for terminal lifecycle states. Note: Additional states might be introduced in future releases. (CANCELED, DISABLED, EXCLUDED, FAILED, MAXIMUM_CONCURRENT_RUNS_REACHED, SUCCESS, SUCCESS_WITH_FAILURES, TIMEDOUT, UPSTREAM_CANCELED, UPSTREAM_FAILED)"
              },
              {
                "name": "state_message",
                "type": "string",
                "description": "A descriptive message for the current state. This field is unstructured, and its exact format is subject to change."
              },
              {
                "name": "user_cancelled_or_timedout",
                "type": "boolean",
                "description": "A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out."
              }
            ]
          },
          {
            "name": "status",
            "type": "object",
            "description": "The current status of the run",
            "children": [
              {
                "name": "queue_details",
                "type": "object",
                "description": "If the run was queued, details about the reason for queuing the run."
              },
              {
                "name": "state",
                "type": "string",
                "description": "The current state of the run. (BLOCKED, PENDING, QUEUED, RUNNING, TERMINATED, TERMINATING, WAITING)"
              },
              {
                "name": "termination_details",
                "type": "object",
                "description": "If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run."
              }
            ]
          },
          {
            "name": "timeout_seconds",
            "type": "integer",
            "description": "An optional timeout applied to each run of this job task. A value of ``0`` means no timeout."
          },
          {
            "name": "webhook_notifications",
            "type": "object",
            "description": "A collection of system notification IDs to notify when the run begins or completes. The default behavior is to not send any system notifications. Task webhooks respect the task notification settings.",
            "children": [
              {
                "name": "on_duration_warning_threshold_exceeded",
                "type": "array",
                "description": ""
              },
              {
                "name": "on_failure",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the ``on_failure`` property."
              },
              {
                "name": "on_maintenance_complete",
                "type": "array",
                "description": "An optional list of system notification IDs to call when platform-initiated maintenance completes for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_complete`` property."
              },
              {
                "name": "on_maintenance_start",
                "type": "array",
                "description": "An optional list of system notification IDs to call when platform-initiated maintenance starts for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_start`` property."
              },
              {
                "name": "on_start",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the ``on_start`` property."
              },
              {
                "name": "on_streaming_backlog_exceeded",
                "type": "array",
                "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the ``health`` field using the following metrics: ``STREAMING_BACKLOG_BYTES``, ``STREAMING_BACKLOG_RECORDS``, ``STREAMING_BACKLOG_SECONDS``, or ``STREAMING_BACKLOG_FILES``. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the ``on_streaming_backlog_exceeded`` property."
              },
              {
                "name": "on_success",
                "type": "array",
                "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the ``on_success`` property."
              }
            ]
          }
        ]
      },
      {
        "name": "trigger",
        "type": "string",
        "description": "The type of trigger that fired this run.<br /><br />- ``PERIODIC``: Schedules that periodically trigger runs, such as a cron scheduler.<br />- ``ONE_TIME``: One time triggers that fire a single run. This occurs you triggered a single run<br />  on demand through the UI or the API.<br />- ``RETRY``: Indicates a run that is triggered as a retry of a previously failed run. This<br />  occurs when you request to re-run the job in case of failures.<br />- ``RUN_JOB_TASK``: Indicates a run that is triggered using a Run Job task.<br />- ``FILE_ARRIVAL``: Indicates a run that is triggered by a file arrival.<br />- ``CONTINUOUS``: Indicates a run that is triggered by a continuous job.<br />- ``TABLE``: Indicates a run that is triggered by a table update.<br />- ``CONTINUOUS_RESTART``: Indicates a run created by user to manually restart a continuous job<br />  run.<br />- ``MODEL``: Indicates a run that is triggered by a model update. (CONTINUOUS, CONTINUOUS_RESTART, FILE_ARRIVAL, ONE_TIME, PERIODIC, RETRY, RUN_JOB_TASK, TABLE)"
      },
      {
        "name": "trigger_info",
        "type": "object",
        "description": "Additional details about what triggered the run",
        "children": [
          {
            "name": "run_id",
            "type": "integer",
            "description": "The run id of the Run Job task run"
          },
          {
            "name": "sql_condition",
            "type": "object",
            "description": "SQL condition evaluation details for this run",
            "children": [
              {
                "name": "condition_evaluation_satisfied",
                "type": "boolean",
                "description": "Whether the last condition evaluation was satisfied (query returned truthy result)."
              },
              {
                "name": "condition_evaluation_sql_session_id",
                "type": "string",
                "description": "The ID of the SQL session, used by the UI to track session context. Set for the QUERY_RETURNS_ROWS trigger mode."
              },
              {
                "name": "condition_evaluation_sql_statement_id",
                "type": "string",
                "description": "The SQL statement ID of the condition evaluation, set when the condition is evaluated by running a single SQL statement (the RESULT_VALUE_CHANGES trigger mode). The UI uses it to link to the query execution details."
              }
            ]
          }
        ]
      },
      {
        "name": "version_id",
        "type": "string",
        "description": "ID of the deployment version that produced the job when this run was created. Identifies a specific snapshot of the deployment in the Deployment Metadata service. Only set for job runs of jobs with a ``BUNDLE`` deployment."
      }
    ]
  },
  {
    "name": "notebook_output",
    "type": "object",
    "description": "The output of a notebook task, if available. A notebook task that terminates (either successfully or with a failure) without calling ``dbutils.notebook.exit()`` is considered to have an empty output. This field is set but its result value is empty. Databricks restricts this API to return the first 5 MB of the output. To return a larger result, use the `ClusterLogConf <https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterlogconf>`__ field to configure log storage for the job cluster.",
    "children": [
      {
        "name": "result",
        "type": "string",
        "description": ""
      },
      {
        "name": "truncated",
        "type": "boolean",
        "description": "Whether or not the result was truncated."
      }
    ]
  },
  {
    "name": "run_job_output",
    "type": "object",
    "description": "The output of a run job task, if available",
    "children": [
      {
        "name": "run_id",
        "type": "integer",
        "description": ""
      }
    ]
  },
  {
    "name": "sql_output",
    "type": "object",
    "description": "The output of a SQL task, if available.",
    "children": [
      {
        "name": "alert_output",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "alert_state",
            "type": "string",
            "description": "The state of the SQL alert.<br /><br />- UNKNOWN: alert yet to be evaluated<br />- OK: alert evaluated and did not fulfill trigger conditions<br />- TRIGGERED: alert evaluated and fulfilled trigger conditions (OK, TRIGGERED, UNKNOWN)"
          },
          {
            "name": "output_link",
            "type": "string",
            "description": "The link to find the output results."
          },
          {
            "name": "query_text",
            "type": "string",
            "description": "The text of the SQL query. Can Run permission of the SQL query associated with the SQL alert is required to view this field."
          },
          {
            "name": "sql_statements",
            "type": "array",
            "description": "Information about SQL statements executed in the run.",
            "children": [
              {
                "name": "lookup_key",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "The canonical identifier of the SQL warehouse."
          }
        ]
      },
      {
        "name": "dashboard_output",
        "type": "object",
        "description": "The output of a SQL dashboard task, if available.",
        "children": [
          {
            "name": "warehouse_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "widgets",
            "type": "array",
            "description": "Widgets executed in the run. Only SQL query based widgets are listed.",
            "children": [
              {
                "name": "end_time",
                "type": "integer",
                "description": ""
              },
              {
                "name": "error",
                "type": "object",
                "description": "The information about the error when execution fails."
              },
              {
                "name": "output_link",
                "type": "string",
                "description": "The link to find the output results."
              },
              {
                "name": "start_time",
                "type": "integer",
                "description": "Time (in epoch milliseconds) when execution of the SQL widget starts."
              },
              {
                "name": "status",
                "type": "string",
                "description": "The execution status of the SQL widget. (CANCELLED, FAILED, PENDING, RUNNING, SUCCESS)"
              },
              {
                "name": "widget_id",
                "type": "string",
                "description": "The canonical identifier of the SQL widget."
              },
              {
                "name": "widget_title",
                "type": "string",
                "description": "The title of the SQL widget."
              }
            ]
          }
        ]
      },
      {
        "name": "query_output",
        "type": "object",
        "description": "The output of a SQL query task, if available.",
        "children": [
          {
            "name": "endpoint_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "output_link",
            "type": "string",
            "description": "The link to find the output results."
          },
          {
            "name": "query_text",
            "type": "string",
            "description": "The text of the SQL query. Can Run permission of the SQL query is required to view this field."
          },
          {
            "name": "sql_statements",
            "type": "array",
            "description": "Information about SQL statements executed in the run.",
            "children": [
              {
                "name": "lookup_key",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "warehouse_id",
            "type": "string",
            "description": "The canonical identifier of the SQL warehouse."
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
    <td><a href="#get_output"><CopyableCode code="get_output" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieve the output and metadata of a single task run. When a notebook task returns a value through</td>
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
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>integer</code></td>
    <td>The canonical identifier for the run.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_output"
    values={[
        { label: 'get_output', value: 'get_output' }
    ]}
>
<TabItem value="get_output">

Retrieve the output and metadata of a single task run. When a notebook task returns a value through

```sql
SELECT
agentic_task_output,
ai_runtime_task_output,
alert_output,
clean_rooms_notebook_output,
dashboard_output,
dbt_cloud_output,
dbt_output,
dbt_platform_output,
error,
error_trace,
genie_task_output,
info,
logs,
logs_truncated,
metadata,
notebook_output,
run_job_output,
sql_output
FROM databricks_workspace.jobs.job_run_output
WHERE run_id = '{{ run_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>
