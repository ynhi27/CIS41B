# Y Nhi Tran
# Exercise Query - v3

import sqlite3
import pandas as pd


def QueryBuilder(db_base, query_type, query_tuple):
    db = sqlite3.connect(db_base)
    cursor = db.cursor()

    if query_type == 'create_table':
        table_schema = query_tuple
        cursor.execute(table_schema)
        db.commit()
        return "Table created successfully."

    elif query_type == 'insert_data':
        table_name, data = query_tuple
        for i in range(len(data)):
            keys = ", ".join(data.columns)
            values = ", ".join([f"'{value}'" if pd.isna(value) else str(value) for value in data.iloc[i]])
            cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({values})")
        db.commit()
        return "Data inserted successfully."

    elif query_type == 'search_data':
        table_name, year = query_tuple
        cursor.execute(f"SELECT * FROM {table_name} WHERE year={year}")
        result = cursor.fetchone()
        if result is not None:
            return result
        else:
            return None

    elif query_type == 'delete_data':
        table_name, year = query_tuple
        cursor.execute(f"DELETE FROM {table_name} WHERE year={year}")
        db.commit()
        return cursor.rowcount > 0

    else:
        return "Invalid query type."
