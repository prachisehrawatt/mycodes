'''Task 2 — Library Book Tracker
Create a Book class with title, author, and __available (private, default True).

Store book data in library.db
Write a checkout() method — if available, set __available to False
Write a save() method that stores the book with its availability status
Write a class method show_available() that queries and prints only available books
Create 3 books, check out one, save all, then show only available books'''



import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS books(title VARCHAR, author VARCHAR, available VARCHAR)")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True

    def checkout(self):
        self.__available = False

    def save(self):
        cur.execute("INSERT INTO books VALUES(?,?,?)", (self.title, self.author, self.__available))
        conn.commit()

    def show_available(self):
        cur.execute("SELECT * FROM books WHERE available=True")
        for i in cur.fetchall():
            print(i)


b1 = Book("The Fault in Our Stars", "John Green")
b2 = Book("Pride and Prejudice", "Jane Austen")
b3 = Book("Me Before You", "Jojo Moyes")

b1.checkout()
b2.checkout()
b1.save()
b2.save()
b3.save()
b3.show_available()

conn.commit()
conn.close()