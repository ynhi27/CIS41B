# CIS41B

These are all exercises, assignments, and small projects that I had done for CIS 41B course at De ANza College.

### Exercise WebScraping
Write a Python script to scrape this website:

[https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita](https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita)

Scrape the "Production-based emissions: annual carbon dioxide emissions in metric tons per capita" for the data.  Use the functionality of Beautifulsoup to scrape the data.  Scrape the columns:  "Country Name","1980","2018".  Store the scraped data in a defaultdict.

### Lab 0 - Data Acquisition
Convert your script from Exercise Webscraping into a Python Class.  The Web scraping class encapsulates all the webscraping functions in the WebscrapingV3.py example file, except for the File and Image scraping functions.  Add appropriate dunders.  Review this website for creating and using class dunders:

[https://www.geeksforgeeks.org/customize-your-python-class-with-magic-or-dunder-methods/?ref=lbp](https://www.geeksforgeeks.org/customize-your-python-class-with-magic-or-dunder-methods/?ref=lbp)
If it's been a while since you programmed a Python Class, here is a video review on creating and using classes:

[https://realpython.com/lessons/classes-python/](https://realpython.com/lessons/classes-python/)

### Exercise Dunder
To your code for Lab0, convert 3 of your functions to Dunders.  Pick Dunders of your choice and note whether the Lab0 function you are replacing is binary or unary.  An example of a unary Dunder is the __len__ and __add__ is binary.  Click this link to get a Dunder list and more info about using Dunders:

[https://www.geeksforgeeks.org/customize-your-python-class-with-magic-or-dunder-methods/?ref=rp](https://www.geeksforgeeks.org/customize-your-python-class-with-magic-or-dunder-methods/?ref=rp)

Then demonstrate your Dunders are used.

### Exercise RegEx
Scrape, using Regex, all the <li> data on the local webpage 'Index.html' in the Webscraping Module on Canvas. Read the file as plain text.

### Exercise Query
  The Sqlite.py file contains several very specific queries:

        select_Query = "select sqlite_version()"
        delete_query = "DELETE from Database where id = "+str(id)
        sel = 'SELECT id FROM Database WHERE name == "{0}"'.format(value)
        insert_query = """INSERT INTO Database (id, name, photo, html) VALUES (?, ?, ?, ?)"""
        sqlite_select_query = """SELECT * from Database"""
        table_query = '''CREATE TABLE Database (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                photo text NOT NULL UNIQUE,
                                html text NOT NULL UNIQUE)'''
                                
  Write a QueryBuilder function.  The QueryBuilder builds a generic Query to build ANY Query type (i.e. version, delete, select, insert, select, table).  The QueryBuilder parameters require:  The type of Query, the input tuple data and then constructs a query string based on the parameters.

        def QueryBuilder( Data_Base, Query_Type, Query_Tuple):
            '''
            ''' Build Query_String
            '''
            ''' return Query_String

### Lab1 - Databases

Purpose:  Create and use a Database

Data Files:  Use BS4, Regular Expressions or Pandas to read in the two data files for this assignment:

Co2.html:
<TBODY><TR><TD>2002</TD><TD>4</TD><TD>2002.292</TD>...
<TBODY><TR><TD>2002</TD><TD>5</TD><TD>2002.375</TD>...
<TBODY><TR><TD>2002</TD><TD>6</TD><TD>2002.458</TD>...
...
SeaLevel.csv
2002.3797,3.43000,1.23000,,
2002.4069,1.13000,0.33000,,
2002.4340,-5.67000,-2.17000,,
...

Where necessary, reduce the data from either Monthly or Daily to Annual data.  Use Python iterators and reducers to handle converting the data to Annual data. Store the data in a Pandas Dataframe.


Database:

Store the Dataframe in an SQLite data base.  Design a class to interface to the SQLite database:

    class Database:
        def __init__(self):
            self.db = sqliteConnection()

            ...

and add functionality for table creation, inserting, searching and deleting entries in the database.  Use your QueryBuilder to build the SQLite database queries.

### Exercise Matplotlib
Using the output from Lab1, selelect a MatPlotLib plot type (chart, graph, bar, pie) to display the CO2 and Sealevel data.  Display the data in ONE plot/graph instead of two.

### Exercise TkInter
Write a TKinter example that I could use in class.  Your example should include interaction with two or more GUI controls.  Generate your own example instead of copying the multiple examples on the internet. The best examples will receive double points.

### Exercise Recursion
Write a recursive function that prints all of the files on a filelist returned from the fileList() function.

### Exercise Client
Design a Client class that interfaces with your SQLDatabase Server (from the Exercise Server).  The Client sends a SQLQuery to the SQLDatabase and receives a Dataframe from the SQLDatabase.  Your class should contain the default __dunders__ and potentially introduce some custom __dunders__.

### Exercise Server
Design a Server Class that provides access to a SQLDatabase.  The clients of your SQLDatabase server, send an SQLQuery to the SQLDatabase.  The SQLDatabase processes the SQLQuery and returns the Data from the Query in a DataFrame.  Your class should implement the default __dunders__ and potentially create some custom __dunders__.

### Lab 2 - Sockets
Process: 
The user (client) requests data from the (server) database.  The database sends back the data to the user.  At acquisition of the data an XYPlot is drawn.

DataFile: 
USAStatesCo2.csv

User Layer:
The user selects a country, and passes the country name to the Business Layer.  Use TKinter to produce a UI for the user to select a country. Send the selected country to the Business Layer.

Business Layer:
Receives the information from the User Layer and constructs a SQL query to send to the Data Layer.  The query extracts the yearly data (1970,2020) for the requested country.  The data may be queried either country year-by-year or in one query for year range.  After receiving the JSON string back from the Data Layer, send the data to the Graphic Layer for plotting.

Data Layer:
Construct a SQL Database based on the data from the DataFile.  Processes the queries from the Business Layer.   Sends back a JSON string for the requested query.  

Graphic Layer:
Create a graphics class to plot the MatPlotLib XYPlot.

Server Layer: (use exercise server)
The database access is controlled by the Server Socket.  The client sends a query, and the server sends a JSON string.

Client Socket: (use exercise client)
Requests data from the server.  After receiving the data from the server, the client displays the data.

### Exercise Miscellaneous 1 - Unit Test

### Exercise Miscellaneous 2 - Profiling

### Exercise Miscellaneous 3 - TimeDate

### Exercise Parallelism
Modify this threading example to use, exclusively, multiprocessing, instead of threading.

import threading
import time
 
class BankAccount():
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
 
  def __str__(self):
    return self.name
#These accounts are our shared resources
account1 = BankAccount("account1", 100)
account2 = BankAccount("account2", 0)
 
class BankTransferThread(threading.Thread):
  def __init__(self, sender, receiver, amount):
    threading.Thread.__init__(self)
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
   
  def run(self):
    sender_initial_balance = self.sender.balance
    sender_initial_balance -= self.amount
    # Inserting delay to allow switch between threads
    time.sleep(0.001)
    self.sender.balance = sender_initial_balance
     
    receiver_initial_balance = self.receiver.balance
    receiver_initial_balance += self.amount
    # Inserting delay to allow switch between threads
    time.sleep(0.001)
    self.receiver.balance = receiver_initial_balance
 
if __name__ == "__main__":
   
  threads = []
 
  for i in range(100):
    threads.append(BankTransferThread(account1, account2, 1))
 
  for thread in threads:
    thread.start()
 
  for thread in threads:
    thread.join()
 
  print(account1.balance)
  print(account2.balance)

### Exercice AI
See ExerciseAI.zip for instructions.  Use as many advanced python techniques as you can for full credit.  

Post lab instructions:  Most successful solutions followed the guidelines and processed the file up to 8 times.  This is ok IF the file is short, but what if the file is long (like 1,000,000 lines).  Devise a system that only processes a small part of the file instead of the complete file to find the encryption rotation.  Successful solutions will receive 10 bonus points.

Note:  if you already devised a system that uses a different technique (other than processing the complete file) repost your solution to this assignment.  Also, if you do something arbitrary like only process a certain percentage of the file, provide the mathmatical reasoning that this percentage is not arbitrary.  For example:  only process 1% of the file as statistically %1 will lead to fewer false positives ... prove this assertion.

### Lab 3 - Threading




