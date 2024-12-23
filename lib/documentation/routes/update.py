import pandas as pd

def generate_update_example(provider, service, resource, methods_df, fields_df):
    """Generate UPDATE example documentation."""
    # Get all UPDATE operations
    update_methods = methods_df[methods_df['SQLVerb'] == 'UPDATE'].copy()
    if update_methods.empty:
        return ""
    
    # Add parameter count for sorting
    update_methods['param_count'] = update_methods['RequiredParams'].apply(
        lambda x: len(x.split(', ')) if pd.notna(x) else 0
    )
    # Sort by parameter count (least specific to most)
    update_methods = update_methods.sort_values('param_count')

    def create_update_statement(method):
        """Creates an UPDATE statement for the given method"""
        required_params = method['RequiredParams'].split(', ') if pd.notna(method['RequiredParams']) else []
        where_clause = []
        for param in required_params:
            template_param = param.replace('data__', '')
            where_clause.append(f"{param} = '{{{{ {template_param} }}}}'")
        where_str = ' AND\n'.join(where_clause)
        
        return f"""/*+ update */
UPDATE {provider}.{service}.{resource}
SET {{ field = value }}
WHERE {where_str};"""

    # If only one UPDATE method, don't use tabs
    if len(update_methods) == 1:
        method = update_methods.iloc[0]
        content = f"""
## `UPDATE` example

Updates a <code>{resource}</code> resource.

```sql
{create_update_statement(method)}
```
"""
    else:
        # For multiple UPDATE methods, use tabs
        content = """
## `UPDATE` example

Updates a <code>%s</code> resource.

<Tabs
    defaultValue="%s"
    values={[
""" % (resource, update_methods.iloc[0]['MethodName'])
    
        # Add tab definitions
        tab_values = []
        for _, method in update_methods.iterrows():
            tab_values.append(
                """        { label: '%s', value: '%s' }""" % (method["MethodName"], method["MethodName"])
            )
        
        content += ',\n'.join(tab_values)
        content += """
    ]
}>
"""

        # Add tab for each UPDATE method
        for _, method in update_methods.iterrows():
            content += f"""<TabItem value="{method['MethodName']}">
```sql
{create_update_statement(method)}
```
</TabItem>
"""
    
        content += "</Tabs>\n"
    return content