---
title: feature_kafka_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_kafka_configs
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

Creates, updates, deletes, gets or lists a <code>feature_kafka_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_kafka_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_kafka_configs" /></td></tr>
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
    "description": ""
  },
  {
    "name": "auth_config",
    "type": "object",
    "description": "Authentication configuration for connection to topics.",
    "children": [
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
            "description": "Secret-scope reference for the JKS keystore password.",
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
            "name": "key_password_ref",
            "type": "object",
            "description": "Secret-scope reference for the private key password. Often the same value as the keystore password (keytool's default), but provided as a separate field because Apache Kafka requires it as a distinct option (kafka.ssl.key.password).",
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
            "name": "truststore_location",
            "type": "string",
            "description": "Unity Catalog volume path to the JKS truststore file containing the CA certificate(s) trusted to verify the Kafka broker's server certificate. e.g. \"/Volumes/&lt;catalog&gt;/&lt;schema&gt;/&lt;volume&gt;/truststore.jks\"."
          },
          {
            "name": "truststore_password_ref",
            "type": "object",
            "description": "Secret-scope reference for the JKS truststore password.",
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
            "name": "disable_hostname_verification",
            "type": "boolean",
            "description": "Set to true only when the broker certificate's SAN intentionally does not match the connection endpoint — for example when reaching the cluster through a PrivateLink endpoint whose DNS name is not in the broker certificate. Skipping the hostname check removes a defense against man-in-the-middle attacks; do not enable casually. mTLS client authentication is unaffected by this option. See the Apache Kafka SSL security guide for background on this check: https://kafka.apache.org/42/security/encryption-and-authentication-using-ssl/#host-name-verification"
          }
        ]
      },
      {
        "name": "uc_service_credential_name",
        "type": "string",
        "description": "Name of the Unity Catalog service credential. This value will be set under the option databricks.serviceCredential"
      }
    ]
  },
  {
    "name": "backfill_source",
    "type": "object",
    "description": "A user-provided and managed source for backfilling data. Historical data is used when creating a training set from streaming features linked to this Kafka config. In the future, a separate table will be maintained by Databricks for forward filling data. The schema for this source must match exactly that of the key and value schemas specified for this Kafka config.",
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
    "name": "bootstrap_servers",
    "type": "string",
    "description": "A comma-separated list of host/port pairs pointing to Kafka cluster."
  },
  {
    "name": "extra_options",
    "type": "object",
    "description": "Catch-all for miscellaneous options. Keys should be source options or Kafka consumer options (kafka.*)"
  },
  {
    "name": "ingestion_config",
    "type": "object",
    "description": "Configuration for ingesting Kafka data into a Databricks-managed Delta table.",
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
    "name": "key_schema",
    "type": "object",
    "description": "Schema configuration for extracting message keys from topics. At least one of key_schema and value_schema must be provided.",
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
        "description": "Protocol Buffer schema with its payload message name.",
        "children": [
          {
            "name": "schema_text",
            "type": "string",
            "description": "The raw .proto file text (proto2 and proto3 syntax supported, see https://protobuf.dev/programming-guides/proto3/ and https://protobuf.dev/programming-guides/proto2/)."
          },
          {
            "name": "message_name",
            "type": "string",
            "description": "The fully-qualified name of the message within schema_text that describes the Kafka payload (e.g. \"Event\" or \"com.example.Event\" if schema_text declares a package). Identifies which message is used to decode each Kafka record — a .proto file may declare multiple messages but only one represents the payload. Must not be empty."
          }
        ]
      }
    ]
  },
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
    "name": "value_schema",
    "type": "object",
    "description": "Schema configuration for extracting message values from topics. At least one of key_schema and value_schema must be provided.",
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
        "description": "Protocol Buffer schema with its payload message name.",
        "children": [
          {
            "name": "schema_text",
            "type": "string",
            "description": "The raw .proto file text (proto2 and proto3 syntax supported, see https://protobuf.dev/programming-guides/proto3/ and https://protobuf.dev/programming-guides/proto2/)."
          },
          {
            "name": "message_name",
            "type": "string",
            "description": "The fully-qualified name of the message within schema_text that describes the Kafka payload (e.g. \"Event\" or \"com.example.Event\" if schema_text declares a package). Identifies which message is used to decode each Kafka record — a .proto file may declare multiple messages but only one represents the payload. Must not be empty."
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
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "auth_config",
    "type": "object",
    "description": "Authentication configuration for connection to topics.",
    "children": [
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
            "description": "Secret-scope reference for the JKS keystore password.",
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
            "name": "key_password_ref",
            "type": "object",
            "description": "Secret-scope reference for the private key password. Often the same value as the keystore password (keytool's default), but provided as a separate field because Apache Kafka requires it as a distinct option (kafka.ssl.key.password).",
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
            "name": "truststore_location",
            "type": "string",
            "description": "Unity Catalog volume path to the JKS truststore file containing the CA certificate(s) trusted to verify the Kafka broker's server certificate. e.g. \"/Volumes/&lt;catalog&gt;/&lt;schema&gt;/&lt;volume&gt;/truststore.jks\"."
          },
          {
            "name": "truststore_password_ref",
            "type": "object",
            "description": "Secret-scope reference for the JKS truststore password.",
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
            "name": "disable_hostname_verification",
            "type": "boolean",
            "description": "Set to true only when the broker certificate's SAN intentionally does not match the connection endpoint — for example when reaching the cluster through a PrivateLink endpoint whose DNS name is not in the broker certificate. Skipping the hostname check removes a defense against man-in-the-middle attacks; do not enable casually. mTLS client authentication is unaffected by this option. See the Apache Kafka SSL security guide for background on this check: https://kafka.apache.org/42/security/encryption-and-authentication-using-ssl/#host-name-verification"
          }
        ]
      },
      {
        "name": "uc_service_credential_name",
        "type": "string",
        "description": "Name of the Unity Catalog service credential. This value will be set under the option databricks.serviceCredential"
      }
    ]
  },
  {
    "name": "backfill_source",
    "type": "object",
    "description": "A user-provided and managed source for backfilling data. Historical data is used when creating a training set from streaming features linked to this Kafka config. In the future, a separate table will be maintained by Databricks for forward filling data. The schema for this source must match exactly that of the key and value schemas specified for this Kafka config.",
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
    "name": "bootstrap_servers",
    "type": "string",
    "description": "A comma-separated list of host/port pairs pointing to Kafka cluster."
  },
  {
    "name": "extra_options",
    "type": "object",
    "description": "Catch-all for miscellaneous options. Keys should be source options or Kafka consumer options (kafka.*)"
  },
  {
    "name": "ingestion_config",
    "type": "object",
    "description": "Configuration for ingesting Kafka data into a Databricks-managed Delta table.",
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
    "name": "key_schema",
    "type": "object",
    "description": "Schema configuration for extracting message keys from topics. At least one of key_schema and value_schema must be provided.",
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
        "description": "Protocol Buffer schema with its payload message name.",
        "children": [
          {
            "name": "schema_text",
            "type": "string",
            "description": "The raw .proto file text (proto2 and proto3 syntax supported, see https://protobuf.dev/programming-guides/proto3/ and https://protobuf.dev/programming-guides/proto2/)."
          },
          {
            "name": "message_name",
            "type": "string",
            "description": "The fully-qualified name of the message within schema_text that describes the Kafka payload (e.g. \"Event\" or \"com.example.Event\" if schema_text declares a package). Identifies which message is used to decode each Kafka record — a .proto file may declare multiple messages but only one represents the payload. Must not be empty."
          }
        ]
      }
    ]
  },
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
    "name": "value_schema",
    "type": "object",
    "description": "Schema configuration for extracting message values from topics. At least one of key_schema and value_schema must be provided.",
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
        "description": "Protocol Buffer schema with its payload message name.",
        "children": [
          {
            "name": "schema_text",
            "type": "string",
            "description": "The raw .proto file text (proto2 and proto3 syntax supported, see https://protobuf.dev/programming-guides/proto3/ and https://protobuf.dev/programming-guides/proto2/)."
          },
          {
            "name": "message_name",
            "type": "string",
            "description": "The fully-qualified name of the message within schema_text that describes the Kafka payload (e.g. \"Event\" or \"com.example.Event\" if schema_text declares a package). Identifies which message is used to decode each Kafka record — a .proto file may declare multiple messages but only one represents the payload. Must not be empty."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get a Kafka config. During PrPr, Kafka configs can be read and used when creating features under the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Kafka configs. During PrPr, Kafka configs can be read and used when creating features under the</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-kafka_config"><code>kafka_config</code></a></td>
    <td></td>
    <td>Create a Kafka config. During PrPr, Kafka configs can be read and used when creating features under</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-kafka_config"><code>kafka_config</code></a></td>
    <td></td>
    <td>Update a Kafka config. During PrPr, Kafka configs can be read and used when creating features under</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a Kafka config. During PrPr, Kafka configs can be read and used when creating features under</td>
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
    <td>Name of the Kafka config to delete.</td>
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

Get a Kafka config. During PrPr, Kafka configs can be read and used when creating features under the

```sql
SELECT
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
ingestion_config,
key_schema,
subscription_mode,
value_schema
FROM databricks_workspace.ml.feature_kafka_configs
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Kafka configs. During PrPr, Kafka configs can be read and used when creating features under the

```sql
SELECT
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
ingestion_config,
key_schema,
subscription_mode,
value_schema
FROM databricks_workspace.ml.feature_kafka_configs
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
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a Kafka config. During PrPr, Kafka configs can be read and used when creating features under

```sql
INSERT INTO databricks_workspace.ml.feature_kafka_configs (
kafka_config,
deployment_name
)
SELECT 
'{{ kafka_config }}' /* required */,
'{{ deployment_name }}'
RETURNING
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
ingestion_config,
key_schema,
subscription_mode,
value_schema
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_kafka_configs
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the feature_kafka_configs resource.
    - name: kafka_config
      value:
        name: "{{ name }}"
        bootstrap_servers: "{{ bootstrap_servers }}"
        subscription_mode:
          assign: "{{ assign }}"
          subscribe: "{{ subscribe }}"
          subscribe_pattern: "{{ subscribe_pattern }}"
        auth_config:
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
          uc_service_credential_name: "{{ uc_service_credential_name }}"
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
        extra_options: "{{ extra_options }}"
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
        key_schema:
          avro_schema: "{{ avro_schema }}"
          json_schema: "{{ json_schema }}"
          proto_schema:
            schema_text: "{{ schema_text }}"
            message_name: "{{ message_name }}"
        value_schema:
          avro_schema: "{{ avro_schema }}"
          json_schema: "{{ json_schema }}"
          proto_schema:
            schema_text: "{{ schema_text }}"
            message_name: "{{ message_name }}"
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

Update a Kafka config. During PrPr, Kafka configs can be read and used when creating features under

```sql
UPDATE databricks_workspace.ml.feature_kafka_configs
SET 
kafka_config = '{{ kafka_config }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND kafka_config = '{{ kafka_config }}' --required
RETURNING
name,
auth_config,
backfill_source,
bootstrap_servers,
extra_options,
ingestion_config,
key_schema,
subscription_mode,
value_schema;
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

Delete a Kafka config. During PrPr, Kafka configs can be read and used when creating features under

```sql
DELETE FROM databricks_workspace.ml.feature_kafka_configs
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>
