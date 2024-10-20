import functools
from typing import Tuple, Callable

# Define function types for different query types
QueryFunction = Callable[[str, Tuple[str, str, str]], str]

# Function to handle the "version" query type
def handle_version_query(data_base: str, query_tuple: Tuple[str, str, str]) -> str:
    return "SELECT version();"

# Function to handle the "delete" query type
def handle_delete_query(data_base: str, query_tuple: Tuple[str, str, str]) -> str:
    table_name, condition = query_tuple
    return f"DELETE FROM {table_name} WHERE {condition};"

# Function to handle the "select" query type
def handle_select_query(data_base: str, query_tuple: Tuple[str, str, str]) -> str:
    table_name, columns, condition = query_tuple
    return f"SELECT {columns} FROM {table_name} WHERE {condition};"

# Function to handle the "insert" query type
def handle_insert_query(data_base: str, query_tuple: Tuple[str, str, str]) -> str:
    table_name, columns, values = query_tuple
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"

# Function to handle the "update" query type
def handle_update_query(data_base: str, query_tuple: Tuple[str, str, str]) -> str:
    table_name, set_values, condition = query_tuple
    return f"UPDATE {table_name} SET {set_values} WHERE {condition};"

# Function to build the query string using the provided query type and tuple
def query_builder(data_base: str, query_type: str, query_tuple: Tuple[str, str, str]) -> str:
    # Create a dictionary of query type strings to corresponding functions
    query_functions = {
        "version": handle_version_query,
        "delete": handle_delete_query,
        "select": handle_select_query,
        "insert": handle_insert_query,
        "update": handle_update_query
    }

    # Find the appropriate function based on the query type
    query_function = query_functions.get(query_type)
    if query_function:
        # Call the function and return the result
        return query_function(data_base, query_tuple)
    else:
        return "Invalid query type."

data_base = "my_database"
query_type = "select"
query_tuple = ("my_table", "*", "id = 1")

query_string = query_builder(data_base, query_type, query_tuple)
print("Query string:", query_string)
