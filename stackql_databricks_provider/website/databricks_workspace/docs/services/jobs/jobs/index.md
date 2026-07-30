---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.jobs.jobs" /></td></tr>
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
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "The id of the budget policy used by this job for cost attribution purposes. This may be set through (in order of precedence): 1. Budget admins through the account or workspace console 2. Jobs UI in the job details page and Jobs API using ``budget_policy_id`` 3. Inferred default based on accessible budget policies of the run_as identity on job creation or modification."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The id of the usage policy used by this job for cost attribution purposes."
  },
  {
    "name": "job_id",
    "type": "integer",
    "description": "The canonical identifier for this job."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The creator user name. This field won’t be included in the response if the user has already been deleted."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "The email of an active workspace user or the application ID of a service principal that the job runs as. This value can be changed by setting the ``run_as`` field when creating or updating a job. By default, ``run_as_user_name`` is based on the current job settings and is set to the creator of the job if job access control is disabled or to the user with the ``is_owner`` permission if job access control is enabled."
  },
  {
    "name": "created_time",
    "type": "integer",
    "description": "The time at which this job was created in epoch milliseconds (milliseconds since 1/1/1970 UTC)."
  },
  {
    "name": "has_more",
    "type": "boolean",
    "description": "Indicates if the job has more array properties (``tasks``, ``job_clusters``) that are not shown. They can be accessed via :method:jobs/get endpoint. It is only relevant for API 2.2 :method:jobs/list requests with ``expand_tasks=true``."
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "A token that can be used to list the next page of array properties."
  },
  {
    "name": "path",
    "type": "string",
    "description": "Path of the job object in workspace file tree, including file extension. If absent, the job doesn't have a workspace object. Example: /Workspace/user@example.com/my_project/my_job.job.json"
  },
  {
    "name": "settings",
    "type": "object",
    "description": "Settings for this job and all of its runs. These settings can be updated using the ``resetJob`` method.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "continuous",
        "type": "object",
        "description": "An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of ``schedule`` and ``continuous`` can be used.",
        "children": [
          {
            "name": "maintenance_window",
            "type": "object",
            "description": "A recurring weekly time window during which platform-initiated maintenance is allowed to run for<br />    a continuous job.",
            "children": [
              {
                "name": "start_hour",
                "type": "integer",
                "description": "An integer between 0 and 23 denoting the start hour for the maintenance window in the 24-hour day. Platform-initiated maintenance is triggered only within a one-hour window starting at this hour. This field is required."
              },
              {
                "name": "day_of_week",
                "type": "string",
                "description": "The day of week on which maintenance is allowed to happen. This field is required. (FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY)"
              },
              {
                "name": "timezone_id",
                "type": "string",
                "description": "A Java timezone ID. The maintenance window is resolved with respect to this timezone. See `Java TimeZone <https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html>`__ for details. This field is required."
              }
            ]
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Indicate whether the continuous execution of the job is paused or not. Defaults to UNPAUSED. (PAUSED, UNPAUSED)"
          },
          {
            "name": "task_retry_mode",
            "type": "string",
            "description": "Indicate whether the continuous job is applying task level retries or not. Defaults to NEVER. (NEVER, ON_FAILURE)"
          }
        ]
      },
      {
        "name": "deployment",
        "type": "object",
        "description": "Deployment information for jobs managed by external sources.",
        "children": [
          {
            "name": "kind",
            "type": "string",
            "description": "- ``BUNDLE``: The job is managed by Databricks Asset Bundle.<br />- ``SYSTEM_MANAGED``: The job is managed by Databricks and is read-only. (BUNDLE, SYSTEM_MANAGED)"
          },
          {
            "name": "deployment_id",
            "type": "string",
            "description": "ID of the deployment that manages this job. Only set when ``kind`` is ``BUNDLE``. Used to look up deployment metadata from the Deployment Metadata service."
          },
          {
            "name": "metadata_file_path",
            "type": "string",
            "description": "Path of the file that contains deployment metadata."
          },
          {
            "name": "version_id",
            "type": "string",
            "description": "ID of the version of the deployment that produced this job. Only set when ``kind`` is ``BUNDLE``. Identifies a specific snapshot of the deployment in the Deployment Metadata service."
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding."
      },
      {
        "name": "edit_mode",
        "type": "string",
        "description": "Edit mode of the job. - ``UI_LOCKED``: The job is in a locked UI state and cannot be modified. - ``EDITABLE``: The job is in an editable state and can be modified. (EDITABLE, UI_LOCKED)"
      },
      {
        "name": "email_notifications",
        "type": "object",
        "description": "An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.",
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
        "name": "environment_variables",
        "type": "array",
        "description": "Named environment-variable entries that tasks can reference by key from ``TaskSettings.environment_variables_key``. Each entry holds inline ``variables`` plus optional ``.env`` ``files``. Maximum 10 entries per job. Entries are independent of one another — there is no cross-entry merging.",
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
        "name": "environments",
        "type": "array",
        "description": "A list of task execution environment specifications that can be referenced by serverless tasks of this job. For serverless notebook tasks, if the environment_key is not specified, the notebook environment will be used if present. If a jobs environment is specified, it will override the notebook environment. For other serverless tasks, the task environment is required to be specified using environment_key in the task settings.",
        "children": [
          {
            "name": "environment_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "spec",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "format",
        "type": "string",
        "description": "Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to ``\"MULTI_TASK\"``. (MULTI_TASK, SINGLE_TASK)"
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
        "name": "health",
        "type": "object",
        "description": "An optional set of health rules that can be defined for this job.",
        "children": [
          {
            "name": "rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "metric",
                "type": "string",
                "description": "Specifies the health metric that is being evaluated for a particular health rule.<br /><br />- ``RUN_DURATION_SECONDS``: Expected total time for a run in seconds.<br />- ``STREAMING_BACKLOG_BYTES``: An estimate of the maximum bytes of data waiting to be consumed<br />  across all streams. This metric is in Public Preview.<br />- ``STREAMING_BACKLOG_RECORDS``: An estimate of the maximum offset lag across all streams. This<br />  metric is in Public Preview.<br />- ``STREAMING_BACKLOG_SECONDS``: An estimate of the maximum consumer delay across all streams.<br />  This metric is in Public Preview.<br />- ``STREAMING_BACKLOG_FILES``: An estimate of the maximum number of outstanding files across all<br />  streams. This metric is in Public Preview. (RUN_DURATION_SECONDS, STREAMING_BACKLOG_BYTES, STREAMING_BACKLOG_FILES, STREAMING_BACKLOG_RECORDS, STREAMING_BACKLOG_SECONDS)"
              },
              {
                "name": "op",
                "type": "string",
                "description": "Specifies the operator used to compare the health metric value with the specified threshold. (GREATER_THAN)"
              },
              {
                "name": "value",
                "type": "integer",
                "description": "Specifies the threshold value that the health metric should obey to satisfy the health rule."
              }
            ]
          }
        ]
      },
      {
        "name": "job_clusters",
        "type": "array",
        "description": "A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.",
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
        "name": "max_concurrent_runs",
        "type": "integer",
        "description": "An optional maximum allowed number of concurrent runs of the job. Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters. This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs. This value cannot exceed 1000. Setting this value to ``0`` causes all new runs to be skipped."
      },
      {
        "name": "name",
        "type": "string",
        "description": "An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding."
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Optional notification settings that are used when sending notifications to each of the ``email_notifications`` and ``webhook_notifications`` for this job.",
        "children": [
          {
            "name": "no_alert_for_canceled_runs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in ``on_failure`` if the run is skipped."
          }
        ]
      },
      {
        "name": "parameters",
        "type": "array",
        "description": "Job-level parameter definitions",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "default",
            "type": "string",
            "description": "Default value of the parameter."
          }
        ]
      },
      {
        "name": "parent_path",
        "type": "string",
        "description": "Path of the job parent folder in workspace file tree. If absent, the job doesn't have a workspace object."
      },
      {
        "name": "performance_target",
        "type": "string",
        "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget). (PERFORMANCE_OPTIMIZED, STANDARD)"
      },
      {
        "name": "queue",
        "type": "object",
        "description": "The queue settings of the job.",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "run_as",
        "type": "object",
        "description": "The user or service principal that the job runs as, if specified in the request. This field indicates the explicit configuration of ``run_as`` for the job. To find the value in all cases, explicit or implicit, use ``run_as_user_name``.",
        "children": [
          {
            "name": "group_name",
            "type": "string",
            "description": "Group name of an account group assigned to the workspace. Setting this field requires being a member of the group."
          },
          {
            "name": "service_principal_name",
            "type": "string",
            "description": "Application ID of an active service principal. Setting this field requires the ``servicePrincipal/user`` role."
          },
          {
            "name": "user_name",
            "type": "string",
            "description": "The email of an active workspace user. Non-admin users can only set this field to their own email."
          }
        ]
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to ``runNow``.",
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
        "name": "tags",
        "type": "object",
        "description": "A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job."
      },
      {
        "name": "tasks",
        "type": "array",
        "description": "A list of task specifications to be executed by this job. It supports up to 1000 elements in write endpoints (:method:jobs/create, :method:jobs/reset, :method:jobs/update, :method:jobs/submit). Read endpoints return only 100 tasks. If more than 100 tasks are available, you can paginate through them using :method:jobs/get. Use the ``next_page_token`` field at the object root to determine if more results are available.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": ""
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
            "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the ``run_if`` condition is true. The key is ``task_key``, and the value is the name assigned to the dependent task.",
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
            "name": "email_notifications",
            "type": "object",
            "description": "An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails.",
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
            "name": "environment_key",
            "type": "string",
            "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
          },
          {
            "name": "environment_variables_key",
            "type": "string",
            "description": "Reference to a ``JobEnvironmentVariables`` entry defined in ``JobSettings.environment_variables``. The selected entry's variables and file contents are applied to this task at execution time. Length and pattern mirror ``environment_key`` so the two references look identical to customers reading task settings."
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
            "name": "health",
            "type": "object",
            "description": "An optional set of health rules that can be defined for this job.",
            "children": [
              {
                "name": "rules",
                "type": "array",
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
            "description": "Optional notification settings that are used when sending notifications to each of the ``email_notifications`` and ``webhook_notifications`` for this task.",
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
            "name": "retry_on_timeout",
            "type": "boolean",
            "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
          },
          {
            "name": "run_if",
            "type": "string",
            "description": "An optional value specifying the condition determining whether the task is run once its dependencies have been completed. - ``ALL_SUCCESS``: All dependencies have executed and succeeded - ``AT_LEAST_ONE_SUCCESS``: At least one dependency has succeeded - ``NONE_FAILED``: None of the dependencies have failed and at least one was executed - ``ALL_DONE``: All dependencies have been completed - ``AT_LEAST_ONE_FAILED``: At least one dependency failed - ``ALL_FAILED``: ALl dependencies have failed (ALL_DONE, ALL_FAILED, ALL_SUCCESS, AT_LEAST_ONE_FAILED, AT_LEAST_ONE_SUCCESS, NONE_FAILED)"
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
            "name": "timeout_seconds",
            "type": "integer",
            "description": "An optional timeout applied to each run of this job task. A value of ``0`` means no timeout."
          },
          {
            "name": "webhook_notifications",
            "type": "object",
            "description": "A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications.",
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
        "name": "timeout_seconds",
        "type": "integer",
        "description": "An optional timeout applied to each run of this job. A value of ``0`` means no timeout."
      },
      {
        "name": "trigger",
        "type": "object",
        "description": "A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to ``runNow``.",
        "children": [
          {
            "name": "file_arrival",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": ""
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time passed since the last time the trigger fired. The minimum allowed value is 60 seconds"
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no file activity has occurred for the specified amount of time. This makes it possible to wait for a batch of incoming files to arrive before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "model",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "condition",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (MODEL_ALIAS_SET, MODEL_CREATED, MODEL_VERSION_READY)"
              },
              {
                "name": "aliases",
                "type": "array",
                "description": "Aliases of the model versions to monitor. Can only be used in conjunction with condition MODEL_ALIAS_SET."
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "securable_name",
                "type": "string",
                "description": "Name of the securable to monitor (\"mycatalog.myschema.mymodel\" in the case of model-level triggers, \"mycatalog.myschema\" in the case of schema-level triggers) or empty in the case of metastore-level triggers."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no model updates have occurred for the specified time and can be used to wait for a series of model updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Whether this trigger is paused or not. (PAUSED, UNPAUSED)"
          },
          {
            "name": "periodic",
            "type": "object",
            "description": "Periodic trigger settings.",
            "children": [
              {
                "name": "interval",
                "type": "integer",
                "description": ""
              },
              {
                "name": "unit",
                "type": "string",
                "description": "The unit of time for the interval. (DAYS, HOURS, MINUTES, WEEKS)"
              }
            ]
          },
          {
            "name": "sql_condition",
            "type": "object",
            "description": "SQL condition that must be satisfied for the trigger to fire. Can be used in combination with other trigger types and runs *after* other trigger types conditions are evaluated.",
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
          },
          {
            "name": "table_update",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "table_names",
                "type": "array",
                "description": ""
              },
              {
                "name": "condition",
                "type": "string",
                "description": "The table(s) condition based on which to trigger a job run. (ALL_UPDATED, ANY_UPDATED)"
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no table updates have occurred for the specified time and can be used to wait for a series of table updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          }
        ]
      },
      {
        "name": "usage_policy_id",
        "type": "string",
        "description": "The id of the user specified usage policy to use for this job. If not specified, a default usage policy may be applied when creating or modifying the job. See ``effective_usage_policy_id`` for the usage policy used by this workload."
      },
      {
        "name": "webhook_notifications",
        "type": "object",
        "description": "A collection of system notification IDs to notify when runs of this job begin or complete.",
        "children": [
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the ``on_failure`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_maintenance_complete",
            "type": "array",
            "description": "An optional list of system notification IDs to call when platform-initiated maintenance completes for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_complete`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_maintenance_start",
            "type": "array",
            "description": "An optional list of system notification IDs to call when platform-initiated maintenance starts for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_start`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the ``on_start`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the ``health`` field using the following metrics: ``STREAMING_BACKLOG_BYTES``, ``STREAMING_BACKLOG_RECORDS``, ``STREAMING_BACKLOG_SECONDS``, or ``STREAMING_BACKLOG_FILES``. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the ``on_streaming_backlog_exceeded`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the ``on_success`` property.",
            "children": [
              {
                "name": "id",
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
    "name": "trigger_state",
    "type": "object",
    "description": "State of the trigger associated with the job.",
    "children": [
      {
        "name": "file_arrival",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "using_file_events",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Whether this trigger is paused or not. For continuous schedules, it can differ from the configured pause_status whenever a paused continuous job is kickstarted by an operation other than an update, such as a run-now. (PAUSED, UNPAUSED)"
      },
      {
        "name": "sql_condition",
        "type": "object",
        "description": "State for SQL condition evaluation, can coexist with other trigger states.",
        "children": [
          {
            "name": "latest_condition_evaluation_satisfied",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "latest_condition_evaluation_sql_session_id",
            "type": "string",
            "description": "The ID of the SQL session, used by UI to track session context. Populated for QUERY_RETURNS_ROWS, which executes the query through Redash."
          },
          {
            "name": "latest_condition_evaluation_sql_statement_id",
            "type": "string",
            "description": "The SEA statement ID of the SQL statement executed for the latest condition evaluation. Populated for RESULT_VALUE_CHANGES, which executes the query through the SQL execution API."
          }
        ]
      },
      {
        "name": "table",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "last_seen_table_states",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "has_seen_updates",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "table_name",
                "type": "string",
                "description": "Full table name of the table to monitor, e.g. ``mycatalog.myschema.mytable``"
              }
            ]
          },
          {
            "name": "using_scalable_monitoring",
            "type": "boolean",
            "description": "Indicates whether the trigger is using scalable monitoring."
          }
        ]
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": "The id of the budget policy used by this job for cost attribution purposes. This may be set through (in order of precedence): 1. Budget admins through the account or workspace console 2. Jobs UI in the job details page and Jobs API using ``budget_policy_id`` 3. Inferred default based on accessible budget policies of the run_as identity on job creation or modification."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The id of the usage policy used by this job for cost attribution purposes."
  },
  {
    "name": "job_id",
    "type": "integer",
    "description": "The canonical identifier for this job."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "The creator user name. This field won’t be included in the response if the user has already been deleted."
  },
  {
    "name": "created_time",
    "type": "integer",
    "description": ""
  },
  {
    "name": "has_more",
    "type": "boolean",
    "description": "Indicates if the job has more array properties (``tasks``, ``job_clusters``) that are not shown. They can be accessed via :method:jobs/get endpoint. It is only relevant for API 2.2 :method:jobs/list requests with ``expand_tasks=true``."
  },
  {
    "name": "path",
    "type": "string",
    "description": "Path of the job object in workspace file tree, including file extension. If absent, the job doesn't have a workspace object. Example: /Workspace/user@example.com/my_project/my_job.job.json"
  },
  {
    "name": "settings",
    "type": "object",
    "description": "Settings for this job and all of its runs. These settings can be updated using the ``resetJob`` method.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "continuous",
        "type": "object",
        "description": "An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of ``schedule`` and ``continuous`` can be used.",
        "children": [
          {
            "name": "maintenance_window",
            "type": "object",
            "description": "A recurring weekly time window during which platform-initiated maintenance is allowed to run for<br />    a continuous job.",
            "children": [
              {
                "name": "start_hour",
                "type": "integer",
                "description": "An integer between 0 and 23 denoting the start hour for the maintenance window in the 24-hour day. Platform-initiated maintenance is triggered only within a one-hour window starting at this hour. This field is required."
              },
              {
                "name": "day_of_week",
                "type": "string",
                "description": "The day of week on which maintenance is allowed to happen. This field is required. (FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY)"
              },
              {
                "name": "timezone_id",
                "type": "string",
                "description": "A Java timezone ID. The maintenance window is resolved with respect to this timezone. See `Java TimeZone <https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html>`__ for details. This field is required."
              }
            ]
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Indicate whether the continuous execution of the job is paused or not. Defaults to UNPAUSED. (PAUSED, UNPAUSED)"
          },
          {
            "name": "task_retry_mode",
            "type": "string",
            "description": "Indicate whether the continuous job is applying task level retries or not. Defaults to NEVER. (NEVER, ON_FAILURE)"
          }
        ]
      },
      {
        "name": "deployment",
        "type": "object",
        "description": "Deployment information for jobs managed by external sources.",
        "children": [
          {
            "name": "kind",
            "type": "string",
            "description": "- ``BUNDLE``: The job is managed by Databricks Asset Bundle.<br />- ``SYSTEM_MANAGED``: The job is managed by Databricks and is read-only. (BUNDLE, SYSTEM_MANAGED)"
          },
          {
            "name": "deployment_id",
            "type": "string",
            "description": "ID of the deployment that manages this job. Only set when ``kind`` is ``BUNDLE``. Used to look up deployment metadata from the Deployment Metadata service."
          },
          {
            "name": "metadata_file_path",
            "type": "string",
            "description": "Path of the file that contains deployment metadata."
          },
          {
            "name": "version_id",
            "type": "string",
            "description": "ID of the version of the deployment that produced this job. Only set when ``kind`` is ``BUNDLE``. Identifies a specific snapshot of the deployment in the Deployment Metadata service."
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding."
      },
      {
        "name": "edit_mode",
        "type": "string",
        "description": "Edit mode of the job. - ``UI_LOCKED``: The job is in a locked UI state and cannot be modified. - ``EDITABLE``: The job is in an editable state and can be modified. (EDITABLE, UI_LOCKED)"
      },
      {
        "name": "email_notifications",
        "type": "object",
        "description": "An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.",
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
        "name": "environment_variables",
        "type": "array",
        "description": "Named environment-variable entries that tasks can reference by key from ``TaskSettings.environment_variables_key``. Each entry holds inline ``variables`` plus optional ``.env`` ``files``. Maximum 10 entries per job. Entries are independent of one another — there is no cross-entry merging.",
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
        "name": "environments",
        "type": "array",
        "description": "A list of task execution environment specifications that can be referenced by serverless tasks of this job. For serverless notebook tasks, if the environment_key is not specified, the notebook environment will be used if present. If a jobs environment is specified, it will override the notebook environment. For other serverless tasks, the task environment is required to be specified using environment_key in the task settings.",
        "children": [
          {
            "name": "environment_key",
            "type": "string",
            "description": ""
          },
          {
            "name": "spec",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "format",
        "type": "string",
        "description": "Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to ``\"MULTI_TASK\"``. (MULTI_TASK, SINGLE_TASK)"
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
        "name": "health",
        "type": "object",
        "description": "An optional set of health rules that can be defined for this job.",
        "children": [
          {
            "name": "rules",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "metric",
                "type": "string",
                "description": "Specifies the health metric that is being evaluated for a particular health rule.<br /><br />- ``RUN_DURATION_SECONDS``: Expected total time for a run in seconds.<br />- ``STREAMING_BACKLOG_BYTES``: An estimate of the maximum bytes of data waiting to be consumed<br />  across all streams. This metric is in Public Preview.<br />- ``STREAMING_BACKLOG_RECORDS``: An estimate of the maximum offset lag across all streams. This<br />  metric is in Public Preview.<br />- ``STREAMING_BACKLOG_SECONDS``: An estimate of the maximum consumer delay across all streams.<br />  This metric is in Public Preview.<br />- ``STREAMING_BACKLOG_FILES``: An estimate of the maximum number of outstanding files across all<br />  streams. This metric is in Public Preview. (RUN_DURATION_SECONDS, STREAMING_BACKLOG_BYTES, STREAMING_BACKLOG_FILES, STREAMING_BACKLOG_RECORDS, STREAMING_BACKLOG_SECONDS)"
              },
              {
                "name": "op",
                "type": "string",
                "description": "Specifies the operator used to compare the health metric value with the specified threshold. (GREATER_THAN)"
              },
              {
                "name": "value",
                "type": "integer",
                "description": "Specifies the threshold value that the health metric should obey to satisfy the health rule."
              }
            ]
          }
        ]
      },
      {
        "name": "job_clusters",
        "type": "array",
        "description": "A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.",
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
        "name": "max_concurrent_runs",
        "type": "integer",
        "description": "An optional maximum allowed number of concurrent runs of the job. Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters. This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs. This value cannot exceed 1000. Setting this value to ``0`` causes all new runs to be skipped."
      },
      {
        "name": "name",
        "type": "string",
        "description": "An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding."
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Optional notification settings that are used when sending notifications to each of the ``email_notifications`` and ``webhook_notifications`` for this job.",
        "children": [
          {
            "name": "no_alert_for_canceled_runs",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "no_alert_for_skipped_runs",
            "type": "boolean",
            "description": "If true, do not send notifications to recipients specified in ``on_failure`` if the run is skipped."
          }
        ]
      },
      {
        "name": "parameters",
        "type": "array",
        "description": "Job-level parameter definitions",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "default",
            "type": "string",
            "description": "Default value of the parameter."
          }
        ]
      },
      {
        "name": "parent_path",
        "type": "string",
        "description": "Path of the job parent folder in workspace file tree. If absent, the job doesn't have a workspace object."
      },
      {
        "name": "performance_target",
        "type": "string",
        "description": "PerformanceTarget defines how performant (lower latency) or cost efficient the execution of run<br />on serverless compute should be. The performance mode on the job or pipeline should map to a<br />performance setting that is passed to Cluster Manager (see cluster-common PerformanceTarget). (PERFORMANCE_OPTIMIZED, STANDARD)"
      },
      {
        "name": "queue",
        "type": "object",
        "description": "The queue settings of the job.",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "run_as",
        "type": "object",
        "description": "The user or service principal that the job runs as, if specified in the request. This field indicates the explicit configuration of ``run_as`` for the job. To find the value in all cases, explicit or implicit, use ``run_as_user_name``.",
        "children": [
          {
            "name": "group_name",
            "type": "string",
            "description": "Group name of an account group assigned to the workspace. Setting this field requires being a member of the group."
          },
          {
            "name": "service_principal_name",
            "type": "string",
            "description": "Application ID of an active service principal. Setting this field requires the ``servicePrincipal/user`` role."
          },
          {
            "name": "user_name",
            "type": "string",
            "description": "The email of an active workspace user. Non-admin users can only set this field to their own email."
          }
        ]
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to ``runNow``.",
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
        "name": "tags",
        "type": "object",
        "description": "A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job."
      },
      {
        "name": "tasks",
        "type": "array",
        "description": "A list of task specifications to be executed by this job. It supports up to 1000 elements in write endpoints (:method:jobs/create, :method:jobs/reset, :method:jobs/update, :method:jobs/submit). Read endpoints return only 100 tasks. If more than 100 tasks are available, you can paginate through them using :method:jobs/get. Use the ``next_page_token`` field at the object root to determine if more results are available.",
        "children": [
          {
            "name": "task_key",
            "type": "string",
            "description": ""
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
            "description": "An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the ``run_if`` condition is true. The key is ``task_key``, and the value is the name assigned to the dependent task.",
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
            "name": "email_notifications",
            "type": "object",
            "description": "An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails.",
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
            "name": "environment_key",
            "type": "string",
            "description": "The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute."
          },
          {
            "name": "environment_variables_key",
            "type": "string",
            "description": "Reference to a ``JobEnvironmentVariables`` entry defined in ``JobSettings.environment_variables``. The selected entry's variables and file contents are applied to this task at execution time. Length and pattern mirror ``environment_key`` so the two references look identical to customers reading task settings."
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
            "name": "health",
            "type": "object",
            "description": "An optional set of health rules that can be defined for this job.",
            "children": [
              {
                "name": "rules",
                "type": "array",
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
            "description": "Optional notification settings that are used when sending notifications to each of the ``email_notifications`` and ``webhook_notifications`` for this task.",
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
            "name": "retry_on_timeout",
            "type": "boolean",
            "description": "An optional policy to specify whether to retry a job when it times out. The default behavior is to not retry on timeout."
          },
          {
            "name": "run_if",
            "type": "string",
            "description": "An optional value specifying the condition determining whether the task is run once its dependencies have been completed. - ``ALL_SUCCESS``: All dependencies have executed and succeeded - ``AT_LEAST_ONE_SUCCESS``: At least one dependency has succeeded - ``NONE_FAILED``: None of the dependencies have failed and at least one was executed - ``ALL_DONE``: All dependencies have been completed - ``AT_LEAST_ONE_FAILED``: At least one dependency failed - ``ALL_FAILED``: ALl dependencies have failed (ALL_DONE, ALL_FAILED, ALL_SUCCESS, AT_LEAST_ONE_FAILED, AT_LEAST_ONE_SUCCESS, NONE_FAILED)"
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
            "name": "timeout_seconds",
            "type": "integer",
            "description": "An optional timeout applied to each run of this job task. A value of ``0`` means no timeout."
          },
          {
            "name": "webhook_notifications",
            "type": "object",
            "description": "A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications.",
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
        "name": "timeout_seconds",
        "type": "integer",
        "description": "An optional timeout applied to each run of this job. A value of ``0`` means no timeout."
      },
      {
        "name": "trigger",
        "type": "object",
        "description": "A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to ``runNow``.",
        "children": [
          {
            "name": "file_arrival",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "url",
                "type": "string",
                "description": ""
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time passed since the last time the trigger fired. The minimum allowed value is 60 seconds"
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no file activity has occurred for the specified amount of time. This makes it possible to wait for a batch of incoming files to arrive before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "model",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "condition",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (MODEL_ALIAS_SET, MODEL_CREATED, MODEL_VERSION_READY)"
              },
              {
                "name": "aliases",
                "type": "array",
                "description": "Aliases of the model versions to monitor. Can only be used in conjunction with condition MODEL_ALIAS_SET."
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "securable_name",
                "type": "string",
                "description": "Name of the securable to monitor (\"mycatalog.myschema.mymodel\" in the case of model-level triggers, \"mycatalog.myschema\" in the case of schema-level triggers) or empty in the case of metastore-level triggers."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no model updates have occurred for the specified time and can be used to wait for a series of model updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Whether this trigger is paused or not. (PAUSED, UNPAUSED)"
          },
          {
            "name": "periodic",
            "type": "object",
            "description": "Periodic trigger settings.",
            "children": [
              {
                "name": "interval",
                "type": "integer",
                "description": ""
              },
              {
                "name": "unit",
                "type": "string",
                "description": "The unit of time for the interval. (DAYS, HOURS, MINUTES, WEEKS)"
              }
            ]
          },
          {
            "name": "sql_condition",
            "type": "object",
            "description": "SQL condition that must be satisfied for the trigger to fire. Can be used in combination with other trigger types and runs *after* other trigger types conditions are evaluated.",
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
          },
          {
            "name": "table_update",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "table_names",
                "type": "array",
                "description": ""
              },
              {
                "name": "condition",
                "type": "string",
                "description": "The table(s) condition based on which to trigger a job run. (ALL_UPDATED, ANY_UPDATED)"
              },
              {
                "name": "min_time_between_triggers_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after the specified amount of time has passed since the last time the trigger fired. The minimum allowed value is 60 seconds."
              },
              {
                "name": "wait_after_last_change_seconds",
                "type": "integer",
                "description": "If set, the trigger starts a run only after no table updates have occurred for the specified time and can be used to wait for a series of table updates before triggering a run. The minimum allowed value is 60 seconds."
              }
            ]
          }
        ]
      },
      {
        "name": "usage_policy_id",
        "type": "string",
        "description": "The id of the user specified usage policy to use for this job. If not specified, a default usage policy may be applied when creating or modifying the job. See ``effective_usage_policy_id`` for the usage policy used by this workload."
      },
      {
        "name": "webhook_notifications",
        "type": "object",
        "description": "A collection of system notification IDs to notify when runs of this job begin or complete.",
        "children": [
          {
            "name": "on_duration_warning_threshold_exceeded",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_failure",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the ``on_failure`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_maintenance_complete",
            "type": "array",
            "description": "An optional list of system notification IDs to call when platform-initiated maintenance completes for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_complete`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_maintenance_start",
            "type": "array",
            "description": "An optional list of system notification IDs to call when platform-initiated maintenance starts for a continuous job. A maximum of 3 destinations can be specified for the ``on_maintenance_start`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_start",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the ``on_start`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_streaming_backlog_exceeded",
            "type": "array",
            "description": "An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream. Streaming backlog thresholds can be set in the ``health`` field using the following metrics: ``STREAMING_BACKLOG_BYTES``, ``STREAMING_BACKLOG_RECORDS``, ``STREAMING_BACKLOG_SECONDS``, or ``STREAMING_BACKLOG_FILES``. Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes. A maximum of 3 destinations can be specified for the ``on_streaming_backlog_exceeded`` property.",
            "children": [
              {
                "name": "id",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "on_success",
            "type": "array",
            "description": "An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the ``on_success`` property.",
            "children": [
              {
                "name": "id",
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
    "name": "trigger_state",
    "type": "object",
    "description": "State of the trigger associated with the job.",
    "children": [
      {
        "name": "file_arrival",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "using_file_events",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Whether this trigger is paused or not. For continuous schedules, it can differ from the configured pause_status whenever a paused continuous job is kickstarted by an operation other than an update, such as a run-now. (PAUSED, UNPAUSED)"
      },
      {
        "name": "sql_condition",
        "type": "object",
        "description": "State for SQL condition evaluation, can coexist with other trigger states.",
        "children": [
          {
            "name": "latest_condition_evaluation_satisfied",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "latest_condition_evaluation_sql_session_id",
            "type": "string",
            "description": "The ID of the SQL session, used by UI to track session context. Populated for QUERY_RETURNS_ROWS, which executes the query through Redash."
          },
          {
            "name": "latest_condition_evaluation_sql_statement_id",
            "type": "string",
            "description": "The SEA statement ID of the SQL statement executed for the latest condition evaluation. Populated for RESULT_VALUE_CHANGES, which executes the query through the SQL execution API."
          }
        ]
      },
      {
        "name": "table",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "last_seen_table_states",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "has_seen_updates",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "table_name",
                "type": "string",
                "description": "Full table name of the table to monitor, e.g. ``mycatalog.myschema.mytable``"
              }
            ]
          },
          {
            "name": "using_scalable_monitoring",
            "type": "boolean",
            "description": "Indicates whether the trigger is using scalable monitoring."
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-include_trigger_state"><code>include_trigger_state</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Retrieves the details for a single job.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-expand_tasks"><code>expand_tasks</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Retrieves a list of jobs.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Create a new job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Add, update, or remove specific settings of an existing job. Use the [*Reset*</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-new_settings"><code>new_settings</code></a></td>
    <td></td>
    <td>Overwrite all settings for the given job. Use the [*Update* endpoint](:method:jobs/update) to update</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a job.</td>
</tr>
<tr>
    <td><a href="#run_now"><CopyableCode code="run_now" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Run a job and return the ``run_id`` of the triggered run.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>integer</code></td>
    <td>The canonical identifier of the job to retrieve information about. This field is required.</td>
</tr>
<tr id="parameter-expand_tasks">
    <td><CopyableCode code="expand_tasks" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include task and cluster details in the response. Note that only the first 100 elements will be shown. Use :method:jobs/get to paginate through all tasks and clusters.</td>
</tr>
<tr id="parameter-include_trigger_state">
    <td><CopyableCode code="include_trigger_state" /></td>
    <td><code>boolean</code></td>
    <td>Flag that indicates that trigger state should be included in the response.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>The number of jobs to return. This value must be greater than 0 and less or equal to 100. The default value is 20.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A filter on the list based on the exact (case insensitive) job name.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>The offset of the first job to return, relative to the most recently created job. Deprecated since June 2023. Use ``page_token`` to iterate through the pages instead.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Use ``next_page_token`` or ``prev_page_token`` returned from the previous request to list the next or previous page of jobs respectively.</td>
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

Retrieves the details for a single job.

```sql
SELECT
effective_budget_policy_id,
effective_usage_policy_id,
job_id,
creator_user_name,
run_as_user_name,
created_time,
has_more,
next_page_token,
path,
settings,
trigger_state
FROM databricks_workspace.jobs.jobs
WHERE job_id = '{{ job_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND include_trigger_state = '{{ include_trigger_state }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of jobs.

```sql
SELECT
effective_budget_policy_id,
effective_usage_policy_id,
job_id,
creator_user_name,
created_time,
has_more,
path,
settings,
trigger_state
FROM databricks_workspace.jobs.jobs
WHERE deployment_name = '{{ deployment_name }}' -- required
AND expand_tasks = '{{ expand_tasks }}'
AND limit = '{{ limit }}'
AND name = '{{ name }}'
AND offset = '{{ offset }}'
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
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new job.

```sql
INSERT INTO databricks_workspace.jobs.jobs (
access_control_list,
budget_policy_id,
continuous,
deployment,
description,
edit_mode,
email_notifications,
environment_variables,
environments,
format,
git_source,
health,
job_clusters,
max_concurrent_runs,
name,
notification_settings,
parameters,
parent_path,
performance_target,
queue,
run_as,
schedule,
tags,
tasks,
timeout_seconds,
trigger,
usage_policy_id,
webhook_notifications,
deployment_name
)
SELECT 
'{{ access_control_list }}',
'{{ budget_policy_id }}',
'{{ continuous }}',
'{{ deployment }}',
'{{ description }}',
'{{ edit_mode }}',
'{{ email_notifications }}',
'{{ environment_variables }}',
'{{ environments }}',
'{{ format }}',
'{{ git_source }}',
'{{ health }}',
'{{ job_clusters }}',
{{ max_concurrent_runs }},
'{{ name }}',
'{{ notification_settings }}',
'{{ parameters }}',
'{{ parent_path }}',
'{{ performance_target }}',
'{{ queue }}',
'{{ run_as }}',
'{{ schedule }}',
'{{ tags }}',
'{{ tasks }}',
{{ timeout_seconds }},
'{{ trigger }}',
'{{ usage_policy_id }}',
'{{ webhook_notifications }}',
'{{ deployment_name }}'
RETURNING
job_id
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: jobs
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the jobs resource.
    - name: access_control_list
      description: |
        List of permissions to set on the job.
      value:
        - group_name: "{{ group_name }}"
          permission_level: "{{ permission_level }}"
          service_principal_name: "{{ service_principal_name }}"
          user_name: "{{ user_name }}"
    - name: budget_policy_id
      value: "{{ budget_policy_id }}"
      description: |
        The id of the user specified budget policy to use for this job. If not specified, a default budget policy may be applied when creating or modifying the job. See \`\`effective_budget_policy_id\`\` for the budget policy used by this workload.
    - name: continuous
      description: |
        An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of \`\`schedule\`\` and \`\`continuous\`\` can be used.
      value:
        maintenance_window:
          start_hour: {{ start_hour }}
          day_of_week: "{{ day_of_week }}"
          timezone_id: "{{ timezone_id }}"
        pause_status: "{{ pause_status }}"
        task_retry_mode: "{{ task_retry_mode }}"
    - name: deployment
      description: |
        Deployment information for jobs managed by external sources.
      value:
        kind: "{{ kind }}"
        deployment_id: "{{ deployment_id }}"
        metadata_file_path: "{{ metadata_file_path }}"
        version_id: "{{ version_id }}"
    - name: description
      value: "{{ description }}"
      description: |
        An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding.
    - name: edit_mode
      value: "{{ edit_mode }}"
      description: |
        Edit mode of the job. - \`\`UI_LOCKED\`\`: The job is in a locked UI state and cannot be modified. - \`\`EDITABLE\`\`: The job is in an editable state and can be modified.
    - name: email_notifications
      description: |
        An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.
      value:
        no_alert_for_skipped_runs: {{ no_alert_for_skipped_runs }}
        on_duration_warning_threshold_exceeded:
          - "{{ on_duration_warning_threshold_exceeded }}"
        on_failure:
          - "{{ on_failure }}"
        on_maintenance_complete:
          - "{{ on_maintenance_complete }}"
        on_maintenance_start:
          - "{{ on_maintenance_start }}"
        on_start:
          - "{{ on_start }}"
        on_streaming_backlog_exceeded:
          - "{{ on_streaming_backlog_exceeded }}"
        on_success:
          - "{{ on_success }}"
    - name: environment_variables
      description: |
        Named environment-variable entries that tasks can reference by key from \`\`TaskSettings.environment_variables_key\`\`. Each entry holds inline \`\`variables\`\` plus optional \`\`.env\`\` \`\`files\`\`. Maximum 10 entries per job. Entries are independent of one another — there is no cross-entry merging.
      value:
        - environment_variables_key: "{{ environment_variables_key }}"
          files: "{{ files }}"
          variables: "{{ variables }}"
    - name: environments
      description: |
        A list of task execution environment specifications that can be referenced by serverless tasks of this job. For serverless notebook tasks, if the environment_key is not specified, the notebook environment will be used if present. If a jobs environment is specified, it will override the notebook environment. For other serverless tasks, the task environment is required to be specified using environment_key in the task settings.
      value:
        - environment_key: "{{ environment_key }}"
          spec: "{{ spec }}"
    - name: format
      value: "{{ format }}"
      description: |
        Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to \`\`"MULTI_TASK"\`\`.
    - name: git_source
      description: |
        An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If \`\`git_source\`\` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting \`\`source\`\` to \`\`WORKSPACE\`\` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, \`\`git_source\`\` must be defined on the job.
      value:
        git_url: "{{ git_url }}"
        git_provider: "{{ git_provider }}"
        git_branch: "{{ git_branch }}"
        git_commit: "{{ git_commit }}"
        git_snapshot:
          used_commit: "{{ used_commit }}"
        git_tag: "{{ git_tag }}"
        job_source:
          job_config_path: "{{ job_config_path }}"
          import_from_git_branch: "{{ import_from_git_branch }}"
          dirty_state: "{{ dirty_state }}"
        sparse_checkout:
          patterns:
            - "{{ patterns }}"
    - name: health
      description: |
        An optional set of health rules that can be defined for this job.
      value:
        rules:
          - metric: "{{ metric }}"
            op: "{{ op }}"
            value: {{ value }}
    - name: job_clusters
      description: |
        A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
      value:
        - job_cluster_key: "{{ job_cluster_key }}"
          new_cluster: "{{ new_cluster }}"
          serverless_compute_id: "{{ serverless_compute_id }}"
    - name: max_concurrent_runs
      value: {{ max_concurrent_runs }}
      description: |
        An optional maximum allowed number of concurrent runs of the job. Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters. This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new runs are skipped unless there are fewer than 3 active runs. This value cannot exceed 1000. Setting this value to \`\`0\`\` causes all new runs to be skipped.
    - name: name
      value: "{{ name }}"
      description: |
        An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.
    - name: notification_settings
      description: |
        Optional notification settings that are used when sending notifications to each of the \`\`email_notifications\`\` and \`\`webhook_notifications\`\` for this job.
      value:
        no_alert_for_canceled_runs: {{ no_alert_for_canceled_runs }}
        no_alert_for_skipped_runs: {{ no_alert_for_skipped_runs }}
    - name: parameters
      description: |
        Job-level parameter definitions
      value:
        - name: "{{ name }}"
          default: "{{ default }}"
    - name: parent_path
      value: "{{ parent_path }}"
      description: |
        Path of the job parent folder in workspace file tree. If absent, the job doesn't have a workspace object.
    - name: performance_target
      value: "{{ performance_target }}"
      description: |
        The performance mode on a serverless job. This field determines the level of compute performance or cost-efficiency for the run. The performance target does not apply to tasks that run on Serverless GPU compute. - \`\`STANDARD\`\`: Enables cost-efficient execution of serverless workloads. - \`\`PERFORMANCE_OPTIMIZED\`\`: Prioritizes fast startup and execution times through rapid scaling and optimized cluster performance.
    - name: queue
      description: |
        The queue settings of the job.
      value:
        enabled: {{ enabled }}
    - name: run_as
      description: |
        The user or service principal that the job runs as, if specified in the request. This field indicates the explicit configuration of \`\`run_as\`\` for the job. To find the value in all cases, explicit or implicit, use \`\`run_as_user_name\`\`.
      value:
        group_name: "{{ group_name }}"
        service_principal_name: "{{ service_principal_name }}"
        user_name: "{{ user_name }}"
    - name: schedule
      description: |
        An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to \`\`runNow\`\`.
      value:
        quartz_cron_expression: "{{ quartz_cron_expression }}"
        timezone_id: "{{ timezone_id }}"
        pause_status: "{{ pause_status }}"
        sql_condition:
          sql_query_id: "{{ sql_query_id }}"
          warehouse_id: "{{ warehouse_id }}"
          trigger_mode: "{{ trigger_mode }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.
    - name: tasks
      description: |
        A list of task specifications to be executed by this job. It supports up to 1000 elements in write endpoints (:method:jobs/create, :method:jobs/reset, :method:jobs/update, :method:jobs/submit). Read endpoints return only 100 tasks. If more than 100 tasks are available, you can paginate through them using :method:jobs/get. Use the \`\`next_page_token\`\` field at the object root to determine if more results are available.
      value:
        - task_key: "{{ task_key }}"
          agentic_task:
            context:
              conversation_ids:
                - "{{ conversation_ids }}"
              instructions:
                - "{{ instructions }}"
            genie_code_api: "{{ genie_code_api }}"
            goal: "{{ goal }}"
            input: "{{ input }}"
            output_schema:
              properties: "{{ properties }}"
            supervisor_agent:
              agent_id: "{{ agent_id }}"
            supervisor_api:
              instructions: "{{ instructions }}"
              model: "{{ model }}"
              tools:
                - app:
                    name: "{{ name }}"
                  catalog:
                    name: "{{ name }}"
                  dashboard:
                    dashboard_id: "{{ dashboard_id }}"
                  description: "{{ description }}"
                  genie_space:
                    space_id: "{{ space_id }}"
                  knowledge_assistant:
                    knowledge_assistant_id: "{{ knowledge_assistant_id }}"
                  schema:
                    name: "{{ name }}"
                  serving_endpoint:
                    name: "{{ name }}"
                  supervisor_agent:
                    supervisor_agent_id: "{{ supervisor_agent_id }}"
                  table:
                    name: "{{ name }}"
                  tool_type: "{{ tool_type }}"
                  uc_connection:
                    name: "{{ name }}"
                  uc_function:
                    name: "{{ name }}"
                  uc_mcp:
                    name: "{{ name }}"
                  vector_search_index:
                    name: "{{ name }}"
                  volume:
                    name: "{{ name }}"
                  web_search: "{{ web_search }}"
            task_output_schema: "{{ task_output_schema }}"
            trace_destination:
              catalog_name: "{{ catalog_name }}"
              experiment_id: "{{ experiment_id }}"
              schema_name: "{{ schema_name }}"
              table_prefix: "{{ table_prefix }}"
          ai_runtime_task:
            experiment: "{{ experiment }}"
            deployments:
              - command_path: "{{ command_path }}"
                compute:
                  accelerator_type: "{{ accelerator_type }}"
                  accelerator_count: {{ accelerator_count }}
                docker_image_url: "{{ docker_image_url }}"
                name: "{{ name }}"
            code_source_path: "{{ code_source_path }}"
            docker_image_url: "{{ docker_image_url }}"
            mlflow_experiment_directory: "{{ mlflow_experiment_directory }}"
            mlflow_run: "{{ mlflow_run }}"
            parameters: "{{ parameters }}"
          alert_task:
            alert_id: "{{ alert_id }}"
            parameters: "{{ parameters }}"
            subscribers:
              - destination_id: "{{ destination_id }}"
                user_name: "{{ user_name }}"
            warehouse_id: "{{ warehouse_id }}"
            workspace_path: "{{ workspace_path }}"
          clean_rooms_notebook_task:
            clean_room_name: "{{ clean_room_name }}"
            notebook_name: "{{ notebook_name }}"
            etag: "{{ etag }}"
            notebook_base_parameters: "{{ notebook_base_parameters }}"
          compute:
            hardware_accelerator: "{{ hardware_accelerator }}"
          condition_task:
            op: "{{ op }}"
            left: "{{ left }}"
            right: "{{ right }}"
          dashboard_task:
            dashboard_id: "{{ dashboard_id }}"
            filters: "{{ filters }}"
            subscription:
              custom_subject: "{{ custom_subject }}"
              paused: {{ paused }}
              subscribers:
                - destination_id: "{{ destination_id }}"
                  user_name: "{{ user_name }}"
            warehouse_id: "{{ warehouse_id }}"
          dbt_cloud_task:
            connection_resource_name: "{{ connection_resource_name }}"
            dbt_cloud_job_id: {{ dbt_cloud_job_id }}
          dbt_platform_task:
            connection_resource_name: "{{ connection_resource_name }}"
            dbt_platform_job_id: "{{ dbt_platform_job_id }}"
          dbt_task:
            commands:
              - "{{ commands }}"
            catalog: "{{ catalog }}"
            profiles_directory: "{{ profiles_directory }}"
            project_directory: "{{ project_directory }}"
            schema: "{{ schema }}"
            source: "{{ source }}"
            warehouse_id: "{{ warehouse_id }}"
          depends_on: "{{ depends_on }}"
          description: "{{ description }}"
          disable_auto_optimization: {{ disable_auto_optimization }}
          disabled: {{ disabled }}
          email_notifications:
            no_alert_for_skipped_runs: {{ no_alert_for_skipped_runs }}
            on_duration_warning_threshold_exceeded:
              - "{{ on_duration_warning_threshold_exceeded }}"
            on_failure:
              - "{{ on_failure }}"
            on_maintenance_complete:
              - "{{ on_maintenance_complete }}"
            on_maintenance_start:
              - "{{ on_maintenance_start }}"
            on_start:
              - "{{ on_start }}"
            on_streaming_backlog_exceeded:
              - "{{ on_streaming_backlog_exceeded }}"
            on_success:
              - "{{ on_success }}"
          environment_key: "{{ environment_key }}"
          environment_variables_key: "{{ environment_variables_key }}"
          existing_cluster_id: "{{ existing_cluster_id }}"
          for_each_task:
            inputs: "{{ inputs }}"
            task:
              task_key: "{{ task_key }}"
              agentic_task:
                context:
                  conversation_ids: "{{ conversation_ids }}"
                  instructions: "{{ instructions }}"
                genie_code_api: "{{ genie_code_api }}"
                goal: "{{ goal }}"
                input: "{{ input }}"
                output_schema:
                  properties: "{{ properties }}"
                supervisor_agent:
                  agent_id: "{{ agent_id }}"
                supervisor_api:
                  instructions: "{{ instructions }}"
                  model: "{{ model }}"
                  tools: "{{ tools }}"
                task_output_schema: "{{ task_output_schema }}"
                trace_destination:
                  catalog_name: "{{ catalog_name }}"
                  experiment_id: "{{ experiment_id }}"
                  schema_name: "{{ schema_name }}"
                  table_prefix: "{{ table_prefix }}"
              ai_runtime_task:
                experiment: "{{ experiment }}"
                deployments:
                  - command_path: "{{ command_path }}"
                    compute:
                      accelerator_type: "{{ accelerator_type }}"
                      accelerator_count: {{ accelerator_count }}
                    docker_image_url: "{{ docker_image_url }}"
                    name: "{{ name }}"
                code_source_path: "{{ code_source_path }}"
                docker_image_url: "{{ docker_image_url }}"
                mlflow_experiment_directory: "{{ mlflow_experiment_directory }}"
                mlflow_run: "{{ mlflow_run }}"
                parameters: "{{ parameters }}"
              alert_task:
                alert_id: "{{ alert_id }}"
                parameters: "{{ parameters }}"
                subscribers:
                  - destination_id: "{{ destination_id }}"
                    user_name: "{{ user_name }}"
                warehouse_id: "{{ warehouse_id }}"
                workspace_path: "{{ workspace_path }}"
              clean_rooms_notebook_task:
                clean_room_name: "{{ clean_room_name }}"
                notebook_name: "{{ notebook_name }}"
                etag: "{{ etag }}"
                notebook_base_parameters: "{{ notebook_base_parameters }}"
              compute:
                hardware_accelerator: "{{ hardware_accelerator }}"
              condition_task:
                op: "{{ op }}"
                left: "{{ left }}"
                right: "{{ right }}"
              dashboard_task:
                dashboard_id: "{{ dashboard_id }}"
                filters: "{{ filters }}"
                subscription:
                  custom_subject: "{{ custom_subject }}"
                  paused: {{ paused }}
                  subscribers: "{{ subscribers }}"
                warehouse_id: "{{ warehouse_id }}"
              dbt_cloud_task:
                connection_resource_name: "{{ connection_resource_name }}"
                dbt_cloud_job_id: {{ dbt_cloud_job_id }}
              dbt_platform_task:
                connection_resource_name: "{{ connection_resource_name }}"
                dbt_platform_job_id: "{{ dbt_platform_job_id }}"
              dbt_task:
                commands:
                  - "{{ commands }}"
                catalog: "{{ catalog }}"
                profiles_directory: "{{ profiles_directory }}"
                project_directory: "{{ project_directory }}"
                schema: "{{ schema }}"
                source: "{{ source }}"
                warehouse_id: "{{ warehouse_id }}"
              depends_on:
                - task_key: "{{ task_key }}"
                  outcome: "{{ outcome }}"
              description: "{{ description }}"
              disable_auto_optimization: {{ disable_auto_optimization }}
              disabled: {{ disabled }}
              email_notifications:
                no_alert_for_skipped_runs: {{ no_alert_for_skipped_runs }}
                on_duration_warning_threshold_exceeded:
                  - "{{ on_duration_warning_threshold_exceeded }}"
                on_failure:
                  - "{{ on_failure }}"
                on_maintenance_complete:
                  - "{{ on_maintenance_complete }}"
                on_maintenance_start:
                  - "{{ on_maintenance_start }}"
                on_start:
                  - "{{ on_start }}"
                on_streaming_backlog_exceeded:
                  - "{{ on_streaming_backlog_exceeded }}"
                on_success:
                  - "{{ on_success }}"
              environment_key: "{{ environment_key }}"
              environment_variables_key: "{{ environment_variables_key }}"
              existing_cluster_id: "{{ existing_cluster_id }}"
              for_each_task:
                inputs: "{{ inputs }}"
                task:
                  task_key: "{{ task_key }}"
                  agentic_task: "{{ agentic_task }}"
                  ai_runtime_task: "{{ ai_runtime_task }}"
                  alert_task: "{{ alert_task }}"
                  clean_rooms_notebook_task: "{{ clean_rooms_notebook_task }}"
                  compute: "{{ compute }}"
                  condition_task: "{{ condition_task }}"
                  dashboard_task: "{{ dashboard_task }}"
                  dbt_cloud_task: "{{ dbt_cloud_task }}"
                  dbt_platform_task: "{{ dbt_platform_task }}"
                  dbt_task: "{{ dbt_task }}"
                  depends_on: "{{ depends_on }}"
                  description: "{{ description }}"
                  disable_auto_optimization: {{ disable_auto_optimization }}
                  disabled: {{ disabled }}
                  email_notifications: "{{ email_notifications }}"
                  environment_key: "{{ environment_key }}"
                  environment_variables_key: "{{ environment_variables_key }}"
                  existing_cluster_id: "{{ existing_cluster_id }}"
                  for_each_task: "{{ for_each_task }}"
                  gen_ai_compute_task: "{{ gen_ai_compute_task }}"
                  genie_task: "{{ genie_task }}"
                  health: "{{ health }}"
                  job_cluster_key: "{{ job_cluster_key }}"
                  libraries: "{{ libraries }}"
                  max_retries: {{ max_retries }}
                  min_retry_interval_millis: {{ min_retry_interval_millis }}
                  new_cluster: "{{ new_cluster }}"
                  notebook_task: "{{ notebook_task }}"
                  notification_settings: "{{ notification_settings }}"
                  pipeline_task: "{{ pipeline_task }}"
                  power_bi_task: "{{ power_bi_task }}"
                  python_operator_task: "{{ python_operator_task }}"
                  python_wheel_task: "{{ python_wheel_task }}"
                  retry_on_timeout: {{ retry_on_timeout }}
                  run_if: "{{ run_if }}"
                  run_job_task: "{{ run_job_task }}"
                  spark_jar_task: "{{ spark_jar_task }}"
                  spark_python_task: "{{ spark_python_task }}"
                  spark_submit_task: "{{ spark_submit_task }}"
                  sql_task: "{{ sql_task }}"
                  timeout_seconds: {{ timeout_seconds }}
                  webhook_notifications: "{{ webhook_notifications }}"
                concurrency: {{ concurrency }}
              gen_ai_compute_task:
                dl_runtime_image: "{{ dl_runtime_image }}"
                client_version: "{{ client_version }}"
                code_source_tar_path: "{{ code_source_tar_path }}"
                command: "{{ command }}"
                compute:
                  num_gpus: {{ num_gpus }}
                  gpu_node_pool_id: "{{ gpu_node_pool_id }}"
                  gpu_type: "{{ gpu_type }}"
                docker_image_url: "{{ docker_image_url }}"
                mlflow_experiment_name: "{{ mlflow_experiment_name }}"
                mlflow_run_name: "{{ mlflow_run_name }}"
                requirements_yaml_path: "{{ requirements_yaml_path }}"
                source: "{{ source }}"
                training_script_path: "{{ training_script_path }}"
                yaml_parameters: "{{ yaml_parameters }}"
                yaml_parameters_file_path: "{{ yaml_parameters_file_path }}"
              genie_task:
                configuration_id: "{{ configuration_id }}"
              health:
                rules:
                  - metric: "{{ metric }}"
                    op: "{{ op }}"
                    value: {{ value }}
              job_cluster_key: "{{ job_cluster_key }}"
              libraries: "{{ libraries }}"
              max_retries: {{ max_retries }}
              min_retry_interval_millis: {{ min_retry_interval_millis }}
              new_cluster: "{{ new_cluster }}"
              notebook_task:
                notebook_path: "{{ notebook_path }}"
                base_parameters: "{{ base_parameters }}"
                source: "{{ source }}"
                warehouse_id: "{{ warehouse_id }}"
              notification_settings:
                alert_on_last_attempt: {{ alert_on_last_attempt }}
                no_alert_for_canceled_runs: {{ no_alert_for_canceled_runs }}
                no_alert_for_skipped_runs: {{ no_alert_for_skipped_runs }}
              pipeline_task:
                pipeline_id: "{{ pipeline_id }}"
                full_refresh: {{ full_refresh }}
                full_refresh_selection:
                  - "{{ full_refresh_selection }}"
                parameters: "{{ parameters }}"
                refresh_flow_selection:
                  - "{{ refresh_flow_selection }}"
                refresh_selection:
                  - "{{ refresh_selection }}"
                reset_checkpoint_selection:
                  - "{{ reset_checkpoint_selection }}"
              power_bi_task:
                connection_resource_name: "{{ connection_resource_name }}"
                incremental_refresh_config:
                  archive_window_granularity: "{{ archive_window_granularity }}"
                  archive_window_periods: {{ archive_window_periods }}
                  detect_data_changes: {{ detect_data_changes }}
                  mode: "{{ mode }}"
                  only_refresh_complete_periods: {{ only_refresh_complete_periods }}
                  refresh_window_granularity: "{{ refresh_window_granularity }}"
                  refresh_window_periods: {{ refresh_window_periods }}
                power_bi_model:
                  authentication_method: "{{ authentication_method }}"
                  model_name: "{{ model_name }}"
                  overwrite_existing: {{ overwrite_existing }}
                  storage_mode: "{{ storage_mode }}"
                  workspace_name: "{{ workspace_name }}"
                refresh_after_update: {{ refresh_after_update }}
                tables:
                  - catalog: "{{ catalog }}"
                    incremental_refresh_datetime_column: "{{ incremental_refresh_datetime_column }}"
                    name: "{{ name }}"
                    schema: "{{ schema }}"
                    storage_mode: "{{ storage_mode }}"
                    table_type: "{{ table_type }}"
                warehouse_id: "{{ warehouse_id }}"
              python_operator_task:
                main: "{{ main }}"
                parameters:
                  - name: "{{ name }}"
                    value: "{{ value }}"
              python_wheel_task:
                package_name: "{{ package_name }}"
                entry_point: "{{ entry_point }}"
                named_parameters: "{{ named_parameters }}"
                parameters:
                  - "{{ parameters }}"
              retry_on_timeout: {{ retry_on_timeout }}
              run_if: "{{ run_if }}"
              run_job_task:
                job_id: {{ job_id }}
                dbt_commands:
                  - "{{ dbt_commands }}"
                jar_params:
                  - "{{ jar_params }}"
                job_parameters: "{{ job_parameters }}"
                notebook_params: "{{ notebook_params }}"
                pipeline_params:
                  full_refresh: {{ full_refresh }}
                  full_refresh_selection: "{{ full_refresh_selection }}"
                  refresh_flow_selection: "{{ refresh_flow_selection }}"
                  refresh_selection: "{{ refresh_selection }}"
                  reset_checkpoint_selection: "{{ reset_checkpoint_selection }}"
                python_named_params: "{{ python_named_params }}"
                python_params:
                  - "{{ python_params }}"
                spark_submit_params:
                  - "{{ spark_submit_params }}"
                sql_params: "{{ sql_params }}"
              spark_jar_task:
                jar_uri: "{{ jar_uri }}"
                main_class_name: "{{ main_class_name }}"
                parameters:
                  - "{{ parameters }}"
                run_as_repl: {{ run_as_repl }}
              spark_python_task:
                python_file: "{{ python_file }}"
                parameters:
                  - "{{ parameters }}"
                source: "{{ source }}"
              spark_submit_task:
                parameters:
                  - "{{ parameters }}"
              sql_task:
                warehouse_id: "{{ warehouse_id }}"
                alert:
                  alert_id: "{{ alert_id }}"
                  pause_subscriptions: {{ pause_subscriptions }}
                  subscriptions: "{{ subscriptions }}"
                dashboard:
                  dashboard_id: "{{ dashboard_id }}"
                  custom_subject: "{{ custom_subject }}"
                  pause_subscriptions: {{ pause_subscriptions }}
                  subscriptions: "{{ subscriptions }}"
                file:
                  path: "{{ path }}"
                  source: "{{ source }}"
                parameters: "{{ parameters }}"
                query:
                  query_id: "{{ query_id }}"
              timeout_seconds: {{ timeout_seconds }}
              webhook_notifications:
                on_duration_warning_threshold_exceeded:
                  - id: "{{ id }}"
                on_failure:
                  - id: "{{ id }}"
                on_maintenance_complete:
                  - id: "{{ id }}"
                on_maintenance_start:
                  - id: "{{ id }}"
                on_start:
                  - id: "{{ id }}"
                on_streaming_backlog_exceeded:
                  - id: "{{ id }}"
                on_success:
                  - id: "{{ id }}"
            concurrency: {{ concurrency }}
          gen_ai_compute_task:
            dl_runtime_image: "{{ dl_runtime_image }}"
            client_version: "{{ client_version }}"
            code_source_tar_path: "{{ code_source_tar_path }}"
            command: "{{ command }}"
            compute:
              num_gpus: {{ num_gpus }}
              gpu_node_pool_id: "{{ gpu_node_pool_id }}"
              gpu_type: "{{ gpu_type }}"
            docker_image_url: "{{ docker_image_url }}"
            mlflow_experiment_name: "{{ mlflow_experiment_name }}"
            mlflow_run_name: "{{ mlflow_run_name }}"
            requirements_yaml_path: "{{ requirements_yaml_path }}"
            source: "{{ source }}"
            training_script_path: "{{ training_script_path }}"
            yaml_parameters: "{{ yaml_parameters }}"
            yaml_parameters_file_path: "{{ yaml_parameters_file_path }}"
          genie_task:
            configuration_id: "{{ configuration_id }}"
          health:
            rules:
              - metric: "{{ metric }}"
                op: "{{ op }}"
                value: {{ value }}
          job_cluster_key: "{{ job_cluster_key }}"
          libraries: "{{ libraries }}"
          max_retries: {{ max_retries }}
          min_retry_interval_millis: {{ min_retry_interval_millis }}
          new_cluster: "{{ new_cluster }}"
          notebook_task:
            notebook_path: "{{ notebook_path }}"
            base_parameters: "{{ base_parameters }}"
            source: "{{ source }}"
            warehouse_id: "{{ warehouse_id }}"
          notification_settings:
            alert_on_last_attempt: {{ alert_on_last_attempt }}
            no_alert_for_canceled_runs: {{ no_alert_for_canceled_runs }}
            no_alert_for_skipped_runs: {{ no_alert_for_skipped_runs }}
          pipeline_task:
            pipeline_id: "{{ pipeline_id }}"
            full_refresh: {{ full_refresh }}
            full_refresh_selection:
              - "{{ full_refresh_selection }}"
            parameters: "{{ parameters }}"
            refresh_flow_selection:
              - "{{ refresh_flow_selection }}"
            refresh_selection:
              - "{{ refresh_selection }}"
            reset_checkpoint_selection:
              - "{{ reset_checkpoint_selection }}"
          power_bi_task:
            connection_resource_name: "{{ connection_resource_name }}"
            incremental_refresh_config:
              archive_window_granularity: "{{ archive_window_granularity }}"
              archive_window_periods: {{ archive_window_periods }}
              detect_data_changes: {{ detect_data_changes }}
              mode: "{{ mode }}"
              only_refresh_complete_periods: {{ only_refresh_complete_periods }}
              refresh_window_granularity: "{{ refresh_window_granularity }}"
              refresh_window_periods: {{ refresh_window_periods }}
            power_bi_model:
              authentication_method: "{{ authentication_method }}"
              model_name: "{{ model_name }}"
              overwrite_existing: {{ overwrite_existing }}
              storage_mode: "{{ storage_mode }}"
              workspace_name: "{{ workspace_name }}"
            refresh_after_update: {{ refresh_after_update }}
            tables:
              - catalog: "{{ catalog }}"
                incremental_refresh_datetime_column: "{{ incremental_refresh_datetime_column }}"
                name: "{{ name }}"
                schema: "{{ schema }}"
                storage_mode: "{{ storage_mode }}"
                table_type: "{{ table_type }}"
            warehouse_id: "{{ warehouse_id }}"
          python_operator_task:
            main: "{{ main }}"
            parameters:
              - name: "{{ name }}"
                value: "{{ value }}"
          python_wheel_task:
            package_name: "{{ package_name }}"
            entry_point: "{{ entry_point }}"
            named_parameters: "{{ named_parameters }}"
            parameters:
              - "{{ parameters }}"
          retry_on_timeout: {{ retry_on_timeout }}
          run_if: "{{ run_if }}"
          run_job_task:
            job_id: {{ job_id }}
            dbt_commands:
              - "{{ dbt_commands }}"
            jar_params:
              - "{{ jar_params }}"
            job_parameters: "{{ job_parameters }}"
            notebook_params: "{{ notebook_params }}"
            pipeline_params:
              full_refresh: {{ full_refresh }}
              full_refresh_selection:
                - "{{ full_refresh_selection }}"
              refresh_flow_selection:
                - "{{ refresh_flow_selection }}"
              refresh_selection:
                - "{{ refresh_selection }}"
              reset_checkpoint_selection:
                - "{{ reset_checkpoint_selection }}"
            python_named_params: "{{ python_named_params }}"
            python_params:
              - "{{ python_params }}"
            spark_submit_params:
              - "{{ spark_submit_params }}"
            sql_params: "{{ sql_params }}"
          spark_jar_task:
            jar_uri: "{{ jar_uri }}"
            main_class_name: "{{ main_class_name }}"
            parameters:
              - "{{ parameters }}"
            run_as_repl: {{ run_as_repl }}
          spark_python_task:
            python_file: "{{ python_file }}"
            parameters:
              - "{{ parameters }}"
            source: "{{ source }}"
          spark_submit_task:
            parameters:
              - "{{ parameters }}"
          sql_task:
            warehouse_id: "{{ warehouse_id }}"
            alert:
              alert_id: "{{ alert_id }}"
              pause_subscriptions: {{ pause_subscriptions }}
              subscriptions:
                - destination_id: "{{ destination_id }}"
                  user_name: "{{ user_name }}"
            dashboard:
              dashboard_id: "{{ dashboard_id }}"
              custom_subject: "{{ custom_subject }}"
              pause_subscriptions: {{ pause_subscriptions }}
              subscriptions:
                - destination_id: "{{ destination_id }}"
                  user_name: "{{ user_name }}"
            file:
              path: "{{ path }}"
              source: "{{ source }}"
            parameters: "{{ parameters }}"
            query:
              query_id: "{{ query_id }}"
          timeout_seconds: {{ timeout_seconds }}
          webhook_notifications:
            on_duration_warning_threshold_exceeded:
              - id: "{{ id }}"
            on_failure:
              - id: "{{ id }}"
            on_maintenance_complete:
              - id: "{{ id }}"
            on_maintenance_start:
              - id: "{{ id }}"
            on_start:
              - id: "{{ id }}"
            on_streaming_backlog_exceeded:
              - id: "{{ id }}"
            on_success:
              - id: "{{ id }}"
    - name: timeout_seconds
      value: {{ timeout_seconds }}
      description: |
        An optional timeout applied to each run of this job. A value of \`\`0\`\` means no timeout.
    - name: trigger
      description: |
        A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to \`\`runNow\`\`.
      value:
        file_arrival:
          url: "{{ url }}"
          min_time_between_triggers_seconds: {{ min_time_between_triggers_seconds }}
          wait_after_last_change_seconds: {{ wait_after_last_change_seconds }}
        model:
          condition: "{{ condition }}"
          aliases:
            - "{{ aliases }}"
          min_time_between_triggers_seconds: {{ min_time_between_triggers_seconds }}
          securable_name: "{{ securable_name }}"
          wait_after_last_change_seconds: {{ wait_after_last_change_seconds }}
        pause_status: "{{ pause_status }}"
        periodic:
          interval: {{ interval }}
          unit: "{{ unit }}"
        sql_condition:
          sql_query_id: "{{ sql_query_id }}"
          warehouse_id: "{{ warehouse_id }}"
          trigger_mode: "{{ trigger_mode }}"
        table_update:
          table_names:
            - "{{ table_names }}"
          condition: "{{ condition }}"
          min_time_between_triggers_seconds: {{ min_time_between_triggers_seconds }}
          wait_after_last_change_seconds: {{ wait_after_last_change_seconds }}
    - name: usage_policy_id
      value: "{{ usage_policy_id }}"
      description: |
        The id of the user specified usage policy to use for this job. If not specified, a default usage policy may be applied when creating or modifying the job. See \`\`effective_usage_policy_id\`\` for the usage policy used by this workload.
    - name: webhook_notifications
      description: |
        A collection of system notification IDs to notify when runs of this job begin or complete.
      value:
        on_duration_warning_threshold_exceeded:
          - id: "{{ id }}"
        on_failure:
          - id: "{{ id }}"
        on_maintenance_complete:
          - id: "{{ id }}"
        on_maintenance_start:
          - id: "{{ id }}"
        on_start:
          - id: "{{ id }}"
        on_streaming_backlog_exceeded:
          - id: "{{ id }}"
        on_success:
          - id: "{{ id }}"
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

Add, update, or remove specific settings of an existing job. Use the [*Reset*

```sql
UPDATE databricks_workspace.jobs.jobs
SET 
job_id = {{ job_id }},
fields_to_remove = '{{ fields_to_remove }}',
new_settings = '{{ new_settings }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND job_id = '{{ job_id }}' --required;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="reset"
    values={[
        { label: 'reset', value: 'reset' }
    ]}
>
<TabItem value="reset">

Overwrite all settings for the given job. Use the [*Update* endpoint](:method:jobs/update) to update

```sql
REPLACE databricks_workspace.jobs.jobs
SET 
job_id = {{ job_id }},
new_settings = '{{ new_settings }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND job_id = '{{ job_id }}' --required
AND new_settings = '{{ new_settings }}' --required;
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

Deletes a job.

```sql
DELETE FROM databricks_workspace.jobs.jobs
WHERE deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="run_now"
    values={[
        { label: 'run_now', value: 'run_now' }
    ]}
>
<TabItem value="run_now">

Run a job and return the ``run_id`` of the triggered run.

```sql
EXEC databricks_workspace.jobs.jobs.run_now 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"job_id": {{ job_id }}, 
"dbt_commands": "{{ dbt_commands }}", 
"idempotency_token": "{{ idempotency_token }}", 
"jar_params": "{{ jar_params }}", 
"job_parameters": "{{ job_parameters }}", 
"notebook_params": "{{ notebook_params }}", 
"only": "{{ only }}", 
"performance_target": "{{ performance_target }}", 
"pipeline_params": "{{ pipeline_params }}", 
"python_named_params": "{{ python_named_params }}", 
"python_params": "{{ python_params }}", 
"queue": "{{ queue }}", 
"spark_submit_params": "{{ spark_submit_params }}", 
"sql_params": "{{ sql_params }}"
}'
;
```
</TabItem>
</Tabs>
