import sqlite3

books = [

    (1,"The Alchemist"),
    (2,"Harry Potter and the Philosopher's Stone"),
    (3,"To Kill a Mockingbird"),
    (4,"The Great Gatsby")
]
with sqlite3.connect("book.db") as myconn:
    cursor = myconn.cursor()

    cursor.execute('''
        CREATE TABLE book1(
            id INTEGER,
            name TEXT
        )
    ''')


    for id,name in books:
        cursor.execute(" INSERT INTO books VALUES (?,?)" , (id,name))

    myconn.commit()
    myconn.close() 