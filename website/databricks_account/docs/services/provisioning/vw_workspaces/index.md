--- 
title: vw_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_workspaces
  - provisioning
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>vw_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vw_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vw_workspaces" /></td></tr>
</tbody></table>

## Fields

See the SQL Definition (view DDL) for fields returned by this view.

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
select
workspace_id,
workspace_name,
deployment_name,
account_id,
aws_region,
workspace_status,
workspace_status_message,
pricing_tier,
is_no_public_ip_enabled,
credentials_id,
JSON_EXTRACT(identity_federation_info, '$.enable_identity_federation') as identity_federation_enabled,
storage_configuration_id,
JSON_EXTRACT(workspace_info, '$.compliance_security_profile.is_enabled') as compliance_security_profile_enabled,
JSON_EXTRACT(workspace_info, '$.enhanced_security_monitoring.is_enabled') as enhanced_security_monitoring_enabled,
creation_time
from databricks_account.provisioning.workspaces 
where account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce' 
```

</TabItem>
<TabItem value="Postgres">

```sql
select 
workspace_id,
workspace_name,
deployment_name,
account_id,
aws_region,
workspace_status,
workspace_status_message,
pricing_tier,
is_no_public_ip_enabled,
credentials_id,
json_extract_path_text(identity_federation_info, 'enable_identity_federation') as identity_federation_enabled,
storage_configuration_id,
json_extract_path_text(workspace_info, 'compliance_security_profile', 'is_enabled') as compliance_security_profile_enabled,
json_extract_path_text(workspace_info, 'enhanced_security_monitoring', 'is_enabled') as enhanced_security_monitoring_enabled,
creation_time
from databricks_account.provisioning.workspaces
where account_id = 'ebfcc5a9-9d49-4c93-b651-b3ee6cf1c9ce' 
```

</TabItem>
</Tabs>
