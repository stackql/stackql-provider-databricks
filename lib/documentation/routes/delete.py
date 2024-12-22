import pandas as pd

def generate_delete_example(provider, service, resource, methods_df, fields_df):
    """Generate DELETE example documentation."""
    # Get all DELETE operations
    delete_methods = methods_df[methods_df['SQLVerb'] == 'DELETE'].copy()
    if delete_methods.empty:
        return ""
    
    # Add parameter count for sorting
    delete_methods['param_count'] = delete_methods['RequiredParams'].apply(
        lambda x: len(x.split(', ')) if pd.notna(x) else 0
    )
    # Sort by parameter count (least specific to most)
    delete_methods = delete_methods.sort_values('param_count')

    def create_delete_statement(method):
        """Creates a DELETE statement for the given method"""
        required_params = method['RequiredParams'].split(', ') if pd.notna(method['RequiredParams']) else []
        where_clause = []
        for param in required_params:
            template_param = param.replace('data__', '')
            where_clause.append(f"{param} = '{{{{ {template_param} }}}}'")
        where_str = ' AND\n'.join(where_clause)
        
        return f"""/*+ delete */
DELETE FROM {provider}.{service}.{resource}
WHERE {where_str};"""

    # If only one DELETE method, don't use tabs
    if len(delete_methods) == 1:
        method = delete_methods.iloc[0]
        content = f"""
## DELETE example

Deletes a <code>{resource}</code> resource.

```sql
{create_delete_statement(method)}
```
"""
    else:
        # For multiple DELETE methods, use tabs
        content = """
## DELETE example

Deletes a <code>%s</code> resource.

<Tabs
    defaultValue="%s"
    values={[
""" % (resource, delete_methods.iloc[0]['MethodName'])
    
        # Add tab definitions
        tab_values = []
        for _, method in delete_methods.iterrows():
            tab_values.append(
                f"""        {{ label: '{method["MethodName"]}', value: '{method["MethodName"]}' }}"""
            )
        
        content += ',\n'.join(tab_values)
        content += """
    ]
}>
"""
    
        # Add tab for each DELETE method
        for _, method in delete_methods.iterrows():
            content += f"""<TabItem value="{method['MethodName']}">

```sql
{create_delete_statement(method)}
```

</TabItem>
"""
    
        content += "</Tabs>\n"
    return content