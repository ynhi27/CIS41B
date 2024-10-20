# Y Nhi Tran
# Lab 3 - Threading

import threading
import sqlite3
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression


class WebScrape:
    def __init__(self, url):
        self.url = url

    def scrape_table_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
        tables = soup.find_all("table")
        table = tables[2]
        headers = [th.text.strip() for th in table.select("thead tr:not(:first-child) th")]
        rows = []
        for tr in table.find_all("tr"):
            row = [td.text.strip() for td in tr.find_all("td")]
            if row:
                rows.append(row)
        data = pd.DataFrame(rows, columns=headers)
        return data


class Database:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()

    def create_table(self, table_name, columns):
        column_names = []
        for col in columns:
            col_name = col.replace(".", "_")
            if col_name in column_names:
                suffix = 1
                while f"{col_name}_{suffix}" in column_names:
                    suffix += 1
                col_name = f"{col_name}_{suffix}"
            column_names.append(col_name)

        column_defs = [f'"{col}" REAL' for col in column_names]
        table_schema = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
        self.cursor.execute(table_schema)
        self.db.commit()

    def insert_data(self, table_name, data):
        for _, row in data.iterrows():
            placeholders = ", ".join(["?" for _ in data.columns])
            values = [value if pd.notna(value) else None for value in row]
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            self.cursor.execute(query, values)
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


class GasDataExtractor:
    def __init__(self, agent, db_name, gas_data):
        self.agent = agent
        self.db_name = db_name
        self.gas_data = gas_data

    def extract_yearly_data(self):
        # Create a new connection and cursor for each thread
        db = sqlite3.connect(self.db_name)
        cursor = db.cursor()

        with db_lock:
            for year in range(1990, 2020):
                cursor.execute(f"SELECT \"{self.agent}\" FROM {table_name} WHERE year=?", (year,))
                result = cursor.fetchone()
                if result is not None:
                    cell_data = result[0]
                    print(f"{self.agent} - Year: {year}, Data: {cell_data}")

                    if self.agent not in self.gas_data:
                        self.gas_data[self.agent] = {"year": [], "data": []}

                    self.gas_data[self.agent]["year"].append(year)
                    self.gas_data[self.agent]["data"].append(cell_data)
                else:
                    print(f"No data available for {self.agent} - Year: {year}")

        # Close the connection after processing
        cursor.close()
        db.close()


if __name__ == "__main__":
    # Define the URL
    url = "https://gml.noaa.gov/aggi/aggi.html"

    # Create an instance of the WebScrape class
    web_scrape = WebScrape(url)

    # Scrape the table data
    data = web_scrape.scrape_table_data()

    # Create an instance of the Database class
    db = Database("climate_data.db")

    # Define the table name and columns
    table_name = "climate_data"
    columns = data.columns

    # Create the table in the database
    db.create_table(table_name, columns)

    # Insert the data into the table
    db.insert_data(table_name, data)

    # Define the lock to ensure exclusive access to the database
    db_lock = threading.Lock()

    # Define the agents
    agents = ["CO2", "CH4", "N2O", "CFCs*", "HCFCs", "HFCs*"]

    # Create an empty dictionary to store gas data
    gas_data = {}

    # Start the threaded agents
    threads = []
    for agent in agents:
        thread = threading.Thread(target=GasDataExtractor(agent, "climate_data.db", gas_data).extract_yearly_data)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Plot linear regression for each gas
    plt.figure(figsize=(12, 8))
    scatter_plots = []
    for agent, data in gas_data.items():
        if len(data["data"]) > 1:
            x = np.array(data["year"], dtype=np.float64).reshape(-1, 1)
            y = np.array(data["data"], dtype=np.float64).reshape(-1, 1)

            # Perform linear regression
            model = LinearRegression()
            model.fit(x, y)
            y_pred = model.predict(x)

            # Create scatter plot for each gas
            scatter_plot = plt.scatter(x, y, label=agent)
            scatter_plots.append(scatter_plot)
            plt.plot(x, y_pred, color='red')

    plt.xlabel('Year')
    plt.ylabel('Gas Level')
    plt.title('Linear Regression for Gas Levels')
    plt.legend(handles=scatter_plots)
    plt.show()
