import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS persons(
id INTEGER PRIMARY KEY,
name VARCHAR,
age INTEGER,
role VARCHAR,
detail VARCHAR,
salary INTEGER)
""")
conn.commit()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def save(self, role, detail, salary):
        cur.execute(
            "INSERT INTO persons(name,age,role,detail,salary) VALUES(?,?,?,?,?)",
            (self.name, self.__age, role, detail, salary),
        )
        conn.commit()


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def save(self):
        super().save("Student", "Grade " + str(self.grade), 0)


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def save(self):
        super().save("TEACHER", self.subject, self.salary)


class Staff(Person):
    def __init__(self, name, age, dept, salary):
        super().__init__(name, age)
        self.dept = dept
        self.salary = salary

    def save(self):
        super().save("STAFF", self.dept, self.salary)


while True:

    print("===== SCHOOL MANAGEMENT =====")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Staff")
    print("4. Show Records")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        s = Student(name, age, grade)
        s.save()
        print("student added !")

    elif ch == 2:
        name = input("Name: ")
        age = int(input("Age: "))
        sub = input("Subject: ")
        sal = float(input("Salary: "))
        t = Teacher(name,age, sub, sal)
        t.save()
        print("teacher added !")

    elif ch == 3:
        name = input("Name: ")
        age = int(input("Age: "))
        dep = input("Department: ")
        sal = float(input("Salary: "))
        st = Staff(name,age,dep,sal)
        st.save()
        print("staff added !")

    elif ch == 4:
        cur.execute("SELECT * FROM persons")
        rows = cur.fetchall()
        print("----Records----")
        for i in rows:
            print(i)

    elif ch == 5:
        print("thank you !")
        break

    else:
        print("invalid choice !")

conn.commit()
conn.close()
