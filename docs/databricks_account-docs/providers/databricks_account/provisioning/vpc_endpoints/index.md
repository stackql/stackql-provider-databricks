---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - vpc_endpoints
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

Operations on a <code>vpc_endpoints</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vpc_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `string` |  |
| <CopyableCode code="aws_account_id" /> | `string` |  |
| <CopyableCode code="aws_endpoint_service_id" /> | `string` |  |
| <CopyableCode code="aws_vpc_endpoint_id" /> | `string` |  |
| <CopyableCode code="region" /> | `string` |  |
| <CopyableCode code="state" /> | `string` |  |
| <CopyableCode code="use_case" /> | `string` |  |
| <CopyableCode code="vpc_endpoint_id" /> | `string` |  |
| <CopyableCode code="vpc_endpoint_name" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, vpc_endpoint_id" /> | Gets a VPC endpoint configuration, which represents a |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all VPC endpoints for an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a VPC endpoint configuration, which represents a |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, vpc_endpoint_id" /> | Deletes a VPC endpoint configuration, which represents an |
