# Y Nhi Tran
# Exercise Query - v2

import sqlite3
import pandas as pd


def create_database(db_name):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    return db, cursor


def create_table(cursor, table_schema):
    cursor.execute(table_schema)


def insert_data(cursor, table_name, data):
    for i in range(len(data)):
        keys = ", ".join(data.columns)
        values = ", ".join([f"'{value}'" if pd.isna(value) else str(value) for value in data.iloc[i]])
        cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({values})")


def search_data(cursor, table_name, year):
    cursor.execute(f"SELECT * FROM {table_name} WHERE year={year}")
    result = cursor.fetchone()
    if result is not None:
        return result
    else:
        return None


def delete_data(cursor, table_name, year):
    cursor.execute(f"DELETE FROM {table_name} WHERE year={year}")
    return cursor.rowcount > 0
