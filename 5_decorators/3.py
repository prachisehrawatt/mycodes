class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is a dog")

obj = Dog('Ramu', 'Bull Dog') 

obj.bark()