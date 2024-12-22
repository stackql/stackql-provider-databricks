import os
from pathlib import Path
import pandas as pd

def generate_service_doc(provider, service, resources_df, providers_path):
    """Generate documentation for a service."""
    # Create directory structure
    service_path = Path(providers_path) / service
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
  - Databricks
  - {service}
  - {provider}
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/{provider}/stackql-databricks-provider-featured-image.png
---

__`{service}`__ service documentation.

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

Services from Databricks.

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

def check_view_exists(conn, provider, service, resource):
    """Check if a view exists for the given resource."""
    view_name = f"vw_{resource}"
    query = f"DESCRIBE EXTENDED {provider}.{service}.{view_name}"
    try:
        r = conn.execute(query)
        return True
    except Exception:
        return False

def get_view_fields(conn, provider, service, resource):
    """Get fields for the view if it exists."""
    view_name = f"vw_{resource}"
    query = f"DESCRIBE EXTENDED {provider}.{service}.{view_name}"
    try:
        r = conn.execute(query)
        data = r.fetchall()
        return pd.DataFrame([i.copy() for i in data])
    except Exception:
        return None

def generate_methods_section(methods_df):
    """Generate the methods section of the documentation."""
    methods_content = "## Methods\n| Name | Accessible by | Required Params | Description |\n|:-----|:--------------|:----------------|:------------|\n"
    
    for _, row in methods_df.iterrows():
        required_params = row['RequiredParams'] if pd.notna(row['RequiredParams']) else ''
        description = row['description'] if pd.notna(row['description']) else ''
        methods_content += f"| <CopyableCode code=\"{row['MethodName']}\" /> | `{row['SQLVerb']}` | <CopyableCode code=\"{required_params}\" /> | {description} |\n"
    
    return methods_content

def generate_fields_section(resource_fields_df, view_fields_df=None):
    """Generate the fields section of the documentation."""
    fields_content = "## Fields\n"
    
    if view_fields_df is not None:
        # Generate tabbed view with both resource and view fields
        fields_content += """<Tabs
    defaultValue="view"
    values={[
        { label: 'view', value: 'view', },
        { label: 'resource', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
"""
        # Add view fields
        for _, row in view_fields_df.iterrows():
            fields_content += f"| <CopyableCode code=\"{row['name']}\" /> | `{row['type'] or 'unknown'}` | {row.get('description', '')} |\n"
        
        fields_content += """</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
"""
        # Add resource fields
        for _, row in resource_fields_df.iterrows():
            fields_content += f"| <CopyableCode code=\"{row['name']}\" /> | `{row['type'] or 'unknown'}` | {row.get('description', '')} |\n"
        
        fields_content += "</TabItem>\n</Tabs>\n\n"
    else:
        # Generate simple table for resource fields only
        fields_content += """| Name | Datatype | Description |
|:-----|:---------|:------------|
"""
        for _, row in resource_fields_df.iterrows():
            fields_content += f"| <CopyableCode code=\"{row['name']}\" /> | `{row['type'] or 'unknown'}` | {row.get('description', '')} |\n"
        
        fields_content += "\n"
    
    return fields_content

def generate_resource_doc(provider, service, resource, methods_df, fields_df, providers_path, resources_df):
    """Generate documentation for a specific resource."""
    # Skip if this is a view
    if resource.startswith('vw_'):
        return
        
    # Check if a corresponding view exists by looking in resources_df
    view_name = f"vw_{resource}"
    has_view = view_name in resources_df['name'].values
    
    # Get view fields if the view exists
    view_fields = fields_df if has_view else None
    
    # Create directory structure
    resource_path = Path(providers_path) / service / resource
    resource_path.mkdir(parents=True, exist_ok=True)
    
    # Generate resource documentation
    doc_content = f"""---
title: {resource}
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - {resource}
  - {service}
  - {provider}
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/{provider}/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>{resource}</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>{resource}</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="{provider}.{service}.{resource}" /></td></tr>
</tbody></table>

"""
    # Add fields section
    if fields_df is not None and not fields_df.empty:
        doc_content += generate_fields_section(fields_df, view_fields)
    else:
        doc_content += """
`SELECT` not supported for this resource, see the methods section for supported operations.
"""
    
    # Add methods section
    if methods_df is not None and not methods_df.empty:
        doc_content += generate_methods_section(methods_df)
    
    # Write the documentation to file
    with open(resource_path / "index.md", "w") as f:
        f.write(doc_content)