import sqlite3

class Product: #main
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Product):
    def __init__(self, title, price, weight):
        super().__init__(title, price)
        self.weight = weight

    def save_to_db(self, conn):
        conn.execute(
            "INSERT INTO products VALUES(NULL,?,?,?,?,?)",
            ("Book", self.title, self.price, self.weight, None)
        )

class Software(Product):
    def __init__(self, title, price, file_size):
        super().__init__(title, price)
        self.file_size = file_size

    def save_to_db(self, conn):
        conn.execute(
            "INSERT INTO products VALUES(NULL,?,?,?,?,?)",
            ("Software", self.title, self.price, None, self.file_size)
        )

def get_all_products(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")

    for row in cur.fetchall():
        if row[1] == "Book":
            p = Book(row[2], row[3], row[4])
        else:
            p = Software(row[2], row[3], row[5])

        print(type(p).__name__, p.__dict__)



conn = sqlite3.connect("inventory.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY,
product_type TEXT,
title TEXT,
price REAL,
weight REAL,
file_size REAL)
""")

b = Book("Python", 500, 0.8)
s = Software("Photoshop", 2500, 3500)

b.save_to_db(conn)
s.save_to_db(conn)

conn.commit()
get_all_products(conn)
conn.close()