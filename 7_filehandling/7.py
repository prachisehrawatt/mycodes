import sqlite3

with sqlite3.connect("library.db") as conn:
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER,
            title TEXT
        )
        """)
    books = [
        (1, "The Pragmatic Programmer"),
        (2, "Clean Code"),
        (3, "Fluent Python")
        ]

    cursor.executemany("INSERT INTO books VALUES (?, ?)", books)

    cursor.execute("SELECT * FROM books")

    for row in cursor.fetchall():
        print(row)

conn.commit()
conn.close()