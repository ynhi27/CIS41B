# Y Nhi Tran
# Lab 1 - Databases - v2

import pandas as pd
import sqlite3


class Database:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()

    def create_table(self, table_schema):
        self.cursor.execute(table_schema)
        self.db.commit()

    def insert_data(self, table_name, data):
        for i in range(len(data)):
            keys = ", ".join(data.columns)
            values = ", ".join([f"'{value}'" if pd.isna(value) else str(value) for value in data.iloc[i]])
            self.cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({values})")
        self.db.commit()

    def search_data(self, table_name, year):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE year={year}")
        result = self.cursor.fetchone()
        if result is not None:
            return result
        else:
            return None

    def delete_data(self, table_name, year):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE year={year}")
        self.db.commit()
        return self.cursor.rowcount > 0


# Read in Co2.html - ignore first 2 lines of the file
co2 = pd.read_html('Co2.html', header=2)[0]

# Read in SeaLevel.csv - ignore the lines that have '#'
sea_level = pd.read_csv("SeaLevel.csv", comment='#', sep=',')
sea_level['year'] = sea_level['year'].apply(lambda x: int(x))

# Calculate the average of the 'average' column for each year
co2_avg = co2.groupby(['year']).mean().reset_index()
co2_avg.rename(columns={'average': 'CO2'}, inplace=True)
co2_avg2 = co2_avg[["year", "CO2"]]

# Calculate the average of the 'TOPEX' column for each year
sea_level_avg = sea_level.groupby(['year']).mean().reset_index()
sea_level_avg = sea_level_avg.fillna(0)
sea_level_avg.rename(columns={'TOPEX/Poseidon': 'Sea_Level'}, inplace=True)
sea_level_avg2 = sea_level_avg[["year", "Sea_Level"]]

# Merge the two dataframes on the 'year' column
result = pd.merge(co2_avg2, sea_level_avg2, how='outer', on='year')

# Print out the result
print(result.to_string())

# Create an instance of the Database class
db = Database('data.db')

# Define the table schema
table_schema = '''CREATE TABLE IF NOT EXISTS data (
                    year INT PRIMARY KEY,
                    CO2 REAL,
                    Sea_Level REAL
                )'''

# Create the table in the database
db.create_table(table_schema)

# Insert the data into the database table
db.insert_data('data', result)

# Search for data in the database
search_year = 2019
search_result = db.search_data('data', search_year)
if search_result is not None:
    print(f"Data for year {search_year}: {search_result}")
else:
    print(f"No data found for year {search_year}")

# Delete data from the database
delete_year = 2018
if db.delete_data('data', delete_year):
    print(f"Data for year {delete_year} deleted.")
else:
    print(f"No data found for year {delete_year}. Deletion unsuccessful.")


""" OUTPUT
Data for year 2019: (2019, 411.41, 63.09242424242425)
Data for year 2018 deleted.
"""