import sqlite3

def getData():
    # this establishes a connection from our python file
    # to our Db file
    connect = sqlite3.connect("testDb_p2.db")

    # this variable lets us send and recieve data back and forth from
    # our file to our database
    cursor = connect.cursor()

    # the actual data we want to get from the database
    query1= "SELECT model FROM computers"
#    query2= "SELECT model FROM computers"

    #this is telling the program to fetch the query above
    cursor.execute(query)

    # storing the fetched data inside of results
    results = cursorfetchall()

    # printing out data
    print(results)

# getData()


def getSingleData():
    computerSearch = input("What computer model are you looking for?")
    
    connect = sqlite3.connect("testDb_p2.db")

    cursor = connect.cursor()

    query1= f"SELECT model FROM computers"
    #this is telling the program to fetch the query above
    cursor.execute(query1)

    # storing the fetched data inside of results
    results = cursor.fetchall()

    # printing out data
    print(results)

getSingleData()