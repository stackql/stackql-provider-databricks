---
title: network_connectivity
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - network_connectivity
  - settings
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

Operations on a <code>network_connectivity</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_connectivity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.network_connectivity" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="account_id" /> | `string` |  |
| <CopyableCode code="creation_time" /> | `integer` |  |
| <CopyableCode code="egress_config" /> | `object` |  |
| <CopyableCode code="network_connectivity_config_id" /> | `string` |  |
| <CopyableCode code="region" /> | `string` |  |
| <CopyableCode code="updated_time" /> | `integer` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getnetworkconnectivityconfiguration" /> | `SELECT` | <CopyableCode code="account_id, network_connectivity_config_id" /> | Gets a network connectivity configuration. |
| <CopyableCode code="listnetworkconnectivityconfigurations" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets an array of network connectivity configurations. |
| <CopyableCode code="createnetworkconnectivityconfiguration" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a network connectivity configuration (NCC), which provides stable IP CIDR blocks that are associated with your workspace. You can assign an NCC to one or more workspaces in the same region. Once assigned, the workspace serverless compute resources use the same set of stable IP CIDR blocks to access your resources. |
| <CopyableCode code="deletenetworkconnectivityconfiguration" /> | `DELETE` | <CopyableCode code="account_id, network_connectivity_config_id" /> | Deletes a network connectivity configuration. |
