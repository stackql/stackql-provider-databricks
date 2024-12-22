---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - workspaces
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

Operations on a <code>workspaces</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.workspaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'view', value: 'view', },
        { label: 'resource', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `string` |  |
| <CopyableCode code="aws_region" /> | `string` |  |
| <CopyableCode code="creation_time" /> | `integer` |  |
| <CopyableCode code="credentials_id" /> | `string` |  |
| <CopyableCode code="custom_tags" /> | `object` |  |
| <CopyableCode code="deployment_name" /> | `string` |  |
| <CopyableCode code="is_no_public_ip_enabled" /> | `boolean` |  |
| <CopyableCode code="managed_services_customer_managed_key_id" /> | `string` |  |
| <CopyableCode code="network_id" /> | `string` |  |
| <CopyableCode code="pricing_tier" /> | `string` |  |
| <CopyableCode code="private_access_settings_id" /> | `string` |  |
| <CopyableCode code="storage_configuration_id" /> | `string` |  |
| <CopyableCode code="storage_customer_managed_key_id" /> | `string` |  |
| <CopyableCode code="workspace_id" /> | `integer` |  |
| <CopyableCode code="workspace_name" /> | `string` |  |
| <CopyableCode code="workspace_status" /> | `string` |  |
| <CopyableCode code="workspace_status_message" /> | `string` |  |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `string` |  |
| <CopyableCode code="aws_region" /> | `string` |  |
| <CopyableCode code="creation_time" /> | `integer` |  |
| <CopyableCode code="credentials_id" /> | `string` |  |
| <CopyableCode code="custom_tags" /> | `object` |  |
| <CopyableCode code="deployment_name" /> | `string` |  |
| <CopyableCode code="is_no_public_ip_enabled" /> | `boolean` |  |
| <CopyableCode code="managed_services_customer_managed_key_id" /> | `string` |  |
| <CopyableCode code="network_id" /> | `string` |  |
| <CopyableCode code="pricing_tier" /> | `string` |  |
| <CopyableCode code="private_access_settings_id" /> | `string` |  |
| <CopyableCode code="storage_configuration_id" /> | `string` |  |
| <CopyableCode code="storage_customer_managed_key_id" /> | `string` |  |
| <CopyableCode code="workspace_id" /> | `integer` |  |
| <CopyableCode code="workspace_name" /> | `string` |  |
| <CopyableCode code="workspace_status" /> | `string` |  |
| <CopyableCode code="workspace_status_message" /> | `string` |  |
</TabItem>
</Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, workspace_id" /> | Gets information including status for a Databricks workspace, specified by ID. In the response, the |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all workspaces associated with an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a new workspace using a credential configuration and a storage configuration, an optional network configuration (if using a customer-managed VPC), an optional managed services key configuration (if using customer-managed keys for managed services), and an optional storage key configuration (if using customer-managed keys for storage). The key configurations used for managed services and storage encryption can be the same or different. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, workspace_id" /> | Terminates and deletes a Databricks workspace. From an API perspective, deletion is immediate. However, it might take a few minutes for all workspaces resources to be deleted, depending on the size and number of workspace resources. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id, workspace_id" /> | Updates a workspace configuration for either a running workspace or a failed workspace. The elements that can be updated varies between these two use cases. |
