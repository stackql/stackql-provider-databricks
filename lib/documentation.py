import os
from pathlib import Path

def generate_resource_doc(provider, service, resource, methods_df, fields_df, base_path):
    """Generate documentation for a specific resource."""
    # Create directory structure
    resource_path = Path(base_path) / provider / service / resource
    resource_path.mkdir(parents=True, exist_ok=True)
    
    # Generate resource documentation
    doc_content = f"""---
title: {resource}
hide_title: false
hide_table_of_contents: false
keywords:
  - {resource}
  - {service}
  - {provider}
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage {provider} resources using SQL
custom_edit_url: null
image: /img/providers/{provider}/stackql-{provider}-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>{resource}</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="{provider}.{service}.{resource}" /></td></tr>
</tbody></table>

## Fields
"""
    # Add fields section
    if fields_df is not None and not fields_df.empty:
        doc_content += generate_fields_section(fields_df)
    
    # Add methods section
    if methods_df is not None and not methods_df.empty:
        doc_content += generate_methods_section(methods_df)
    
    # Write the documentation to file
    with open(resource_path / "index.md", "w") as f:
        f.write(doc_content)

def generate_service_doc(provider, service, resources_df, base_path):
    """Generate documentation for a service."""
    # Create directory structure
    service_path = Path(base_path) / provider / service
    service_path.mkdir(parents=True, exist_ok=True)
    
    total_resources = len(resources_df)
    
    # Split resources into two columns
    resources_list = resources_df['name'].tolist()
    mid_point = (total_resources + 1) // 2
    col1_resources = resources_list[:mid_point]
    col2_resources = resources_list[mid_point:]
    
    doc_content = f"""---
title: {service}
hide_title: false
hide_table_of_contents: false
keywords:
  - {service}
  - {provider}
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage {provider} resources using SQL
custom_edit_url: null
image: /img/providers/{provider}/stackql-{provider}-provider-featured-image.png
---

{service} service documentation.

:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>{total_resources}</b></span><br />
</div>
</div>

:::

## Resources
<div class="row">
<div class="providerDocColumn">
"""
    
    # Add first column of resources
    for resource in col1_resources:
        doc_content += f'<a href="/providers/{provider}/{service}/{resource}/">{resource}</a><br />\n'
    
    doc_content += """</div>
<div class="providerDocColumn">
"""
    
    # Add second column of resources
    for resource in col2_resources:
        doc_content += f'<a href="/providers/{provider}/{service}/{resource}/">{resource}</a><br />\n'
    
    doc_content += "</div>\n</div>"
    
    # Write the documentation to file
    with open(service_path / "index.md", "w") as f:
        f.write(doc_content)

def generate_provider_doc(provider, services_df, total_resources, total_methods, base_path):
    """Generate documentation for the provider."""
    provider_path = Path(base_path) / provider
    provider_path.mkdir(parents=True, exist_ok=True)
    
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
  - {provider}
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage {provider} resources using SQL
custom_edit_url: null
image: /img/providers/{provider}/stackql-{provider}-provider-featured-image.png
id: {provider}-doc
slug: /providers/{provider}
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Core cloud services from {provider}.

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

To use the databricks_{provider}, set the following environment variables:

DATABRICKS_ACCOUNT_ID - a uuid representing your Databricks account id, you can get this from the Databricks UI
DATABRICKS_CLIENT_ID - obtained after creating a service principal through the Databricks UI
DATABRICKS_CLIENT_SECRET - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function

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
    with open(provider_path / "index.md", "w") as f:
        f.write(doc_content)

def generate_fields_section(fields_df):
    """Generate the fields section of the documentation."""
    fields_content = """<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource', value: 'view', },
        { label: 'resource', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
"""
    
    for _, row in fields_df.iterrows():
        fields_content += f"| <CopyableCode code=\"{row['name']}\" /> | `{row['type'] or 'unknown'}` | {row.get('description', '')} |\n"
    
    fields_content += "</TabItem>\n</Tabs>\n\n"
    return fields_content

def generate_methods_section(methods_df):
    """Generate the methods section of the documentation."""
    methods_content = "## Methods\n| Name | Accessible by | Required Params | Description |\n|:-----|:--------------|:----------------|:------------|\n"
    
    for _, row in methods_df.iterrows():
        required_params = row['RequiredParams'] if pd.notna(row['RequiredParams']) else ''
        description = row['description'] if pd.notna(row['description']) else ''
        methods_content += f"| <CopyableCode code=\"{row['MethodName']}\" /> | `{row['SQLVerb']}` | <CopyableCode code=\"{required_params}\" /> | {description} |\n"
    
    return methods_content