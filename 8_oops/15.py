'''Task 1 — Animal Sound Recorder Create a base class Animal with a method speak() that returns "...".

Create Dog, Cat, and Cow classes that inherit from Animal and override speak() to return their sound
Loop through a list containing all 3 objects and call save() on each using a single loop — this is the polymorphism in action
Print all records from the DB at the end'''

import sqlite3

conn = sqlite3.connect("animals.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS animal_sounds (
    id INTEGER PRIMARY KEY,
    animal Char,
    sound Char
)
""")

class Animal:
    def speak(self):
        return "..."

    def save(self):
        cursor.execute(
            "INSERT INTO animal_sounds (animal, sound) VALUES (?, ?)",
            (self.__class__.__self__, self.speak())
        )
        conn.commit()


class Dog(Animal):
    def speak(self):
        return "bhau bhau"


class Cat(Animal):
    def speak(self):
        return "meow"


class Cow(Animal):
    def speak(self):
        return "moo"

dog = Dog("tom !")
cat = Cat("kitty !")
cow = Cow("")
print("records saved successfully !")

cursor.execute("SELECT * FROM animal_sounds")
records = cursor.fetchall()

for i in records:
    print(i)

conn.commit()
conn.close()