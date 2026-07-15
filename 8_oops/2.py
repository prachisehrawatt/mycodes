'''
Write a Python script : 
a. create a class that accepts - make, model, date_of_purchase
b. setup database connection to db - carsdb and store info into table - cars
c. Store object details in db
'''

import sqlite3
class Car:
    def __init__(self, make, model, date_of_purchase):
        self.make = make
        self.model = model
        self.date_of_purchase = date_of_purchase



car1 = Car("Hyundai", "Creta", "2025-05-07")
car2 = Car("Mercedes", "Maybach GLS","2025-05-07" )
conn = sqlite3.connect("carsdb.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cars(
    make TEXT,
    model TEXT,
    date_of_purchase TEXT
)
""")

cursor.execute(
    "INSERT INTO cars(make, model, date_of_purchase) VALUES(?, ?, ?)",
    (car1.make, car1.model, car1.date_of_purchase)
)
cursor.execute(
    "INSERT INTO cars VALUES(?, ?, ?)",
    (car2.make, car2.model, car2.date_of_purchase)

)

conn.commit()
print("car details stored successfully !")

cursor.close()
conn.close()