import tkinter as tk
from tkinter import messagebox
import socket
import pickle
import matplotlib.pyplot as plt


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


def handle_state_selection():
    state = state_var.get()
    start_year = int(start_year_var.get())
    end_year = int(end_year_var.get())

    if state and start_year <= end_year:
        with Client(5000) as client:
            # Query for the yearly data of the chosen state within the selected year range
            query = f"SELECT {', '.join(['Year' + str(year) for year in range(start_year, end_year + 1)])} " \
                    f"FROM CO2 WHERE State = '{state}'"
            client.send_query(query)

            dataframe = client.receive_dataframe()

            # Plot the data
            years = range(start_year, end_year + 1)
            data = dataframe.iloc[0].tolist()
            plt.plot(years, data)
            plt.xlabel('Year')
            plt.ylabel('CO2 Emissions')
            plt.title(f'CO2 Emissions for {state} ({start_year}-{end_year})')
            plt.show()
    else:
        messagebox.showwarning("Invalid Selection", "Please select a state and a valid year range.")


root = tk.Tk()
root.title("State Selection")

state_var = tk.StringVar()
start_year_var = tk.StringVar()
end_year_var = tk.StringVar()

# Fetch the CO2 dataframe from the server
with Client(5000) as client:
    client.send_query("SELECT * FROM CO2")
    dataframe = client.receive_dataframe()

state_options = dataframe["State"].tolist()
state_var.set(state_options[0])

state_label = tk.Label(root, text="Select a state:")
state_label.pack()

state_dropdown = tk.OptionMenu(root, state_var, *state_options)
state_dropdown.pack()

start_year_label = tk.Label(root, text="Start Year:")
start_year_label.pack()

start_year_entry = tk.Entry(root, textvariable=start_year_var)
start_year_entry.pack()

end_year_label = tk.Label(root, text="End Year:")
end_year_label.pack()

end_year_entry = tk.Entry(root, textvariable=end_year_var)
end_year_entry.pack()

select_button = tk.Button(root, text="Select", command=handle_state_selection)
select_button.pack()

root.mainloop()
