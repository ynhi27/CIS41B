# Y Nhi Tran
# Exercise Query

def QueryBuilder(Data_Base, Query_Type, Query_Tuple):
    ''' Build Query_String '''
    if Query_Type == "version":
        query_string = "SELECT sqlite_version()"
    elif Query_Type == "delete":
        query_string = "DELETE FROM {0} WHERE id = ?".format(Data_Base)
    elif Query_Type == "select":
        query_string = "SELECT * FROM {0} WHERE name = ?".format(Data_Base)
    elif Query_Type == "insert":
        query_string = "INSERT INTO {0} (id, name, photo, html) VALUES (?, ?, ?, ?)".format(Data_Base)
    elif Query_Type == "table":
        query_string = '''CREATE TABLE Database (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                photo text NOT NULL UNIQUE,
                                html text NOT NULL UNIQUE)'''.format(Data_Base)
    else:
        raise ValueError("Invalid query type")

    return query_string


# Construct a query to get the version of SQLite
query = QueryBuilder("Database", "version", ())
print(query)  # Output: SELECT sqlite_version()

# Construct a query to delete a row with id=1 from the Database table
query = QueryBuilder("Database", "delete", (1,))
print(query)  # Output: DELETE FROM Database WHERE id = ?

# Construct a query to select rows with name="John" from the Database table
query = QueryBuilder("Database", "select", ("John",))
print(query)  # Output: SELECT * FROM Database WHERE name = ?

# Construct a query to insert a new row into the Database table
query = QueryBuilder("Database", "insert", (1, "John", "photo.jpg", "<html></html>"))
print(query)  # Output: INSERT INTO Database (id, name, photo, html) VALUES (?, ?, ?, ?)

# Construct a query to create the Database table
query = QueryBuilder("Database", "table", ())
print(query)  # Output: CREATE TABLE Database (
               # id INTEGER PRIMARY KEY,
               # name TEXT NOT NULL,
               # photo TEXT NOT NULL UNIQUE,
               # html TEXT NOT NULL UNIQUE)"""
