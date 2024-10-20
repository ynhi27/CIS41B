# Y Nhi Tran
# Exercise Client

import socket
import pickle


class Client:
    def __init__(self, portnumber):
        self.port = portnumber
        self.s = socket.socket()
        self.host = socket.gethostname()

    def send_query(self, query):
        self.s.send(query.encode())

    def receive_dataframe(self):
        # Receive the data size
        size_data = b""
        while len(size_data) < 4:
            chunk = self.s.recv(4 - len(size_data))
            if not chunk:
                break
            size_data += chunk
        data_size = int.from_bytes(size_data, "big")

        # Receive the data
        data = b""
        while len(data) < data_size:
            chunk = self.s.recv(min(data_size - len(data), 4096))
            if not chunk:
                break
            data += chunk

        dataframe = pickle.loads(data)
        return dataframe

    def close(self):
        self.s.close()

    def __str__(self):
        return f"Client(port={self.port}, host={self.host})"

    def __repr__(self):
        return f"Client(port={self.port}, host={self.host})"

    def __enter__(self):
        self.s.connect((self.host, self.port))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


client = Client(5000)
with client:
    query = "SELECT * FROM CO2"
    client.send_query(query)

    dataframe = client.receive_dataframe()
    print(dataframe)
