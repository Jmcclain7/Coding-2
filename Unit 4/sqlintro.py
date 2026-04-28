# 1. import sqlite module to be able to use a database
import sqlite3

# 2. the connect method creates/starts our database
connection = sqlite3.connect()

# 3. this cursor variable create a new object that lets us send objects to our database
cursor = connect.cursor()

# 4.we need to create a schema (structure) for our data
cursor.excute('''
    CREATE TABLE computers(
    id INTEGER PRIMARY KEY,
    model TEXT,
    color TEXT,
    hasWebcam BOOL,
    memory INTEGER,
    price INTEGER,                                       
              )''')
cursor.excute('''
    INSERT INTO computers(model, color, hasWeb, memory, price)
    VALUES('apple m4', 'blue', True, 8, 1500)''')