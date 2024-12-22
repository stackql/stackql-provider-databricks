from pathlib import Path

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