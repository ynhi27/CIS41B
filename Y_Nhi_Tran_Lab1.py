# Y Nhi Tran
# Lab 1 - Databases


import pandas as pd
import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect('climate_data.db')
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS data
                                (year INT PRIMARY KEY,
                                co2 REAL,
                                sea_level REAL)''')
        self.db.commit()

    def insert_data(self, data):
        for i in range(len(data)):
            year = data.iloc[i]['year']
            co2 = data.iloc[i]['CO2']
            sea_level = data.iloc[i]['Sea_Level']
            if pd.isna(sea_level):
                sea_level = "0"
            self.cursor.execute(f"INSERT INTO data (year, co2, sea_level) VALUES ({year}, {co2}, {sea_level})")
        self.db.commit()

    def search_data(self, year):
        self.cursor.execute(f"SELECT * FROM data WHERE year={year}")
        result = self.cursor.fetchone()
        if result is not None:
            return {"year": result[0], "CO2": result[1], "Sea_Level": result[2]}
        else:
            return None

    def delete_data(self, year):
        self.cursor.execute(f"DELETE FROM data WHERE year={year}")
        self.db.commit()


# Read in Co2.html - ignore first 2 lines of the file
co2 = pd.read_html('Co2.html', header=2)[0]

# Read in SeaLevel.csv - ignore the lines have '#'
sea_level = pd.read_csv("SeaLevel.csv", comment='#', sep=',')
sea_level['year'] = sea_level['year'].apply(lambda x: int(x))
# print(co2)

# Calculate the average of the 'average' column for each year
co2_avg = co2.groupby(['year']).mean().reset_index()
co2_avg.rename(columns={'average': 'CO2'}, inplace=True)
co2_avg2 = co2_avg[["year", "CO2"]]
# print(co2_avg2)

# Calculate the average of the 'TOPEX' column for each year
sea_level_avg = sea_level.groupby(['year']).mean().reset_index()
sea_level_avg = sea_level_avg.fillna(0)
sea_level_avg.rename(columns={'TOPEX/Poseidon': 'Sea_Level'}, inplace=True)
sea_level_avg2 = sea_level_avg[["year", "Sea_Level"]]
# print(sea_level_avg2)

# Merge the two dataframes on the 'year' column
result = pd.merge(co2_avg2, sea_level_avg2, how='outer', on='year')

# Print out the result
print(result.to_string())

"""# Create a Database object
db = Database()

# Create the table
print("Create table successful!")
db.create_table()

# Insert the data
print("Insert table successful!")
db.insert_data(result)

# Search for data based on year
print("Search for data successful!")
res = db.search_data(2010)
print(res)

# Delete data based on year
print("Delete data successful!")
db.delete_data(2010)"""

"""
Output
Create table successful!
Insert table successful!
Search for data successful!
{'year': 2010, 'CO2': 389.89916666666664, 'Sea_Level': 26.86108108108108}
Delete data successful!
"""