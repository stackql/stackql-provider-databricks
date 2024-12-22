import os, yaml, re
from pathlib import Path
import pandas as pd







# def check_view_exists(conn, provider, service, resource):
#     """Check if a view exists for the given resource."""
#     view_name = f"vw_{resource}"
#     query = f"DESCRIBE EXTENDED {provider}.{service}.{view_name}"
#     try:
#         r = conn.execute(query)
#         return True
#     except Exception:
#         return False

# def get_view_fields(conn, provider, service, resource):
#     """Get fields for the view if it exists."""
#     view_name = f"vw_{resource}"
#     query = f"DESCRIBE EXTENDED {provider}.{service}.{view_name}"
#     try:
#         r = conn.execute(query)
#         data = r.fetchall()
#         return pd.DataFrame([i.copy() for i in data])
#     except Exception:
#         return None





















