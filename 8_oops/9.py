'''Task 1 — Student Record Manager
Create a Student class with name and grade attributes.

Store student data in a SQLite database called school.db
Write a save() method that inserts the student into the database
Write a class method show_all() that prints all students from the database
Create 3 student objects and save them, then display all records'''


import sqlite3
conn = sqlite3.connect("school.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students(name VARCHAR, grade VARCHAR)")

class Student:

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def save(self):
        cur.execute("INSERT INTO students VALUES(?, ?)", (self.name, self.grade))
        conn.commit()

    def show_all(self):
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()

        print("----STUDENT RECORDS----")
        for i in data:
            print(i)


stu_1 = Student("Prachi", "A")
stu_2 = Student("Anjali", "A+")
stu_3 = Student("Dhruv", "B")


stu_1.save()
stu_2.save()
stu_3.save()

stu_1.show_all()

conn.commit()
conn.close()