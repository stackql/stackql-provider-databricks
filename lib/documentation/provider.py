
def generate_provider_doc(provider, services_df, total_resources, total_methods, base_path):
    """Generate documentation for the provider."""
    
    if provider == 'databricks_account':
        provider_desc = "Account-level features, identity and provisioning for Databricks."
    elif provider == 'databricks_workspace':
        provider_desc = "Manage clusters, jobs, notebooks, MLflow and other Databricks workspace resources."

    # Split services into two columns
    services_list = services_df['name'].tolist()
    mid_point = (len(services_list) + 1) // 2
    col1_services = services_list[:mid_point]
    col2_services = services_list[mid_point:]
    
    doc_content = f"""---
title: {provider}
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - {provider}
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/{provider}/stackql-databricks-provider-featured-image.png
id: {provider}-doc
slug: /providers/{provider}
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

{provider_desc}

:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>{len(services_df)}</b></span><br />
<span>total resources:&nbsp;<b>{total_resources}</b></span><br />
<span>total methods:&nbsp;<b>{total_methods}</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL {provider};
```

## Authentication

To use the {provider}, set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.  

## Services
<div class="row">
<div class="providerDocColumn">
"""
    
    # Add first column of services
    for service in col1_services:
        doc_content += f'<a href="/providers/{provider}/{service}/">{service}</a><br />\n'
    
    doc_content += """</div>
<div class="providerDocColumn">
"""
    
    # Add second column of services
    for service in col2_services:
        doc_content += f'<a href="/providers/{provider}/{service}/">{service}</a><br />\n'
    
    doc_content += "</div>\n</div>"
    
    # Write the documentation to file
    with open(base_path / "index.md", "w") as f:
        f.write(doc_content)