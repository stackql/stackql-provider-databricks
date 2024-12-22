---
title: custom_app_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - custom_app_integrations
  - oauth
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

Operations on a <code>custom_app_integrations</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_app_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth.custom_app_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="client_id" /> | `string` |  |
| <CopyableCode code="confidential" /> | `boolean` |  |
| <CopyableCode code="create_time" /> | `string` |  |
| <CopyableCode code="created_by" /> | `integer` |  |
| <CopyableCode code="creator_username" /> | `string` |  |
| <CopyableCode code="integration_id" /> | `string` |  |
| <CopyableCode code="redirect_urls" /> | `array` |  |
| <CopyableCode code="scopes" /> | `array` |  |
| <CopyableCode code="token_access_policy" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, integration_id" /> | Gets the Custom OAuth App Integration for the given integration id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Get the list of custom OAuth app integrations for the specified Databricks account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Create Custom OAuth App Integration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, integration_id" /> | Delete an existing Custom OAuth App Integration. You can retrieve the custom OAuth app integration via |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id, integration_id" /> | Updates an existing custom OAuth App Integration. You can retrieve the custom OAuth app integration via |
