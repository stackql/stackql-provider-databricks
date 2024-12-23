import pandas as pd

def generate_select_example(provider, service, resource, methods_df, fields_df, has_view=False):
    """Generate SELECT example documentation."""
    # Get all SELECT operations
    select_methods = methods_df[methods_df['SQLVerb'] == 'SELECT'].copy()
    if select_methods.empty:
        return ""
    
    # Add parameter count for sorting
    select_methods['param_count'] = select_methods['RequiredParams'].apply(
        lambda x: len(x.split(', ')) if pd.notna(x) else 0
    )
    # Sort by parameter count
    select_methods = select_methods.sort_values('param_count')
    
    # Generate field list (same for all SELECT operations)
    fields = []
    for _, row in fields_df.iterrows():
        fields.append(row['name'])
    field_list = ',\n'.join(fields)
    
    def create_query(resource_name, required_params):
        """Creates a SELECT query with the given params"""
        query = f"""SELECT
{field_list}
FROM {provider}.{service}.{resource_name}"""
        if required_params:
            where_clause = []
            for param in required_params:
                template_param = param.replace('data__', '')
                where_clause.append(f"{param} = '{{{{ {template_param} }}}}'")
            query += f"\nWHERE {' AND\n'.join(where_clause)}"
        query += ";"
        return query

    # If only one SELECT method and no view, don't use tabs
    if len(select_methods) == 1 and not has_view:
        method = select_methods.iloc[0]
        required_params = method['RequiredParams'].split(', ') if pd.notna(method['RequiredParams']) else []
        return f"""
## `SELECT` examples

```sql
{create_query(resource, required_params)}
```
"""
    
    # For multiple methods or when view exists, use tabs
    content = """
## `SELECT` examples

<Tabs
    defaultValue="%s"
    values={[
""" % ("view" if has_view else select_methods.iloc[0]['MethodName'])

    # Add tab definitions
    tab_values = []
    if has_view:
        tab_values.append(f"""        {{ label: 'vw_{resource}', value: 'view' }}""")
    
    for _, method in select_methods.iterrows():
        tab_values.append(
            f"""        {{ label: '{resource} ({method["MethodName"]})', value: '{method["MethodName"]}' }}"""
        )
    
    content += ',\n'.join(tab_values)
    content += """
    ]
}>
"""
    
    # Add view tab if exists
    if has_view:
        content += f"""<TabItem value="view">

```sql
{create_query(f"vw_{resource}", [])}
```

</TabItem>
"""
    
    # Add tab for each SELECT method
    for _, method in select_methods.iterrows():
        required_params = method['RequiredParams'].split(', ') if pd.notna(method['RequiredParams']) else []
        content += f"""<TabItem value="{method['MethodName']}">

```sql
{create_query(resource, required_params)}
```

</TabItem>
"""
    
    content += "</Tabs>\n"
    return content