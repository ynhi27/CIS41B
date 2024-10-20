# Y Nhi Tran
# Exercise Miscellaneous 1 - Unit Test

import unittest
import threading
import time
import socket
import pandas as pd
import sqlite3
import pickle


class Server:
    def __init__(self, portnumber):
        self.port = portnumber
        self.s = socket.socket()
        self.host = socket.gethostname()
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        print('Server listening....')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def serve(self):
        while True:
            conn, addr = self.s.accept()
            print('Got connection from', addr)
            query = conn.recv(1024).decode()
            print('Server received query:', query)

            # Process the SQL query and retrieve data
            data = self.process_query(query)

            # Pickle the data
            pickled_data = pickle.dumps(data)

            # Send the data size first
            data_size = len(pickled_data).to_bytes(4, byteorder='big')
            conn.sendall(data_size)

            # Send the pickled data back to the client
            conn.sendall(pickled_data)
            print('Sent data:', data)

            conn.close()

    def process_query(self, query):
        # Connect to the SQLDatabase and execute the query
        connection = sqlite3.connect('data.db')
        data = pd.read_sql_query(query, connection)
        connection.close()
        return data

    def close(self):
        self.s.close()


class Database:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()

    def create_table(self, table_name, columns):
        column_defs = [f"{col.replace('.', '_')} REAL" for col in columns]
        table_schema = f"CREATE TABLE IF NOT EXISTS {table_name} (State TEXT, {', '.join(column_defs)})"
        self.cursor.execute(table_schema)
        self.db.commit()

    def insert_data(self, table_name, data):
        for i in range(len(data)):
            keys = ", ".join([f'"{col}"' if col.isdigit() else col.replace(".", "_") for col in data.columns])
            placeholders = ", ".join(["?" for _ in data.columns])
            values = [value if pd.notna(value) else None for value in data.iloc[i]]
            self.cursor.execute(f'INSERT INTO {table_name} ({keys}) VALUES ({placeholders})', values)
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


# Create a test case class
class ServerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server in a separate thread
        cls.server_thread = threading.Thread(target=Server(5000).serve)
        cls.server_thread.start()
        # Wait for the server to start listening
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Stop the server by closing the socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((socket.gethostname(), 5000))
            sock.close()
        # Wait for the server thread to join
        cls.server_thread.join()

    def test_query(self):
        # Create a socket and connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((socket.gethostname(), 5000))
            # Send a query
            query = "SELECT * FROM CO2"
            sock.sendall(query.encode())
            # Receive the data size
            data_size_bytes = sock.recv(4)
            data_size = int.from_bytes(data_size_bytes, byteorder='big')
            # Receive the pickled data
            received_data = b""
            while len(received_data) < data_size:
                received_data += sock.recv(1024)
            # Unpickle the data
            unpickled_data = pickle.loads(received_data)
            # Assert that the received data is not None
            self.assertIsNotNone(unpickled_data)
            # Assert that the received data is of type pandas DataFrame
            self.assertIsInstance(unpickled_data, pd.DataFrame)


# Create an instance of the Database class
db = Database("data.db")

# Read in USAStatesCO2.csv with modified column names
CO2 = pd.read_csv("USAStatesCO2.csv", comment='#', sep=',', encoding='latin1',
                  skiprows=4, skipfooter=7, engine='python')
column_mapping = {str(year): f"Year{year}" for year in range(1970, 2021)}
CO2.rename(columns=column_mapping, inplace=True)

# Define the table schema
columns = CO2.columns[1:].tolist()  # Exclude the "State" column
table_schema = "CO2"
db.create_table(table_schema, columns)

# Insert the CO2 data into the database
db.insert_data("CO2", CO2)


# Run the unit tests and display the results
if __name__ == '__main__':
    # Run the unit tests
    test_suite = unittest.TestLoader().loadTestsFromTestCase(ServerTestCase)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    # Display the test results
    if test_result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed!")
