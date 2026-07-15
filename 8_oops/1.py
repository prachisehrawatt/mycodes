class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


    def car(self):
        print(self.brand, self.model)

obj = Car("Suzuki", "Maruti 800")
obj.car()

obj1 = Car("Tata", "Tiago")
obj1.car()