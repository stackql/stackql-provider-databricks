---
title: private_access
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - private_access
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

Operations on a <code>private_access</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.private_access" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `string` |  |
| <CopyableCode code="allowed_vpc_endpoint_ids" /> | `array` |  |
| <CopyableCode code="private_access_level" /> | `string` |  |
| <CopyableCode code="private_access_settings_id" /> | `string` |  |
| <CopyableCode code="private_access_settings_name" /> | `string` |  |
| <CopyableCode code="public_access_enabled" /> | `boolean` |  |
| <CopyableCode code="region" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, private_access_settings_id" /> | Gets a private access settings object, which specifies how your workspace is accessed over |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all private access settings objects for an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a private access settings object, which specifies how your workspace is accessed over |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, private_access_settings_id" /> | Deletes a private access settings object, which determines how your workspace is accessed over |
| <CopyableCode code="replace" /> | `REPLACE` | <CopyableCode code="account_id, private_access_settings_id" /> | Updates an existing private access settings object, which specifies how your workspace is accessed over |
