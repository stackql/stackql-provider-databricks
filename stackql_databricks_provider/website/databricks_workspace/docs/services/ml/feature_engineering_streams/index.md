---
title: feature_engineering_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_engineering_streams
  - ml
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

Creates, updates, deletes, gets or lists a <code>feature_engineering_streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_engineering_streams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_engineering_streams" /></td></tr>
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
    "description": "Full three-part (catalog.schema.stream) name of the stream."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "connection_config",
    "type": "object",
    "description": "Specifies how to connect and authenticate to the stream platform.",
    "children": [
      {
        "name": "direct_mtls_config",
        "type": "object",
        "description": "Direct mTLS configuration for stream platform access. This is only used in the short term until UC Kafka Connections support mTLS . Once UC Kafka Connections support mTLS, this will be deprecated.",
        "children": [
          {
            "name": "bootstrap_servers",
            "type": "string",
            "description": "A comma-separated list of host:port pairs for the Kafka bootstrap servers."
          },
          {
            "name": "mtls_config",
            "type": "object",
            "description": "Mutual-TLS (mTLS) authentication configuration. The keystore (client certificate + private key)<br />    and truststore (CAs trusted to verify the broker) live as JKS files on Unity Catalog volumes,<br />    with their passwords stored in Databricks secret scopes. This matches the SSL setup pattern<br />    documented at<br />    https://docs.databricks.com/en/connect/streaming/kafka/authentication#use-ssl-to-connect-databricks-to-kafka.<br /><br />    At materialization time, the generated PySpark code passes the JKS file paths and resolved<br />    passwords through to the Kafka SSL options (kafka.ssl.keystore.location,<br />    kafka.ssl.keystore.password, kafka.ssl.key.password, kafka.ssl.truststore.location,<br />    kafka.ssl.truststore.password). Passwords are resolved on the Spark cluster via<br />    dbutils.secrets.get; this message stores only references, never password values.",
            "children": [
              {
                "name": "keystore_location",
                "type": "string",
                "description": "Unity Catalog volume path to the JKS keystore file containing the client certificate and private key. e.g. \"/Volumes/&lt;catalog&gt;/&lt;schema&gt;/&lt;volume&gt;/client.jks\". The materialization compute must have read permission on this volume."
              },
              {
                "name": "keystore_password_ref",
                "type": "object",
                "description": "Secret-scope reference for the JKS keystore password."
              },
              {
                "name": "key_password_ref",
                "type": "object",
                "description": "Secret-scope reference for the private key password. Often the same value as the keystore password (keytool's default), but provided as a separate field because Apache Kafka requires it as a distinct option (kafka.ssl.key.password)."
              },
              {
                "name": "truststore_location",
                "type": "string",
                "description": "Unity Catalog volume path to the JKS truststore file containing the CA certificate(s) trusted to verify the Kafka broker's server certificate. e.g. \"/Volumes/&lt;catalog&gt;/&lt;schema&gt;/&lt;volume&gt;/truststore.jks\"."
              },
              {
                "name": "truststore_password_ref",
                "type": "object",
                "description": "Secret-scope reference for the JKS truststore password."
              },
              {
                "name": "disable_hostname_verification",
                "type": "boolean",
                "description": "Set to true only when the broker certificate's SAN intentionally does not match the connection endpoint — for example when reaching the cluster through a PrivateLink endpoint whose DNS name is not in the broker certificate. Skipping the hostname check removes a defense against man-in-the-middle attacks; do not enable casually. mTLS client authentication is unaffected by this option. See the Apache Kafka SSL security guide for background on this check: https://kafka.apache.org/42/security/encryption-and-authentication-using-ssl/#host-name-verification"
              }
            ]
          }
        ]
      },
      {
        "name": "uc_connection_name",
        "type": "string",
        "description": "Name of an existing UC Connection for stream platform access. Must be the correct type for the streaming platform (e.g. a Kafka Connection for a Kafka Stream, or a Kinesis Connection for a Kinesis Stream)."
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time at which this Stream was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of the Stream creator."
  },
  {
    "name": "description",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "ingestion_config",
    "type": "object",
    "description": "Configuration for streaming data ingestion: the managed table storing an offline copy of forward fill data and optional historical backfill.",
    "children": [
      {
        "name": "ingestion_destination",
        "type": "object",
        "description": "Destination for the Databricks-managed Delta table that holds an offline copy of the streaming data for querying and training. This table contains both 1) forward-filled data from the Stream and 2) backfilled data from the BackfillSource (if provided). This table is created and managed by Databricks and is deleted when the Stream is deleted.",
        "children": [
          {
            "name": "delta_table_name",
            "type": "string",
            "description": "The full three-part name (catalog, schema, name) of the Delta table to be created for ingestion."
          }
        ]
      },
      {
        "name": "backfill_job_id",
        "type": "integer",
        "description": "The ID of the Databricks Job that performs the historical backfill of the ingestion Delta table."
      },
      {
        "name": "backfill_source",
        "type": "object",
        "description": "A user-provided source for backfilling data. Historical data is used when creating a training set from streaming features linked to this Stream. The backfill data stored in this location will be copied into the ingestion table for offline querying and training. The schema for this source must match exactly that of the key and payload schemas specified for this Stream.",
        "children": [
          {
            "name": "delta_table_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "delta_table_source",
            "type": "object",
            "description": "Deprecated: Use delta_table_name instead. Kept for backwards compatibility. The Delta table source containing the historical data to backfill. Only the delta table name is used for backfill, other fields are ignored.",
            "children": [
              {
                "name": "full_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "dataframe_schema",
                "type": "string",
                "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Required if transformation_sql is specified. Example: &#123;\"type\":\"struct\",\"fields\":[&#123;\"name\":\"col_a\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;,&#123;\"name\":\"col_c\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;]&#125;"
              },
              {
                "name": "entity_columns",
                "type": "array",
                "description": "Deprecated: Use Feature.entity instead. Kept for backwards compatibility. The entity columns of the Delta table."
              },
              {
                "name": "filter_condition",
                "type": "string",
                "description": "Single WHERE clause to filter delta table before applying transformations. Will be row-wise evaluated, so should only include conditionals and projections."
              },
              {
                "name": "timeseries_column",
                "type": "string",
                "description": "Deprecated: Use Feature.timeseries_column instead. Kept for backwards compatibility. The timeseries column of the Delta table."
              },
              {
                "name": "transformation_sql",
                "type": "string",
                "description": "A single SQL SELECT expression applied after filter_condition. Should contains all the columns needed (eg. \"SELECT *, col_a + col_b AS col_c FROM x.y.z WHERE col_a &gt; 0\" would have ``transformation_sql`` \"*, col_a + col_b AS col_c\") If transformation_sql is not provided, all columns of the delta table are present in the DataSource dataframe."
              }
            ]
          }
        ]
      },
      {
        "name": "deduplication_columns",
        "type": "array",
        "description": "Column paths used to identify duplicate rows during ingestion; only one row per distinct combination of these values is kept. Use dot notation for nested fields (e.g. ``value.user_id``). Empty list means every column is compared."
      },
      {
        "name": "ingestion_job_id",
        "type": "integer",
        "description": "The ID of the Databricks Job that performs the forward-fill ingestion."
      },
      {
        "name": "ingestion_pipeline_id",
        "type": "string",
        "description": "The ID of the SDP pipeline that continuously copies new events from the streaming source into the ingestion Delta table."
      }
    ]
  },
  {
    "name": "schema_config",
    "type": "object",
    "description": "Schema definitions for the stream, provided either directly on the Stream or resolved from an external schema registry through a UC Connection.",
    "children": [
      {
        "name": "direct_schemas",
        "type": "object",
        "description": "Schema definitions provided directly on the Stream.",
        "children": [
          {
            "name": "key_schema",
            "type": "object",
            "description": "Schema for the message key. This is only used for Kafka streams. For Kafka, at least one of payload_schema or key_schema must be specified.",
            "children": [
              {
                "name": "avro_schema",
                "type": "string",
                "description": ""
              },
              {
                "name": "json_schema",
                "type": "string",
                "description": "Schema of the JSON object in standard IETF JSON schema format (https://json-schema.org/)."
              },
              {
                "name": "proto_schema",
                "type": "object",
                "description": "Protocol Buffer schema with its payload message name."
              }
            ]
          },
          {
            "name": "payload_schema",
            "type": "object",
            "description": "Schema for the message payload. For Kafka, this is the value schema. Unless the platform supports another schema (e.g. keys for Kafka), this must be specified.",
            "children": [
              {
                "name": "avro_schema",
                "type": "string",
                "description": ""
              },
              {
                "name": "json_schema",
                "type": "string",
                "description": "Schema of the JSON object in standard IETF JSON schema format (https://json-schema.org/)."
              },
              {
                "name": "proto_schema",
                "type": "object",
                "description": "Protocol Buffer schema with its payload message name."
              }
            ]
          }
        ]
      },
      {
        "name": "schema_registry_config",
        "type": "object",
        "description": "Resolve schemas from an external schema registry.",
        "children": [
          {
            "name": "api_secret_ref",
            "type": "object",
            "description": "Reference to the schema registry API secret in a Databricks secret scope.",
            "children": [
              {
                "name": "scope",
                "type": "string",
                "description": "The Databricks secret scope name."
              },
              {
                "name": "key",
                "type": "string",
                "description": "The key within the scope."
              }
            ]
          },
          {
            "name": "key_schema_locator",
            "type": "object",
            "description": "Schema locator for the message key. Only used for Kafka streams. At least one of payload_schema_locator or key_schema_locator must be set.",
            "children": [
              {
                "name": "format",
                "type": "string",
                "description": "Serialization format for this schema. (FORMAT_AVRO, FORMAT_JSON, FORMAT_PROTOBUF)"
              },
              {
                "name": "confluent_schema",
                "type": "object",
                "description": "Confluent Schema Registry schema locator."
              }
            ]
          },
          {
            "name": "payload_schema_locator",
            "type": "object",
            "description": "Schema locator for the message payload. For Kafka this is the value. At least one of payload_schema_locator or key_schema_locator must be set.",
            "children": [
              {
                "name": "format",
                "type": "string",
                "description": "Serialization format for this schema. (FORMAT_AVRO, FORMAT_JSON, FORMAT_PROTOBUF)"
              },
              {
                "name": "confluent_schema",
                "type": "object",
                "description": "Confluent Schema Registry schema locator."
              }
            ]
          },
          {
            "name": "uc_connection",
            "type": "string",
            "description": "A Schema Registry UC Connection object."
          }
        ]
      }
    ]
  },
  {
    "name": "source_config",
    "type": "object",
    "description": "Source-specific configuration. Determines the streaming platform source.",
    "children": [
      {
        "name": "kafka_stream_config",
        "type": "object",
        "description": "Configuration for Apache Kafka streams.",
        "children": [
          {
            "name": "subscription_mode",
            "type": "object",
            "description": "Options to configure which Kafka topics to pull data from.",
            "children": [
              {
                "name": "assign",
                "type": "string",
                "description": "A JSON string that contains the specific topic-partitions to consume from. For example, for '&#123;\"topicA\":[0,1],\"topicB\":[2,4]&#125;', topicA's 0'th and 1st partitions will be consumed from."
              },
              {
                "name": "subscribe",
                "type": "string",
                "description": "A comma-separated list of Kafka topics to read from. For example, 'topicA,topicB,topicC'."
              },
              {
                "name": "subscribe_pattern",
                "type": "string",
                "description": "A regular expression matching topics to subscribe to. For example, 'topic.*' will subscribe to all topics starting with 'topic'."
              }
            ]
          },
          {
            "name": "extra_options",
            "type": "object",
            "description": "Optional Kafka source or consumer options, validated against a server-side allowlist at request time. Allowed keys: - ``maxOffsetsPerTrigger`` - ``startingOffsets`` - ``includeHeaders`` - ``kafka.request.timeout.ms`` - ``kafka.session.timeout.ms`` - ``kafka.max.partition.fetch.bytes`` The following keys are ingestion-only and are stripped before being forwarded to the materialization pipeline: - ``maxOffsetsPerTrigger`` - ``startingOffsets`` Auth and connection details belong on the parent Stream's ``connection_config``, not here."
          }
        ]
      },
      {
        "name": "kinesis_stream_config",
        "type": "object",
        "description": "Configuration for AWS Kinesis Data Streams.",
        "children": [
          {
            "name": "extra_options",
            "type": "object",
            "description": "Optional Kinesis source options, validated against a server-side allowlist at request time. Auth and connection details belong on the parent Stream's ``connection_config``, not here."
          },
          {
            "name": "stream_arns",
            "type": "object",
            "description": "Kinesis stream ARNs to read from.",
            "children": [
              {
                "name": "arns",
                "type": "array",
                "description": "Kinesis stream ARNs to read from. For example, 'arn:aws:kinesis:us-west-2:111122223333:stream/stream-a'."
              }
            ]
          },
          {
            "name": "stream_names",
            "type": "object",
            "description": "Kinesis stream names to read from.",
            "children": [
              {
                "name": "names",
                "type": "array",
                "description": "Kinesis stream names to read from."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time at which this Stream was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the Stream."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Full three-part (catalog.schema.stream) name of the stream."
  },
  {
    "name": "browse_only",
    "type": "boolean",
    "description": "Indicates whether the principal is limited to retrieving metadata for the associated object through the BROWSE privilege when include_browse is enabled in the request."
  },
  {
    "name": "connection_config",
    "type": "object",
    "description": "Specifies how to connect and authenticate to the stream platform.",
    "children": [
      {
        "name": "direct_mtls_config",
        "type": "object",
        "description": "Direct mTLS configuration for stream platform access. This is only used in the short term until UC Kafka Connections support mTLS . Once UC Kafka Connections support mTLS, this will be deprecated.",
        "children": [
          {
            "name": "bootstrap_servers",
            "type": "string",
            "description": "A comma-separated list of host:port pairs for the Kafka bootstrap servers."
          },
          {
            "name": "mtls_config",
            "type": "object",
            "description": "Mutual-TLS (mTLS) authentication configuration. The keystore (client certificate + private key)<br />    and truststore (CAs trusted to verify the broker) live as JKS files on Unity Catalog volumes,<br />    with their passwords stored in Databricks secret scopes. This matches the SSL setup pattern<br />    documented at<br />    https://docs.databricks.com/en/connect/streaming/kafka/authentication#use-ssl-to-connect-databricks-to-kafka.<br /><br />    At materialization time, the generated PySpark code passes the JKS file paths and resolved<br />    passwords through to the Kafka SSL options (kafka.ssl.keystore.location,<br />    kafka.ssl.keystore.password, kafka.ssl.key.password, kafka.ssl.truststore.location,<br />    kafka.ssl.truststore.password). Passwords are resolved on the Spark cluster via<br />    dbutils.secrets.get; this message stores only references, never password values.",
            "children": [
              {
                "name": "keystore_location",
                "type": "string",
                "description": "Unity Catalog volume path to the JKS keystore file containing the client certificate and private key. e.g. \"/Volumes/&lt;catalog&gt;/&lt;schema&gt;/&lt;volume&gt;/client.jks\". The materialization compute must have read permission on this volume."
              },
              {
                "name": "keystore_password_ref",
                "type": "object",
                "description": "Secret-scope reference for the JKS keystore password."
              },
              {
                "name": "key_password_ref",
                "type": "object",
                "description": "Secret-scope reference for the private key password. Often the same value as the keystore password (keytool's default), but provided as a separate field because Apache Kafka requires it as a distinct option (kafka.ssl.key.password)."
              },
              {
                "name": "truststore_location",
                "type": "string",
                "description": "Unity Catalog volume path to the JKS truststore file containing the CA certificate(s) trusted to verify the Kafka broker's server certificate. e.g. \"/Volumes/&lt;catalog&gt;/&lt;schema&gt;/&lt;volume&gt;/truststore.jks\"."
              },
              {
                "name": "truststore_password_ref",
                "type": "object",
                "description": "Secret-scope reference for the JKS truststore password."
              },
              {
                "name": "disable_hostname_verification",
                "type": "boolean",
                "description": "Set to true only when the broker certificate's SAN intentionally does not match the connection endpoint — for example when reaching the cluster through a PrivateLink endpoint whose DNS name is not in the broker certificate. Skipping the hostname check removes a defense against man-in-the-middle attacks; do not enable casually. mTLS client authentication is unaffected by this option. See the Apache Kafka SSL security guide for background on this check: https://kafka.apache.org/42/security/encryption-and-authentication-using-ssl/#host-name-verification"
              }
            ]
          }
        ]
      },
      {
        "name": "uc_connection_name",
        "type": "string",
        "description": "Name of an existing UC Connection for stream platform access. Must be the correct type for the streaming platform (e.g. a Kafka Connection for a Kafka Stream, or a Kinesis Connection for a Kinesis Stream)."
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time at which this Stream was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of the Stream creator."
  },
  {
    "name": "description",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "ingestion_config",
    "type": "object",
    "description": "Configuration for streaming data ingestion: the managed table storing an offline copy of forward fill data and optional historical backfill.",
    "children": [
      {
        "name": "ingestion_destination",
        "type": "object",
        "description": "Destination for the Databricks-managed Delta table that holds an offline copy of the streaming data for querying and training. This table contains both 1) forward-filled data from the Stream and 2) backfilled data from the BackfillSource (if provided). This table is created and managed by Databricks and is deleted when the Stream is deleted.",
        "children": [
          {
            "name": "delta_table_name",
            "type": "string",
            "description": "The full three-part name (catalog, schema, name) of the Delta table to be created for ingestion."
          }
        ]
      },
      {
        "name": "backfill_job_id",
        "type": "integer",
        "description": "The ID of the Databricks Job that performs the historical backfill of the ingestion Delta table."
      },
      {
        "name": "backfill_source",
        "type": "object",
        "description": "A user-provided source for backfilling data. Historical data is used when creating a training set from streaming features linked to this Stream. The backfill data stored in this location will be copied into the ingestion table for offline querying and training. The schema for this source must match exactly that of the key and payload schemas specified for this Stream.",
        "children": [
          {
            "name": "delta_table_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "delta_table_source",
            "type": "object",
            "description": "Deprecated: Use delta_table_name instead. Kept for backwards compatibility. The Delta table source containing the historical data to backfill. Only the delta table name is used for backfill, other fields are ignored.",
            "children": [
              {
                "name": "full_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "dataframe_schema",
                "type": "string",
                "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Required if transformation_sql is specified. Example: &#123;\"type\":\"struct\",\"fields\":[&#123;\"name\":\"col_a\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;,&#123;\"name\":\"col_c\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;]&#125;"
              },
              {
                "name": "entity_columns",
                "type": "array",
                "description": "Deprecated: Use Feature.entity instead. Kept for backwards compatibility. The entity columns of the Delta table."
              },
              {
                "name": "filter_condition",
                "type": "string",
                "description": "Single WHERE clause to filter delta table before applying transformations. Will be row-wise evaluated, so should only include conditionals and projections."
              },
              {
                "name": "timeseries_column",
                "type": "string",
                "description": "Deprecated: Use Feature.timeseries_column instead. Kept for backwards compatibility. The timeseries column of the Delta table."
              },
              {
                "name": "transformation_sql",
                "type": "string",
                "description": "A single SQL SELECT expression applied after filter_condition. Should contains all the columns needed (eg. \"SELECT *, col_a + col_b AS col_c FROM x.y.z WHERE col_a &gt; 0\" would have ``transformation_sql`` \"*, col_a + col_b AS col_c\") If transformation_sql is not provided, all columns of the delta table are present in the DataSource dataframe."
              }
            ]
          }
        ]
      },
      {
        "name": "deduplication_columns",
        "type": "array",
        "description": "Column paths used to identify duplicate rows during ingestion; only one row per distinct combination of these values is kept. Use dot notation for nested fields (e.g. ``value.user_id``). Empty list means every column is compared."
      },
      {
        "name": "ingestion_job_id",
        "type": "integer",
        "description": "The ID of the Databricks Job that performs the forward-fill ingestion."
      },
      {
        "name": "ingestion_pipeline_id",
        "type": "string",
        "description": "The ID of the SDP pipeline that continuously copies new events from the streaming source into the ingestion Delta table."
      }
    ]
  },
  {
    "name": "schema_config",
    "type": "object",
    "description": "Schema definitions for the stream, provided either directly on the Stream or resolved from an external schema registry through a UC Connection.",
    "children": [
      {
        "name": "direct_schemas",
        "type": "object",
        "description": "Schema definitions provided directly on the Stream.",
        "children": [
          {
            "name": "key_schema",
            "type": "object",
            "description": "Schema for the message key. This is only used for Kafka streams. For Kafka, at least one of payload_schema or key_schema must be specified.",
            "children": [
              {
                "name": "avro_schema",
                "type": "string",
                "description": ""
              },
              {
                "name": "json_schema",
                "type": "string",
                "description": "Schema of the JSON object in standard IETF JSON schema format (https://json-schema.org/)."
              },
              {
                "name": "proto_schema",
                "type": "object",
                "description": "Protocol Buffer schema with its payload message name."
              }
            ]
          },
          {
            "name": "payload_schema",
            "type": "object",
            "description": "Schema for the message payload. For Kafka, this is the value schema. Unless the platform supports another schema (e.g. keys for Kafka), this must be specified.",
            "children": [
              {
                "name": "avro_schema",
                "type": "string",
                "description": ""
              },
              {
                "name": "json_schema",
                "type": "string",
                "description": "Schema of the JSON object in standard IETF JSON schema format (https://json-schema.org/)."
              },
              {
                "name": "proto_schema",
                "type": "object",
                "description": "Protocol Buffer schema with its payload message name."
              }
            ]
          }
        ]
      },
      {
        "name": "schema_registry_config",
        "type": "object",
        "description": "Resolve schemas from an external schema registry.",
        "children": [
          {
            "name": "api_secret_ref",
            "type": "object",
            "description": "Reference to the schema registry API secret in a Databricks secret scope.",
            "children": [
              {
                "name": "scope",
                "type": "string",
                "description": "The Databricks secret scope name."
              },
              {
                "name": "key",
                "type": "string",
                "description": "The key within the scope."
              }
            ]
          },
          {
            "name": "key_schema_locator",
            "type": "object",
            "description": "Schema locator for the message key. Only used for Kafka streams. At least one of payload_schema_locator or key_schema_locator must be set.",
            "children": [
              {
                "name": "format",
                "type": "string",
                "description": "Serialization format for this schema. (FORMAT_AVRO, FORMAT_JSON, FORMAT_PROTOBUF)"
              },
              {
                "name": "confluent_schema",
                "type": "object",
                "description": "Confluent Schema Registry schema locator."
              }
            ]
          },
          {
            "name": "payload_schema_locator",
            "type": "object",
            "description": "Schema locator for the message payload. For Kafka this is the value. At least one of payload_schema_locator or key_schema_locator must be set.",
            "children": [
              {
                "name": "format",
                "type": "string",
                "description": "Serialization format for this schema. (FORMAT_AVRO, FORMAT_JSON, FORMAT_PROTOBUF)"
              },
              {
                "name": "confluent_schema",
                "type": "object",
                "description": "Confluent Schema Registry schema locator."
              }
            ]
          },
          {
            "name": "uc_connection",
            "type": "string",
            "description": "A Schema Registry UC Connection object."
          }
        ]
      }
    ]
  },
  {
    "name": "source_config",
    "type": "object",
    "description": "Source-specific configuration. Determines the streaming platform source.",
    "children": [
      {
        "name": "kafka_stream_config",
        "type": "object",
        "description": "Configuration for Apache Kafka streams.",
        "children": [
          {
            "name": "subscription_mode",
            "type": "object",
            "description": "Options to configure which Kafka topics to pull data from.",
            "children": [
              {
                "name": "assign",
                "type": "string",
                "description": "A JSON string that contains the specific topic-partitions to consume from. For example, for '&#123;\"topicA\":[0,1],\"topicB\":[2,4]&#125;', topicA's 0'th and 1st partitions will be consumed from."
              },
              {
                "name": "subscribe",
                "type": "string",
                "description": "A comma-separated list of Kafka topics to read from. For example, 'topicA,topicB,topicC'."
              },
              {
                "name": "subscribe_pattern",
                "type": "string",
                "description": "A regular expression matching topics to subscribe to. For example, 'topic.*' will subscribe to all topics starting with 'topic'."
              }
            ]
          },
          {
            "name": "extra_options",
            "type": "object",
            "description": "Optional Kafka source or consumer options, validated against a server-side allowlist at request time. Allowed keys: - ``maxOffsetsPerTrigger`` - ``startingOffsets`` - ``includeHeaders`` - ``kafka.request.timeout.ms`` - ``kafka.session.timeout.ms`` - ``kafka.max.partition.fetch.bytes`` The following keys are ingestion-only and are stripped before being forwarded to the materialization pipeline: - ``maxOffsetsPerTrigger`` - ``startingOffsets`` Auth and connection details belong on the parent Stream's ``connection_config``, not here."
          }
        ]
      },
      {
        "name": "kinesis_stream_config",
        "type": "object",
        "description": "Configuration for AWS Kinesis Data Streams.",
        "children": [
          {
            "name": "extra_options",
            "type": "object",
            "description": "Optional Kinesis source options, validated against a server-side allowlist at request time. Auth and connection details belong on the parent Stream's ``connection_config``, not here."
          },
          {
            "name": "stream_arns",
            "type": "object",
            "description": "Kinesis stream ARNs to read from.",
            "children": [
              {
                "name": "arns",
                "type": "array",
                "description": "Kinesis stream ARNs to read from. For example, 'arn:aws:kinesis:us-west-2:111122223333:stream/stream-a'."
              }
            ]
          },
          {
            "name": "stream_names",
            "type": "object",
            "description": "Kinesis stream names to read from.",
            "children": [
              {
                "name": "names",
                "type": "array",
                "description": "Kinesis stream names to read from."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time at which this Stream was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Username of user who last modified the Stream."
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
    <td>Get a Stream by its full three-part name (catalog.schema.stream).</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent"><code>parent</code></a></td>
    <td>List Streams under a given catalog.schema parent.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-stream"><code>stream</code></a></td>
    <td></td>
    <td>Create a Stream, a governed UC entity representing an external streaming data source.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-stream"><code>stream</code></a></td>
    <td></td>
    <td>Update a Stream. Only fields listed in ``update_mask`` are mutated.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a Stream by its full three-part name (catalog.schema.stream).</td>
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
    <td>Full three-part name (catalog.schema.stream) of the Stream to delete.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of results to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page based on a previous query.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Two-part name (catalog.schema) of the parent under which to list Streams.</td>
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

Get a Stream by its full three-part name (catalog.schema.stream).

```sql
SELECT
name,
browse_only,
connection_config,
create_time,
created_by,
description,
ingestion_config,
schema_config,
source_config,
update_time,
updated_by
FROM databricks_workspace.ml.feature_engineering_streams
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Streams under a given catalog.schema parent.

```sql
SELECT
name,
browse_only,
connection_config,
create_time,
created_by,
description,
ingestion_config,
schema_config,
source_config,
update_time,
updated_by
FROM databricks_workspace.ml.feature_engineering_streams
WHERE deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND parent = '{{ parent }}'
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

Create a Stream, a governed UC entity representing an external streaming data source.

```sql
INSERT INTO databricks_workspace.ml.feature_engineering_streams (
stream,
deployment_name
)
SELECT 
'{{ stream }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
browse_only,
connection_config,
create_time,
created_by,
description,
ingestion_config,
schema_config,
source_config,
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_engineering_streams
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the feature_engineering_streams resource.
    - name: stream
      description: |
        The Stream to create.
      value:
        name: "{{ name }}"
        source_config:
          kafka_stream_config:
            subscription_mode:
              assign: "{{ assign }}"
              subscribe: "{{ subscribe }}"
              subscribe_pattern: "{{ subscribe_pattern }}"
            extra_options: "{{ extra_options }}"
          kinesis_stream_config:
            extra_options: "{{ extra_options }}"
            stream_arns:
              arns:
                - "{{ arns }}"
            stream_names:
              names:
                - "{{ names }}"
        connection_config:
          direct_mtls_config:
            bootstrap_servers: "{{ bootstrap_servers }}"
            mtls_config:
              keystore_location: "{{ keystore_location }}"
              keystore_password_ref:
                scope: "{{ scope }}"
                key: "{{ key }}"
              key_password_ref:
                scope: "{{ scope }}"
                key: "{{ key }}"
              truststore_location: "{{ truststore_location }}"
              truststore_password_ref:
                scope: "{{ scope }}"
                key: "{{ key }}"
              disable_hostname_verification: {{ disable_hostname_verification }}
          uc_connection_name: "{{ uc_connection_name }}"
        schema_config:
          direct_schemas:
            key_schema:
              avro_schema: "{{ avro_schema }}"
              json_schema: "{{ json_schema }}"
              proto_schema:
                schema_text: "{{ schema_text }}"
                message_name: "{{ message_name }}"
            payload_schema:
              avro_schema: "{{ avro_schema }}"
              json_schema: "{{ json_schema }}"
              proto_schema:
                schema_text: "{{ schema_text }}"
                message_name: "{{ message_name }}"
          schema_registry_config:
            api_secret_ref:
              scope: "{{ scope }}"
              key: "{{ key }}"
            key_schema_locator:
              format: "{{ format }}"
              confluent_schema:
                subject: "{{ subject }}"
            payload_schema_locator:
              format: "{{ format }}"
              confluent_schema:
                subject: "{{ subject }}"
            uc_connection: "{{ uc_connection }}"
        ingestion_config:
          ingestion_destination:
            delta_table_name: "{{ delta_table_name }}"
          backfill_job_id: {{ backfill_job_id }}
          backfill_source:
            delta_table_name: "{{ delta_table_name }}"
            delta_table_source:
              full_name: "{{ full_name }}"
              dataframe_schema: "{{ dataframe_schema }}"
              entity_columns:
                - "{{ entity_columns }}"
              filter_condition: "{{ filter_condition }}"
              timeseries_column: "{{ timeseries_column }}"
              transformation_sql: "{{ transformation_sql }}"
          deduplication_columns:
            - "{{ deduplication_columns }}"
          ingestion_job_id: {{ ingestion_job_id }}
          ingestion_pipeline_id: "{{ ingestion_pipeline_id }}"
        browse_only: {{ browse_only }}
        create_time: "{{ create_time }}"
        created_by: "{{ created_by }}"
        description: "{{ description }}"
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

Update a Stream. Only fields listed in ``update_mask`` are mutated.

```sql
UPDATE databricks_workspace.ml.feature_engineering_streams
SET 
stream = '{{ stream }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND stream = '{{ stream }}' --required
RETURNING
name,
browse_only,
connection_config,
create_time,
created_by,
description,
ingestion_config,
schema_config,
source_config,
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

Delete a Stream by its full three-part name (catalog.schema.stream).

```sql
DELETE FROM databricks_workspace.ml.feature_engineering_streams
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
