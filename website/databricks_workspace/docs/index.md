---
title: databricks_workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/stackql-databricks-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Manage clusters, jobs, notebooks, MLflow and other Databricks workspace resources.

:::info

For Databricks account operations use the [__`databricks_account`__](https://databricks-account-provider.stackql.io/) provider.

:::

:::info[Provider Summary] 

total services: __18__  
total resources: __204__  

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL databricks_workspace;
```

## Authentication

To use the databricks_workspace, set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.  

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/apps/">apps</a><br />
<a href="/services/cleanrooms/">cleanrooms</a><br />
<a href="/services/compute/">compute</a><br />
<a href="/services/dbsql/">dbsql</a><br />
<a href="/services/deltalivetables/">deltalivetables</a><br />
<a href="/services/deltasharing/">deltasharing</a><br />
<a href="/services/filemanagement/">filemanagement</a><br />
<a href="/services/iam/">iam</a><br />
<a href="/services/lakeview/">lakeview</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/machinelearning/">machinelearning</a><br />
<a href="/services/marketplace/">marketplace</a><br />
<a href="/services/realtimeserving/">realtimeserving</a><br />
<a href="/services/repos/">repos</a><br />
<a href="/services/secrets/">secrets</a><br />
<a href="/services/unitycatalog/">unitycatalog</a><br />
<a href="/services/vectorsearch/">vectorsearch</a><br />
<a href="/services/workflows/">workflows</a><br />
<a href="/services/workspace/">workspace</a><br />
</div>
</div>
