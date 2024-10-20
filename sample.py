import cProfile
from Y_Nhi_Tran_ExerciseClient import Client


def profile_code():
    client = Client(5000)
    with client:
        query = "SELECT * FROM CO2"
        client.send_query(query)

        dataframe = client.receive_dataframe()
        print(dataframe)


# Run the code with profiling
cProfile.run("profile_code()")
