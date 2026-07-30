---
title: policy_compliance_for_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_compliance_for_clusters
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

Creates, updates, deletes, gets or lists a <code>policy_compliance_for_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_compliance_for_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.policy_compliance_for_clusters" /></td></tr>
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
    "name": "is_compliant",
    "type": "boolean",
    "description": ""
  },
  {
    "name": "pending_enforcement",
    "type": "object",
    "description": "Information about the pending enforcement for the cluster. Only present if a pending enforcement is scheduled for the cluster.",
    "children": [
      {
        "name": "enforcement_status",
        "type": "string",
        "description": "Whether the pending enforcement will be applied. A pending enforcement begins in ``ACTIVE`` state. If the enforcement fails to apply too many times, the state transitions to ``INACTIVE``. Afterwards, the enforcement must be re-scheduled to become ``ACTIVE`` again. (ACTIVE, INACTIVE)"
      },
      {
        "name": "initiate_time",
        "type": "string (date-time)",
        "description": "The time the pending enforcement was initiated."
      },
      {
        "name": "initiator_user",
        "type": "string",
        "description": "The user who initiated the pending enforcement."
      },
      {
        "name": "target_changes",
        "type": "array",
        "description": "A list of changes that will be made to the cluster configuration when the pending enforcement is applied.",
        "children": [
          {
            "name": "field",
            "type": "string",
            "description": "The field where this change would be made."
          },
          {
            "name": "new_value",
            "type": "string",
            "description": "The new value of this field after enforcing policy compliance (either a number, a boolean, or a string) converted to a string. This is intended to be read by a human. The typed new value of this field can be retrieved by reading the settings field in the API response."
          },
          {
            "name": "previous_value",
            "type": "string",
            "description": "The previous value of this field before enforcing policy compliance (either a number, a boolean, or a string) converted to a string. This is intended to be read by a human. The type of the field can be retrieved by reading the settings field in the API response."
          }
        ]
      },
      {
        "name": "target_spec",
        "type": "object",
        "description": "The new configuration to apply upon cluster termination or restart.",
        "children": [
          {
            "name": "autoscale",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "max_workers",
                "type": "integer",
                "description": ""
              },
              {
                "name": "min_workers",
                "type": "integer",
                "description": "The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster will have after creation."
              }
            ]
          },
          {
            "name": "autotermination_minutes",
            "type": "integer",
            "description": "Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster will not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination."
          },
          {
            "name": "aws_attributes",
            "type": "object",
            "description": "Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used.",
            "children": [
              {
                "name": "availability",
                "type": "string",
                "description": "Availability type used for all subsequent nodes past the ``first_on_demand`` ones.<br /><br />Note: If ``first_on_demand`` is zero, this availability type will be used for the entire<br />cluster. (ON_DEMAND, SPOT, SPOT_WITH_FALLBACK)"
              },
              {
                "name": "ebs_volume_count",
                "type": "integer",
                "description": "The number of volumes launched for each instance. Users can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation will fail. These EBS volumes will be mounted at ``/ebs0``, ``/ebs1``, and etc. Instance store volumes will be mounted at ``/local_disk0``, ``/local_disk1``, and etc. If EBS volumes are attached, Databricks will configure Spark to use only the EBS volumes for scratch storage because heterogenously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks will configure Spark to use instance store volumes. Please note that if EBS volumes are specified, then the Spark configuration ``spark.local.dir`` will be overridden."
              },
              {
                "name": "ebs_volume_iops",
                "type": "integer",
                "description": "If using gp3 volumes, what IOPS to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
              },
              {
                "name": "ebs_volume_size",
                "type": "integer",
                "description": "The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096. For throughput optimized HDD, this value must be within the range 500 - 4096."
              },
              {
                "name": "ebs_volume_throughput",
                "type": "integer",
                "description": "If using gp3 volumes, what throughput to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
              },
              {
                "name": "ebs_volume_type",
                "type": "string",
                "description": "The type of EBS volumes that will be launched with this cluster. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
              },
              {
                "name": "first_on_demand",
                "type": "integer",
                "description": "The first ``first_on_demand`` nodes of the cluster will be placed on on-demand instances. If this value is greater than 0, the cluster driver node in particular will be placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, ``first_on_demand`` nodes will be placed on on-demand instances and the remainder will be placed on ``availability`` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
              },
              {
                "name": "instance_profile_arn",
                "type": "string",
                "description": "Nodes for this cluster will only be placed on AWS instances with this instance profile. If ommitted, nodes will be placed on instances without an IAM instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
              },
              {
                "name": "spot_bid_price_percent",
                "type": "integer",
                "description": "The bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new ``r3.xlarge`` spot instance, then the bid price is half of the price of on-demand ``r3.xlarge`` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand ``r3.xlarge`` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
              },
              {
                "name": "zone_id",
                "type": "string",
                "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, the zone \"auto\" will be used. If the zone specified is \"auto\", will try to place cluster in a zone with high availability, and will retry placement in a different AZ if there is not enough capacity. The list of available zones as well as the default value can be found by using the ``List Zones`` method."
              }
            ]
          },
          {
            "name": "azure_attributes",
            "type": "object",
            "description": "Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used.",
            "children": [
              {
                "name": "availability",
                "type": "string",
                "description": "Availability type used for all subsequent nodes past the ``first_on_demand`` ones. Note: If ``first_on_demand`` is zero, this availability type will be used for the entire cluster. (ON_DEMAND_AZURE, SPOT_AZURE, SPOT_WITH_FALLBACK_AZURE)"
              },
              {
                "name": "capacity_reservation_group",
                "type": "string",
                "description": "The Azure capacity reservation group resource ID to use for launching VMs. When specified, VMs will be launched using the provided capacity reservation. Capacity reservations can only be specified when the workspace uses injected vnet (i.e. customer defined vnet not managed by databricks). Ensure the databricks-login-prod Enterprise Application is granted the following four permissions: 1. Microsoft.Compute/capacityReservationGroups/read 2. Microsoft.Compute/capacityReservationGroups/deploy/action 3. Microsoft.Compute/capacityReservationGroups/capacityReservations/read 4. Microsoft.Compute/capacityReservationGroups/capacityReservations/deploy/action Format: ``/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/capacityReservationGroups/&#123;capacityReservationGroupName&#125;``"
              },
              {
                "name": "first_on_demand",
                "type": "integer",
                "description": "The first ``first_on_demand`` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, ``first_on_demand`` nodes will be placed on on-demand instances and the remainder will be placed on ``availability`` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
              },
              {
                "name": "log_analytics_info",
                "type": "object",
                "description": "Defines values necessary to configure and run Azure Log Analytics agent"
              },
              {
                "name": "spot_bid_max_price",
                "type": "number",
                "description": "The max bid price to be used for Azure spot instances. The Max price for the bid cannot be higher than the on-demand price of the instance. If not specified, the default value is -1, which specifies that the instance cannot be evicted on the basis of price, and only on the basis of availability. Further, the value should &gt; 0 or -1."
              }
            ]
          },
          {
            "name": "cluster_log_conf",
            "type": "object",
            "description": "The configuration for delivering spark logs to a long-term storage destination. Three kinds of destinations (DBFS, S3 and Unity Catalog volumes) are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every ``5 mins``. The destination of driver logs is ``$destination/$clusterId/driver``, while the destination of executor logs is ``$destination/$clusterId/executor``.",
            "children": [
              {
                "name": "dbfs",
                "type": "object",
                "description": "destination needs to be provided. e.g. ``&#123; \"dbfs\" : &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;``"
              },
              {
                "name": "s3",
                "type": "object",
                "description": "destination and either the region or endpoint need to be provided. e.g. ``&#123; \"s3\": &#123; \"destination\" : \"s3://cluster_log_bucket/prefix\", \"region\" : \"us-west-2\" &#125; &#125;`` Cluster iam role is used to access s3, please make sure the cluster iam role in ``instance_profile_arn`` has permission to write data to the s3 destination."
              },
              {
                "name": "volumes",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"volumes\": &#123; \"destination\": \"/Volumes/catalog/schema/volume/cluster_log\" &#125; &#125;``"
              }
            ]
          },
          {
            "name": "cluster_name",
            "type": "string",
            "description": "Cluster name requested by the user. This doesn't have to be unique. If not specified at creation, the cluster name will be an empty string. For job clusters, the cluster name is automatically set based on the job and job run IDs."
          },
          {
            "name": "custom_tags",
            "type": "object",
            "description": "Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to ``default_tags``. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags"
          },
          {
            "name": "data_security_mode",
            "type": "string",
            "description": "Data security mode decides what data governance model to use when accessing data from a cluster.<br /><br />- ``DATA_SECURITY_MODE_AUTO``: Databricks will choose the most appropriate access mode depending<br />  on your compute configuration.<br />- ``DATA_SECURITY_MODE_STANDARD``: A secure cluster that can be shared by multiple users.<br />  Cluster users are fully isolated so that they cannot see each other’s data and credentials.<br />  Most data governance features are supported in this mode. But programming languages and<br />  cluster features might be limited.<br />- ``DATA_SECURITY_MODE_DEDICATED``: A secure cluster that can only be exclusively used by a<br />  single user specified in ``single_user_name``. Most programming languages, cluster features<br />  and data governance features are available in this mode.<br /><br />The following modes are legacy aliases for the above modes:<br /><br />- ``USER_ISOLATION``: Legacy alias for ``DATA_SECURITY_MODE_STANDARD``.<br />- ``SINGLE_USER``: Legacy alias for ``DATA_SECURITY_MODE_DEDICATED``.<br /><br />The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for<br />future Databricks Runtime versions:<br /><br />- ``LEGACY_TABLE_ACL``: This mode is for users migrating from legacy Table ACL clusters.<br />- ``LEGACY_PASSTHROUGH``: This mode is for users migrating from legacy Passthrough on high<br />  concurrency clusters.<br />- ``LEGACY_SINGLE_USER``: This mode is for users migrating from legacy Passthrough on standard<br />  clusters.<br />- ``LEGACY_SINGLE_USER_STANDARD``: This mode provides a way that doesn’t have UC nor<br />  passthrough enabled. (DATA_SECURITY_MODE_AUTO, DATA_SECURITY_MODE_DEDICATED, DATA_SECURITY_MODE_STANDARD, LEGACY_PASSTHROUGH, LEGACY_SINGLE_USER, LEGACY_SINGLE_USER_STANDARD, LEGACY_TABLE_ACL, NONE, SINGLE_USER, USER_ISOLATION)"
          },
          {
            "name": "dependency_mode",
            "type": "string",
            "description": "Controls dependency configuration for the cluster. (DEPENDENCY_MODE_AUTO, DEPENDENCY_MODE_CLUSTER_LIBRARIES, DEPENDENCY_MODE_ENVIRONMENTS)"
          },
          {
            "name": "docker_image",
            "type": "object",
            "description": "Custom docker image BYOC",
            "children": [
              {
                "name": "basic_auth",
                "type": "object",
                "description": ""
              },
              {
                "name": "url",
                "type": "string",
                "description": "URL of the docker image."
              }
            ]
          },
          {
            "name": "driver_instance_pool_id",
            "type": "string",
            "description": "The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned."
          },
          {
            "name": "driver_node_type_flexibility",
            "type": "object",
            "description": "Flexible node type configuration for the driver node.",
            "children": [
              {
                "name": "alternate_node_type_ids",
                "type": "array",
                "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
              }
            ]
          },
          {
            "name": "driver_node_type_id",
            "type": "string",
            "description": "The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as ``node_type_id`` defined above. This field, along with node_type_id, should not be set if virtual_cluster_size is set. If both driver_node_type_id, node_type_id, and virtual_cluster_size are specified, driver_node_type_id and node_type_id take precedence."
          },
          {
            "name": "enable_elastic_disk",
            "type": "boolean",
            "description": "Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space when its Spark workers are running low on disk space."
          },
          {
            "name": "enable_local_disk_encryption",
            "type": "boolean",
            "description": "Whether to enable LUKS on cluster VMs' local disks"
          },
          {
            "name": "gcp_attributes",
            "type": "object",
            "description": "Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used.",
            "children": [
              {
                "name": "availability",
                "type": "string",
                "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
              },
              {
                "name": "boot_disk_size",
                "type": "integer",
                "description": "Boot disk size in GB"
              },
              {
                "name": "confidential_compute_type",
                "type": "string",
                "description": "The confidential computing technology for this cluster's instances. Currently only SEV_SNP is supported, and only on N2D instance types. When not set, no confidential computing is applied. (CONFIDENTIAL_COMPUTE_TYPE_NONE, SEV_SNP)"
              },
              {
                "name": "first_on_demand",
                "type": "integer",
                "description": "The first ``first_on_demand`` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, ``first_on_demand`` nodes will be placed on on-demand instances and the remainder will be placed on ``availability`` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
              },
              {
                "name": "google_service_account",
                "type": "string",
                "description": "If provided, the cluster will impersonate the google service account when accessing gcloud services (like GCS). The google service account must have previously been added to the Databricks environment by an account administrator."
              },
              {
                "name": "local_ssd_count",
                "type": "integer",
                "description": "If provided, each node (workers and driver) in the cluster will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to `GCP documentation <https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds>`__ for the supported number of local SSDs for each instance type."
              },
              {
                "name": "use_preemptible_executors",
                "type": "boolean",
                "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs (when set to true) versus standard compute engine VMs (when set to false; default). Note: Soon to be deprecated, use the 'availability' field instead."
              },
              {
                "name": "zone_id",
                "type": "string",
                "description": "Identifier for the availability zone in which the cluster resides. This can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region [default]. - \"AUTO\" =&gt; Databricks picks an availability zone to schedule the cluster on. - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones."
              }
            ]
          },
          {
            "name": "init_scripts",
            "type": "array",
            "description": "The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If ``cluster_log_conf`` is specified, init script logs are sent to ``&lt;destination&gt;/&lt;cluster-ID&gt;/init_scripts``.",
            "children": [
              {
                "name": "abfss",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``abfss://&lt;container-name&gt;@&lt;storage-account-name&gt;.dfs.core.windows.net/&lt;directory-name&gt;``"
              },
              {
                "name": "dbfs",
                "type": "object",
                "description": "destination needs to be provided. e.g. ``&#123; \"dbfs\": &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;``"
              },
              {
                "name": "file",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"file\": &#123; \"destination\": \"file:/my/local/file.sh\" &#125; &#125;``"
              },
              {
                "name": "gcs",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"gcs\": &#123; \"destination\": \"gs://my-bucket/file.sh\" &#125; &#125;``"
              },
              {
                "name": "s3",
                "type": "object",
                "description": "destination and either the region or endpoint need to be provided. e.g. ``&#123; \\\"s3\\\": &#123; \\\"destination\\\": \\\"s3://cluster_log_bucket/prefix\\\", \\\"region\\\": \\\"us-west-2\\\" &#125; &#125;`` Cluster iam role is used to access s3, please make sure the cluster iam role in ``instance_profile_arn`` has permission to write data to the s3 destination."
              },
              {
                "name": "volumes",
                "type": "object",
                "description": "destination needs to be provided. e.g. ``&#123; \\\"volumes\\\" : &#123; \\\"destination\\\" : \\\"/Volumes/my-init.sh\\\" &#125; &#125;``"
              },
              {
                "name": "workspace",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"workspace\": &#123; \"destination\": \"/cluster-init-scripts/setup-datadog.sh\" &#125; &#125;``"
              }
            ]
          },
          {
            "name": "instance_pool_id",
            "type": "string",
            "description": "The optional ID of the instance pool to which the cluster belongs."
          },
          {
            "name": "is_single_node",
            "type": "boolean",
            "description": "This field can only be used when ``kind = CLASSIC_PREVIEW``. When set to true, Databricks will automatically set single node related ``custom_tags``, ``spark_conf``, and ``num_workers``"
          },
          {
            "name": "kind",
            "type": "string",
            "description": "The kind of compute described by this compute specification.<br /><br />Depending on ``kind``, different validations and default values will be applied.<br /><br />Clusters with ``kind = CLASSIC_PREVIEW`` support the following fields, whereas clusters with no<br />specified ``kind`` do not.<br /><br />- [is_single_node](/api/workspace/clusters/create#is_single_node)<br />- [use_ml_runtime](/api/workspace/clusters/create#use_ml_runtime)<br /><br />By using the `simple form <https://docs.databricks.com/compute/simple-form.html>`__, your<br />clusters are automatically using ``kind = CLASSIC_PREVIEW``. (CLASSIC_PREVIEW)"
          },
          {
            "name": "node_type_id",
            "type": "string",
            "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the `clusters/listNodeTypes <https://docs.databricks.com/api/workspace/clusters/listnodetypes>`__ API call."
          },
          {
            "name": "num_workers",
            "type": "integer",
            "description": "Number of worker nodes that this cluster should have. A cluster has one Spark Driver and ``num_workers`` Executors for a total of ``num_workers`` + 1 Spark nodes. Note: When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field will immediately be updated to reflect the target size of 10 workers, whereas the workers listed in ``spark_info`` will gradually increase from 5 to 10 as the new nodes are provisioned."
          },
          {
            "name": "policy_id",
            "type": "string",
            "description": "The ID of the cluster policy used to create the cluster if applicable."
          },
          {
            "name": "remote_disk_throughput",
            "type": "integer",
            "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED disks."
          },
          {
            "name": "runtime_engine",
            "type": "string",
            "description": "Determines the cluster's runtime engine, either standard or Photon. This field is not compatible with legacy ``spark_version`` values that contain ``-photon-``. Remove ``-photon-`` from the ``spark_version`` and set ``runtime_engine`` to ``PHOTON``. If left unspecified, the runtime engine defaults to standard unless the spark_version contains -photon-, in which case Photon will be used. (NULL, PHOTON, STANDARD)"
          },
          {
            "name": "single_user_name",
            "type": "string",
            "description": "Single user name if data_security_mode is ``SINGLE_USER``"
          },
          {
            "name": "spark_conf",
            "type": "object",
            "description": "An object containing a set of optional, user-specified Spark configuration key-value pairs. Users can also pass in a string of extra JVM options to the driver and the executors via ``spark.driver.extraJavaOptions`` and ``spark.executor.extraJavaOptions`` respectively."
          },
          {
            "name": "spark_env_vars",
            "type": "object",
            "description": "An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., ``export X='Y'``) while launching the driver and workers. In order to specify an additional set of ``SPARK_DAEMON_JAVA_OPTS``, we recommend appending them to ``$SPARK_DAEMON_JAVA_OPTS`` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: ``&#123;\"SPARK_WORKER_MEMORY\": \"28000m\", \"SPARK_LOCAL_DIRS\": \"/local_disk0\"&#125;`` or ``&#123;\"SPARK_DAEMON_JAVA_OPTS\": \"$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true\"&#125;``"
          },
          {
            "name": "spark_version",
            "type": "string",
            "description": "The Spark version of the cluster, e.g. ``3.3.x-scala2.11``. A list of available Spark versions can be retrieved by using the `clusters/sparkVersions <https://docs.databricks.com/api/workspace/clusters/sparkversions>`__ API call."
          },
          {
            "name": "ssh_public_keys",
            "type": "array",
            "description": "SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name ``ubuntu`` on port ``2200``. Up to 10 keys can be specified."
          },
          {
            "name": "total_initial_remote_disk_size",
            "type": "integer",
            "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED disks."
          },
          {
            "name": "use_ml_runtime",
            "type": "boolean",
            "description": "This field can only be used when ``kind = CLASSIC_PREVIEW``. ``effective_spark_version`` is determined by ``spark_version`` (DBR release), this field ``use_ml_runtime``, and whether ``node_type_id`` is gpu node or not."
          },
          {
            "name": "worker_node_type_flexibility",
            "type": "object",
            "description": "Flexible node type configuration for worker nodes.",
            "children": [
              {
                "name": "alternate_node_type_ids",
                "type": "array",
                "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
              }
            ]
          },
          {
            "name": "workload_type",
            "type": "object",
            "description": "Cluster Attributes showing for clusters workload types.",
            "children": [
              {
                "name": "clients",
                "type": "object",
                "description": "defined what type of clients can use the cluster. E.g. Notebooks, Jobs"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "violations",
    "type": "object",
    "description": "An object containing key-value mappings representing the first 200 policy validation errors. The keys indicate the path where the policy validation error is occurring. The values indicate an error message describing the policy validation error."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "cluster_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "is_compliant",
    "type": "boolean",
    "description": "Whether this cluster is in compliance with the latest version of its policy."
  },
  {
    "name": "pending_enforcement",
    "type": "object",
    "description": "Information about the pending enforcement for the cluster. Only present if a pending enforcement is scheduled for the cluster.",
    "children": [
      {
        "name": "enforcement_status",
        "type": "string",
        "description": "Whether the pending enforcement will be applied. A pending enforcement begins in ``ACTIVE`` state. If the enforcement fails to apply too many times, the state transitions to ``INACTIVE``. Afterwards, the enforcement must be re-scheduled to become ``ACTIVE`` again. (ACTIVE, INACTIVE)"
      },
      {
        "name": "initiate_time",
        "type": "string (date-time)",
        "description": "The time the pending enforcement was initiated."
      },
      {
        "name": "initiator_user",
        "type": "string",
        "description": "The user who initiated the pending enforcement."
      },
      {
        "name": "target_changes",
        "type": "array",
        "description": "A list of changes that will be made to the cluster configuration when the pending enforcement is applied.",
        "children": [
          {
            "name": "field",
            "type": "string",
            "description": "The field where this change would be made."
          },
          {
            "name": "new_value",
            "type": "string",
            "description": "The new value of this field after enforcing policy compliance (either a number, a boolean, or a string) converted to a string. This is intended to be read by a human. The typed new value of this field can be retrieved by reading the settings field in the API response."
          },
          {
            "name": "previous_value",
            "type": "string",
            "description": "The previous value of this field before enforcing policy compliance (either a number, a boolean, or a string) converted to a string. This is intended to be read by a human. The type of the field can be retrieved by reading the settings field in the API response."
          }
        ]
      },
      {
        "name": "target_spec",
        "type": "object",
        "description": "The new configuration to apply upon cluster termination or restart.",
        "children": [
          {
            "name": "autoscale",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "max_workers",
                "type": "integer",
                "description": ""
              },
              {
                "name": "min_workers",
                "type": "integer",
                "description": "The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster will have after creation."
              }
            ]
          },
          {
            "name": "autotermination_minutes",
            "type": "integer",
            "description": "Automatically terminates the cluster after it is inactive for this time in minutes. If not set, this cluster will not be automatically terminated. If specified, the threshold must be between 10 and 10000 minutes. Users can also set this value to 0 to explicitly disable automatic termination."
          },
          {
            "name": "aws_attributes",
            "type": "object",
            "description": "Attributes related to clusters running on Amazon Web Services. If not specified at cluster creation, a set of default values will be used.",
            "children": [
              {
                "name": "availability",
                "type": "string",
                "description": "Availability type used for all subsequent nodes past the ``first_on_demand`` ones.<br /><br />Note: If ``first_on_demand`` is zero, this availability type will be used for the entire<br />cluster. (ON_DEMAND, SPOT, SPOT_WITH_FALLBACK)"
              },
              {
                "name": "ebs_volume_count",
                "type": "integer",
                "description": "The number of volumes launched for each instance. Users can choose up to 10 volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise, cluster creation will fail. These EBS volumes will be mounted at ``/ebs0``, ``/ebs1``, and etc. Instance store volumes will be mounted at ``/local_disk0``, ``/local_disk1``, and etc. If EBS volumes are attached, Databricks will configure Spark to use only the EBS volumes for scratch storage because heterogenously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached, Databricks will configure Spark to use instance store volumes. Please note that if EBS volumes are specified, then the Spark configuration ``spark.local.dir`` will be overridden."
              },
              {
                "name": "ebs_volume_iops",
                "type": "integer",
                "description": "If using gp3 volumes, what IOPS to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
              },
              {
                "name": "ebs_volume_size",
                "type": "integer",
                "description": "The size of each EBS volume (in GiB) launched for each instance. For general purpose SSD, this value must be within the range 100 - 4096. For throughput optimized HDD, this value must be within the range 500 - 4096."
              },
              {
                "name": "ebs_volume_throughput",
                "type": "integer",
                "description": "If using gp3 volumes, what throughput to use for the disk. If this is not set, the maximum performance of a gp2 volume with the same volume size will be used."
              },
              {
                "name": "ebs_volume_type",
                "type": "string",
                "description": "The type of EBS volumes that will be launched with this cluster. (GENERAL_PURPOSE_SSD, THROUGHPUT_OPTIMIZED_HDD)"
              },
              {
                "name": "first_on_demand",
                "type": "integer",
                "description": "The first ``first_on_demand`` nodes of the cluster will be placed on on-demand instances. If this value is greater than 0, the cluster driver node in particular will be placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, ``first_on_demand`` nodes will be placed on on-demand instances and the remainder will be placed on ``availability`` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
              },
              {
                "name": "instance_profile_arn",
                "type": "string",
                "description": "Nodes for this cluster will only be placed on AWS instances with this instance profile. If ommitted, nodes will be placed on instances without an IAM instance profile. The instance profile must have previously been added to the Databricks environment by an account administrator. This feature may only be available to certain customer plans."
              },
              {
                "name": "spot_bid_price_percent",
                "type": "integer",
                "description": "The bid price for AWS spot instances, as a percentage of the corresponding instance type's on-demand price. For example, if this field is set to 50, and the cluster needs a new ``r3.xlarge`` spot instance, then the bid price is half of the price of on-demand ``r3.xlarge`` instances. Similarly, if this field is set to 200, the bid price is twice the price of on-demand ``r3.xlarge`` instances. If not specified, the default value is 100. When spot instances are requested for this cluster, only spot instances whose bid price percentage matches this field will be considered. Note that, for safety, we enforce this field to be no more than 10000."
              },
              {
                "name": "zone_id",
                "type": "string",
                "description": "Identifier for the availability zone/datacenter in which the cluster resides. This string will be of a form like \"us-west-2a\". The provided availability zone must be in the same region as the Databricks deployment. For example, \"us-west-2a\" is not a valid zone id if the Databricks deployment resides in the \"us-east-1\" region. This is an optional field at cluster creation, and if not specified, the zone \"auto\" will be used. If the zone specified is \"auto\", will try to place cluster in a zone with high availability, and will retry placement in a different AZ if there is not enough capacity. The list of available zones as well as the default value can be found by using the ``List Zones`` method."
              }
            ]
          },
          {
            "name": "azure_attributes",
            "type": "object",
            "description": "Attributes related to clusters running on Microsoft Azure. If not specified at cluster creation, a set of default values will be used.",
            "children": [
              {
                "name": "availability",
                "type": "string",
                "description": "Availability type used for all subsequent nodes past the ``first_on_demand`` ones. Note: If ``first_on_demand`` is zero, this availability type will be used for the entire cluster. (ON_DEMAND_AZURE, SPOT_AZURE, SPOT_WITH_FALLBACK_AZURE)"
              },
              {
                "name": "capacity_reservation_group",
                "type": "string",
                "description": "The Azure capacity reservation group resource ID to use for launching VMs. When specified, VMs will be launched using the provided capacity reservation. Capacity reservations can only be specified when the workspace uses injected vnet (i.e. customer defined vnet not managed by databricks). Ensure the databricks-login-prod Enterprise Application is granted the following four permissions: 1. Microsoft.Compute/capacityReservationGroups/read 2. Microsoft.Compute/capacityReservationGroups/deploy/action 3. Microsoft.Compute/capacityReservationGroups/capacityReservations/read 4. Microsoft.Compute/capacityReservationGroups/capacityReservations/deploy/action Format: ``/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/capacityReservationGroups/&#123;capacityReservationGroupName&#125;``"
              },
              {
                "name": "first_on_demand",
                "type": "integer",
                "description": "The first ``first_on_demand`` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, ``first_on_demand`` nodes will be placed on on-demand instances and the remainder will be placed on ``availability`` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
              },
              {
                "name": "log_analytics_info",
                "type": "object",
                "description": "Defines values necessary to configure and run Azure Log Analytics agent"
              },
              {
                "name": "spot_bid_max_price",
                "type": "number",
                "description": "The max bid price to be used for Azure spot instances. The Max price for the bid cannot be higher than the on-demand price of the instance. If not specified, the default value is -1, which specifies that the instance cannot be evicted on the basis of price, and only on the basis of availability. Further, the value should &gt; 0 or -1."
              }
            ]
          },
          {
            "name": "cluster_log_conf",
            "type": "object",
            "description": "The configuration for delivering spark logs to a long-term storage destination. Three kinds of destinations (DBFS, S3 and Unity Catalog volumes) are supported. Only one destination can be specified for one cluster. If the conf is given, the logs will be delivered to the destination every ``5 mins``. The destination of driver logs is ``$destination/$clusterId/driver``, while the destination of executor logs is ``$destination/$clusterId/executor``.",
            "children": [
              {
                "name": "dbfs",
                "type": "object",
                "description": "destination needs to be provided. e.g. ``&#123; \"dbfs\" : &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;``"
              },
              {
                "name": "s3",
                "type": "object",
                "description": "destination and either the region or endpoint need to be provided. e.g. ``&#123; \"s3\": &#123; \"destination\" : \"s3://cluster_log_bucket/prefix\", \"region\" : \"us-west-2\" &#125; &#125;`` Cluster iam role is used to access s3, please make sure the cluster iam role in ``instance_profile_arn`` has permission to write data to the s3 destination."
              },
              {
                "name": "volumes",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"volumes\": &#123; \"destination\": \"/Volumes/catalog/schema/volume/cluster_log\" &#125; &#125;``"
              }
            ]
          },
          {
            "name": "cluster_name",
            "type": "string",
            "description": "Cluster name requested by the user. This doesn't have to be unique. If not specified at creation, the cluster name will be an empty string. For job clusters, the cluster name is automatically set based on the job and job run IDs."
          },
          {
            "name": "custom_tags",
            "type": "object",
            "description": "Additional tags for cluster resources. Databricks will tag all cluster resources (e.g., AWS instances and EBS volumes) with these tags in addition to ``default_tags``. Notes: - Currently, Databricks allows at most 45 custom tags - Clusters can only reuse cloud resources if the resources' tags are a subset of the cluster tags"
          },
          {
            "name": "data_security_mode",
            "type": "string",
            "description": "Data security mode decides what data governance model to use when accessing data from a cluster.<br /><br />- ``DATA_SECURITY_MODE_AUTO``: Databricks will choose the most appropriate access mode depending<br />  on your compute configuration.<br />- ``DATA_SECURITY_MODE_STANDARD``: A secure cluster that can be shared by multiple users.<br />  Cluster users are fully isolated so that they cannot see each other’s data and credentials.<br />  Most data governance features are supported in this mode. But programming languages and<br />  cluster features might be limited.<br />- ``DATA_SECURITY_MODE_DEDICATED``: A secure cluster that can only be exclusively used by a<br />  single user specified in ``single_user_name``. Most programming languages, cluster features<br />  and data governance features are available in this mode.<br /><br />The following modes are legacy aliases for the above modes:<br /><br />- ``USER_ISOLATION``: Legacy alias for ``DATA_SECURITY_MODE_STANDARD``.<br />- ``SINGLE_USER``: Legacy alias for ``DATA_SECURITY_MODE_DEDICATED``.<br /><br />The following modes are deprecated starting with Databricks Runtime 15.0 and will be removed for<br />future Databricks Runtime versions:<br /><br />- ``LEGACY_TABLE_ACL``: This mode is for users migrating from legacy Table ACL clusters.<br />- ``LEGACY_PASSTHROUGH``: This mode is for users migrating from legacy Passthrough on high<br />  concurrency clusters.<br />- ``LEGACY_SINGLE_USER``: This mode is for users migrating from legacy Passthrough on standard<br />  clusters.<br />- ``LEGACY_SINGLE_USER_STANDARD``: This mode provides a way that doesn’t have UC nor<br />  passthrough enabled. (DATA_SECURITY_MODE_AUTO, DATA_SECURITY_MODE_DEDICATED, DATA_SECURITY_MODE_STANDARD, LEGACY_PASSTHROUGH, LEGACY_SINGLE_USER, LEGACY_SINGLE_USER_STANDARD, LEGACY_TABLE_ACL, NONE, SINGLE_USER, USER_ISOLATION)"
          },
          {
            "name": "dependency_mode",
            "type": "string",
            "description": "Controls dependency configuration for the cluster. (DEPENDENCY_MODE_AUTO, DEPENDENCY_MODE_CLUSTER_LIBRARIES, DEPENDENCY_MODE_ENVIRONMENTS)"
          },
          {
            "name": "docker_image",
            "type": "object",
            "description": "Custom docker image BYOC",
            "children": [
              {
                "name": "basic_auth",
                "type": "object",
                "description": ""
              },
              {
                "name": "url",
                "type": "string",
                "description": "URL of the docker image."
              }
            ]
          },
          {
            "name": "driver_instance_pool_id",
            "type": "string",
            "description": "The optional ID of the instance pool for the driver of the cluster belongs. The pool cluster uses the instance pool with id (instance_pool_id) if the driver pool is not assigned."
          },
          {
            "name": "driver_node_type_flexibility",
            "type": "object",
            "description": "Flexible node type configuration for the driver node.",
            "children": [
              {
                "name": "alternate_node_type_ids",
                "type": "array",
                "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
              }
            ]
          },
          {
            "name": "driver_node_type_id",
            "type": "string",
            "description": "The node type of the Spark driver. Note that this field is optional; if unset, the driver node type will be set as the same value as ``node_type_id`` defined above. This field, along with node_type_id, should not be set if virtual_cluster_size is set. If both driver_node_type_id, node_type_id, and virtual_cluster_size are specified, driver_node_type_id and node_type_id take precedence."
          },
          {
            "name": "enable_elastic_disk",
            "type": "boolean",
            "description": "Autoscaling Local Storage: when enabled, this cluster will dynamically acquire additional disk space when its Spark workers are running low on disk space."
          },
          {
            "name": "enable_local_disk_encryption",
            "type": "boolean",
            "description": "Whether to enable LUKS on cluster VMs' local disks"
          },
          {
            "name": "gcp_attributes",
            "type": "object",
            "description": "Attributes related to clusters running on Google Cloud Platform. If not specified at cluster creation, a set of default values will be used.",
            "children": [
              {
                "name": "availability",
                "type": "string",
                "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs, on-demand VMs, or preemptible VMs with a fallback to on-demand VMs if the former is unavailable. (ON_DEMAND_GCP, PREEMPTIBLE_GCP, PREEMPTIBLE_WITH_FALLBACK_GCP)"
              },
              {
                "name": "boot_disk_size",
                "type": "integer",
                "description": "Boot disk size in GB"
              },
              {
                "name": "confidential_compute_type",
                "type": "string",
                "description": "The confidential computing technology for this cluster's instances. Currently only SEV_SNP is supported, and only on N2D instance types. When not set, no confidential computing is applied. (CONFIDENTIAL_COMPUTE_TYPE_NONE, SEV_SNP)"
              },
              {
                "name": "first_on_demand",
                "type": "integer",
                "description": "The first ``first_on_demand`` nodes of the cluster will be placed on on-demand instances. This value should be greater than 0, to make sure the cluster driver node is placed on an on-demand instance. If this value is greater than or equal to the current cluster size, all nodes will be placed on on-demand instances. If this value is less than the current cluster size, ``first_on_demand`` nodes will be placed on on-demand instances and the remainder will be placed on ``availability`` instances. Note that this value does not affect cluster size and cannot currently be mutated over the lifetime of a cluster."
              },
              {
                "name": "google_service_account",
                "type": "string",
                "description": "If provided, the cluster will impersonate the google service account when accessing gcloud services (like GCS). The google service account must have previously been added to the Databricks environment by an account administrator."
              },
              {
                "name": "local_ssd_count",
                "type": "integer",
                "description": "If provided, each node (workers and driver) in the cluster will have this number of local SSDs attached. Each local SSD is 375GB in size. Refer to `GCP documentation <https://cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds>`__ for the supported number of local SSDs for each instance type."
              },
              {
                "name": "use_preemptible_executors",
                "type": "boolean",
                "description": "This field determines whether the spark executors will be scheduled to run on preemptible VMs (when set to true) versus standard compute engine VMs (when set to false; default). Note: Soon to be deprecated, use the 'availability' field instead."
              },
              {
                "name": "zone_id",
                "type": "string",
                "description": "Identifier for the availability zone in which the cluster resides. This can be one of the following: - \"HA\" =&gt; High availability, spread nodes across availability zones for a Databricks deployment region [default]. - \"AUTO\" =&gt; Databricks picks an availability zone to schedule the cluster on. - A GCP availability zone =&gt; Pick One of the available zones for (machine type + region) from https://cloud.google.com/compute/docs/regions-zones."
              }
            ]
          },
          {
            "name": "init_scripts",
            "type": "array",
            "description": "The configuration for storing init scripts. Any number of destinations can be specified. The scripts are executed sequentially in the order provided. If ``cluster_log_conf`` is specified, init script logs are sent to ``&lt;destination&gt;/&lt;cluster-ID&gt;/init_scripts``.",
            "children": [
              {
                "name": "abfss",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``abfss://&lt;container-name&gt;@&lt;storage-account-name&gt;.dfs.core.windows.net/&lt;directory-name&gt;``"
              },
              {
                "name": "dbfs",
                "type": "object",
                "description": "destination needs to be provided. e.g. ``&#123; \"dbfs\": &#123; \"destination\" : \"dbfs:/home/cluster_log\" &#125; &#125;``"
              },
              {
                "name": "file",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"file\": &#123; \"destination\": \"file:/my/local/file.sh\" &#125; &#125;``"
              },
              {
                "name": "gcs",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"gcs\": &#123; \"destination\": \"gs://my-bucket/file.sh\" &#125; &#125;``"
              },
              {
                "name": "s3",
                "type": "object",
                "description": "destination and either the region or endpoint need to be provided. e.g. ``&#123; \\\"s3\\\": &#123; \\\"destination\\\": \\\"s3://cluster_log_bucket/prefix\\\", \\\"region\\\": \\\"us-west-2\\\" &#125; &#125;`` Cluster iam role is used to access s3, please make sure the cluster iam role in ``instance_profile_arn`` has permission to write data to the s3 destination."
              },
              {
                "name": "volumes",
                "type": "object",
                "description": "destination needs to be provided. e.g. ``&#123; \\\"volumes\\\" : &#123; \\\"destination\\\" : \\\"/Volumes/my-init.sh\\\" &#125; &#125;``"
              },
              {
                "name": "workspace",
                "type": "object",
                "description": "destination needs to be provided, e.g. ``&#123; \"workspace\": &#123; \"destination\": \"/cluster-init-scripts/setup-datadog.sh\" &#125; &#125;``"
              }
            ]
          },
          {
            "name": "instance_pool_id",
            "type": "string",
            "description": "The optional ID of the instance pool to which the cluster belongs."
          },
          {
            "name": "is_single_node",
            "type": "boolean",
            "description": "This field can only be used when ``kind = CLASSIC_PREVIEW``. When set to true, Databricks will automatically set single node related ``custom_tags``, ``spark_conf``, and ``num_workers``"
          },
          {
            "name": "kind",
            "type": "string",
            "description": "The kind of compute described by this compute specification.<br /><br />Depending on ``kind``, different validations and default values will be applied.<br /><br />Clusters with ``kind = CLASSIC_PREVIEW`` support the following fields, whereas clusters with no<br />specified ``kind`` do not.<br /><br />- [is_single_node](/api/workspace/clusters/create#is_single_node)<br />- [use_ml_runtime](/api/workspace/clusters/create#use_ml_runtime)<br /><br />By using the `simple form <https://docs.databricks.com/compute/simple-form.html>`__, your<br />clusters are automatically using ``kind = CLASSIC_PREVIEW``. (CLASSIC_PREVIEW)"
          },
          {
            "name": "node_type_id",
            "type": "string",
            "description": "This field encodes, through a single value, the resources available to each of the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or compute intensive workloads. A list of available node types can be retrieved by using the `clusters/listNodeTypes <https://docs.databricks.com/api/workspace/clusters/listnodetypes>`__ API call."
          },
          {
            "name": "num_workers",
            "type": "integer",
            "description": "Number of worker nodes that this cluster should have. A cluster has one Spark Driver and ``num_workers`` Executors for a total of ``num_workers`` + 1 Spark nodes. Note: When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual current number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field will immediately be updated to reflect the target size of 10 workers, whereas the workers listed in ``spark_info`` will gradually increase from 5 to 10 as the new nodes are provisioned."
          },
          {
            "name": "policy_id",
            "type": "string",
            "description": "The ID of the cluster policy used to create the cluster if applicable."
          },
          {
            "name": "remote_disk_throughput",
            "type": "integer",
            "description": "If set, what the configurable throughput (in Mb/s) for the remote disk is. Currently only supported for GCP HYPERDISK_BALANCED disks."
          },
          {
            "name": "runtime_engine",
            "type": "string",
            "description": "Determines the cluster's runtime engine, either standard or Photon. This field is not compatible with legacy ``spark_version`` values that contain ``-photon-``. Remove ``-photon-`` from the ``spark_version`` and set ``runtime_engine`` to ``PHOTON``. If left unspecified, the runtime engine defaults to standard unless the spark_version contains -photon-, in which case Photon will be used. (NULL, PHOTON, STANDARD)"
          },
          {
            "name": "single_user_name",
            "type": "string",
            "description": "Single user name if data_security_mode is ``SINGLE_USER``"
          },
          {
            "name": "spark_conf",
            "type": "object",
            "description": "An object containing a set of optional, user-specified Spark configuration key-value pairs. Users can also pass in a string of extra JVM options to the driver and the executors via ``spark.driver.extraJavaOptions`` and ``spark.executor.extraJavaOptions`` respectively."
          },
          {
            "name": "spark_env_vars",
            "type": "object",
            "description": "An object containing a set of optional, user-specified environment variable key-value pairs. Please note that key-value pair of the form (X,Y) will be exported as is (i.e., ``export X='Y'``) while launching the driver and workers. In order to specify an additional set of ``SPARK_DAEMON_JAVA_OPTS``, we recommend appending them to ``$SPARK_DAEMON_JAVA_OPTS`` as shown in the example below. This ensures that all default databricks managed environmental variables are included as well. Example Spark environment variables: ``&#123;\"SPARK_WORKER_MEMORY\": \"28000m\", \"SPARK_LOCAL_DIRS\": \"/local_disk0\"&#125;`` or ``&#123;\"SPARK_DAEMON_JAVA_OPTS\": \"$SPARK_DAEMON_JAVA_OPTS -Dspark.shuffle.service.enabled=true\"&#125;``"
          },
          {
            "name": "spark_version",
            "type": "string",
            "description": "The Spark version of the cluster, e.g. ``3.3.x-scala2.11``. A list of available Spark versions can be retrieved by using the `clusters/sparkVersions <https://docs.databricks.com/api/workspace/clusters/sparkversions>`__ API call."
          },
          {
            "name": "ssh_public_keys",
            "type": "array",
            "description": "SSH public key contents that will be added to each Spark node in this cluster. The corresponding private keys can be used to login with the user name ``ubuntu`` on port ``2200``. Up to 10 keys can be specified."
          },
          {
            "name": "total_initial_remote_disk_size",
            "type": "integer",
            "description": "If set, what the total initial volume size (in GB) of the remote disks should be. Currently only supported for GCP HYPERDISK_BALANCED disks."
          },
          {
            "name": "use_ml_runtime",
            "type": "boolean",
            "description": "This field can only be used when ``kind = CLASSIC_PREVIEW``. ``effective_spark_version`` is determined by ``spark_version`` (DBR release), this field ``use_ml_runtime``, and whether ``node_type_id`` is gpu node or not."
          },
          {
            "name": "worker_node_type_flexibility",
            "type": "object",
            "description": "Flexible node type configuration for worker nodes.",
            "children": [
              {
                "name": "alternate_node_type_ids",
                "type": "array",
                "description": "A list of node type IDs to use as fallbacks when the primary node type is unavailable."
              }
            ]
          },
          {
            "name": "workload_type",
            "type": "object",
            "description": "Cluster Attributes showing for clusters workload types.",
            "children": [
              {
                "name": "clients",
                "type": "object",
                "description": "defined what type of clients can use the cluster. E.g. Notebooks, Jobs"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "violations",
    "type": "object",
    "description": "An object containing key-value mappings representing the first 200 policy validation errors. The keys indicate the path where the policy validation error is occurring. The values indicate an error message describing the policy validation error."
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
    <td><a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Returns the policy compliance status of a cluster. Clusters could be out of compliance if their policy</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns the policy compliance status of all clusters that use a given policy. Clusters could be out of</td>
</tr>
<tr>
    <td><a href="#enforce"><CopyableCode code="enforce" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Updates a cluster to be compliant with the current version of its policy.</td>
</tr>
<tr>
    <td><a href="#cancel_pending_enforcement"><CopyableCode code="cancel_pending_enforcement" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a></td>
    <td></td>
    <td>Cancels a pending enforcement on a cluster. After canceling the pending enforcement, the cluster will</td>
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
<tr id="parameter-cluster_id">
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the cluster to get the compliance status</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>Canonical unique identifier for the cluster policy.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token that can be used to navigate to the next page or previous page as returned by ``next_page_token`` or ``prev_page_token``.</td>
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

Returns the policy compliance status of a cluster. Clusters could be out of compliance if their policy

```sql
SELECT
is_compliant,
pending_enforcement,
violations
FROM databricks_workspace.compute.policy_compliance_for_clusters
WHERE cluster_id = '{{ cluster_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns the policy compliance status of all clusters that use a given policy. Clusters could be out of

```sql
SELECT
cluster_id,
is_compliant,
pending_enforcement,
violations
FROM databricks_workspace.compute.policy_compliance_for_clusters
WHERE policy_id = '{{ policy_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="enforce"
    values={[
        { label: 'enforce', value: 'enforce' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="enforce">

Updates a cluster to be compliant with the current version of its policy.

```sql
INSERT INTO databricks_workspace.compute.policy_compliance_for_clusters (
cluster_id,
enforce_mode,
validate_only,
deployment_name
)
SELECT 
'{{ cluster_id }}' /* required */,
'{{ enforce_mode }}',
{{ validate_only }},
'{{ deployment_name }}'
RETURNING
changes,
enforce_result,
has_changes
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: policy_compliance_for_clusters
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the policy_compliance_for_clusters resource.
    - name: cluster_id
      value: "{{ cluster_id }}"
      description: |
        The ID of the cluster you want to enforce policy compliance on.
    - name: enforce_mode
      value: "{{ enforce_mode }}"
      description: |
        Determines how changes should be made to clusters that are not in \`\`TERMINATED\`\` state. - \`\`ENFORCE_IMMEDIATELY\`\`: If the cluster is in a \`\`RUNNING\`\` state, it will be restarted so that the new attributes can take effect. For other states aside from \`\`TERMINATED\`\` state, the request will be rejected. - \`\`WAIT_FOR_TERMINATION\`\`: The cluster is not immediately edited. Instead, a pending enforcement is scheduled to update the cluster when it terminates or restarts. When this occurs, \`\`enforce_result\`\` will contain \`\`DEFERRED\`\`. Only workspace admins can use this mode. Regardless of the enforce mode, clusters in \`\`TERMINATED\`\` state are immediately edited.
    - name: validate_only
      value: {{ validate_only }}
      description: |
        If set, previews the changes that would be made to a cluster to enforce compliance but does not update the cluster.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel_pending_enforcement"
    values={[
        { label: 'cancel_pending_enforcement', value: 'cancel_pending_enforcement' }
    ]}
>
<TabItem value="cancel_pending_enforcement">

Cancels a pending enforcement on a cluster. After canceling the pending enforcement, the cluster will

```sql
EXEC databricks_workspace.compute.policy_compliance_for_clusters.cancel_pending_enforcement 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"allow_missing": {{ allow_missing }}
}'
;
```
</TabItem>
</Tabs>
