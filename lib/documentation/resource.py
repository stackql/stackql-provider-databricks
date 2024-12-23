from pathlib import Path
import sys
import pandas as pd

from lib.documentation.routes.delete import generate_delete_example
from lib.documentation.routes.insert import generate_insert_example
from lib.documentation.routes.replace import generate_replace_example
from lib.documentation.routes.select import generate_select_example
from lib.documentation.routes.update import generate_update_example

spec_root_path = ".stackql"

#
# main routine
#

def generate_resource_doc(provider, service, resource, methods_df, fields_df, providers_path, resources_df,conn):
    """Generate documentation for a specific resource."""
    # Skip if this is a view
    if resource.startswith('vw_'):
        return
        
    # Check if a corresponding view exists by looking in resources_df
    has_view = f"vw_{resource}" in resources_df['name'].values
    view_name = f"vw_{resource}" if has_view else None
    
    # Get view fields if the view exists
    view_fields = None
    if has_view:
        view_desc_query = f"DESCRIBE EXTENDED {provider}.{service}.{view_name}"
        try:
            r = conn.execute(view_desc_query)
            data = r.fetchall()
            view_fields = pd.DataFrame([i.copy() for i in data])
        except Exception as e:
            print(f"ERROR [failed to get fields for view {view_name}: {str(e)}]")
            sys.exit(1)
    
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
        doc_content += generate_fields_section(resource, fields_df, view_name, view_fields)
    else:
        doc_content += """
`SELECT` not supported for this resource, see the methods section for supported operations.
"""
    # Add methods section
    if methods_df is not None and not methods_df.empty:
        doc_content += generate_methods_section(methods_df)
        doc_content += generate_select_example(provider, service, resource, methods_df, fields_df, has_view, view_fields)
        doc_content += generate_insert_example(provider, service, resource, methods_df, fields_df, spec_root_path)
        doc_content += generate_update_example(provider, service, resource, methods_df, fields_df)
        doc_content += generate_replace_example(provider, service, resource, methods_df, fields_df)
        doc_content += generate_delete_example(provider, service, resource, methods_df, fields_df)
    else:
        # must be a view
        doc_content += generate_select_example(provider, service, resource, methods_df, fields_df)
        
    
    # Write the documentation to file
    with open(resource_path / "index.md", "w") as f:
        f.write(doc_content)

#
# methods section
#

def generate_methods_section(methods_df):
    """Generate the methods section of the documentation."""
    methods_content = "## Methods\n| Name | Accessible by | Required Params | Description |\n|:-----|:--------------|:----------------|:------------|\n"
    
    for _, row in methods_df.iterrows():
        required_params = row['RequiredParams'] if pd.notna(row['RequiredParams']) else ''
        description = row['description'] if pd.notna(row['description']) else ''
        methods_content += f"| <CopyableCode code=\"{row['MethodName']}\" /> | `{row['SQLVerb']}` | <CopyableCode code=\"{required_params}\" /> | {description} |\n"
    
    return methods_content        

#
# fields section
#

def generate_fields_section(resource_name, resource_fields_df, view_name=None, view_fields_df=None):
    """Generate the fields section of the documentation."""
    fields_content = "## Fields\n"
    
    # Check if descriptions exist in either dataframe
    resource_has_descriptions = not resource_fields_df['description'].isna().all() and not (resource_fields_df['description'] == '').all()
    view_has_descriptions = view_fields_df is not None and not view_fields_df['description'].isna().all() and not (view_fields_df['description'] == '').all()
    
    def generate_table_header(has_description):
        if has_description:
            return """| Name | Datatype | Description |
|:-----|:---------|:------------|
"""
        return """| Name | Datatype |
|:-----|:---------|
"""
    
    def generate_field_row(row, has_description):
        if has_description:
            return f"| <CopyableCode code=\"{row['name']}\" /> | `{row['type'] or 'unknown'}` | {row.get('description', '')} |\n"
        return f"| <CopyableCode code=\"{row['name']}\" /> | `{row['type'] or 'unknown'}` |\n"
    
    if view_fields_df is not None:
        # Generate tabbed view with both resource and view fields
        fields_content += """<Tabs
    defaultValue="view"
    values={[
        { label: '%s', value: 'view', },
        { label: '%s', value: 'resource', },
    ]
}>
<TabItem value="view">

%s""" % (view_name, resource_name, generate_table_header(view_has_descriptions))
        
        # Add view fields
        for _, row in view_fields_df.iterrows():
            fields_content += generate_field_row(row, view_has_descriptions)
        
        fields_content += """</TabItem>
<TabItem value="resource">

%s""" % generate_table_header(resource_has_descriptions)
        
        # Add resource fields
        for _, row in resource_fields_df.iterrows():
            fields_content += generate_field_row(row, resource_has_descriptions)
        
        fields_content += "</TabItem>\n</Tabs>\n\n"
    else:
        # Generate simple table for resource fields only
        fields_content += generate_table_header(resource_has_descriptions)
        for _, row in resource_fields_df.iterrows():
            fields_content += generate_field_row(row, resource_has_descriptions)
        
        fields_content += "\n"
    
    return fields_content