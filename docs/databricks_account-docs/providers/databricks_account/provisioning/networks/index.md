---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - networks
  - provisioning
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>networks</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `string` |  |
| <CopyableCode code="creation_time" /> | `integer` |  |
| <CopyableCode code="error_messages" /> | `array` |  |
| <CopyableCode code="network_id" /> | `string` |  |
| <CopyableCode code="network_name" /> | `string` |  |
| <CopyableCode code="security_group_ids" /> | `array` |  |
| <CopyableCode code="subnet_ids" /> | `array` |  |
| <CopyableCode code="vpc_endpoints" /> | `object` |  |
| <CopyableCode code="vpc_id" /> | `string` |  |
| <CopyableCode code="vpc_status" /> | `string` |  |
| <CopyableCode code="warning_messages" /> | `array` |  |
| <CopyableCode code="workspace_id" /> | `integer` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, network_id" /> | Gets a Databricks network configuration, which represents an AWS VPC and its resources.  This requires a pre-existing VPC and subnets. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all Databricks network configurations for an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a Databricks network configuration that represents an AWS VPC and its resources. The VPC will be used for new Databricks clusters. This requires a pre-existing VPC and subnets. For VPC requirements, see |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, network_id" /> | Deletes a Databricks network configuration, which represents a cloud VPC and its resources. You cannot delete a network that is associated with a workspace. |
