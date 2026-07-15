import sqlite3
class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def save(self, cur):
        cur.execute(
            "INSERT INTO employees VALUES(?,?,?)",
            (self.emp_id, self.name, self.salary)
        )

class Manager(Employee):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name, salary)
        self.bonus = bonus

    def save(self, cur):
        super().save(cur)
        cur.execute(
            "INSERT INTO managers VALUES(?,?)",
            (self.emp_id, self.bonus)
        )