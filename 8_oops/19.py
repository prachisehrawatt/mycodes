

class Car:
    def __init__(self, ubrand, umodel): 
        self.brand = ubrand
        self.model = umodel

    def car_name(self):     
        return f"Car {self.brand} , Model : {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel Fuel !"


class ElectricCar:
    def __init__(self, ubrand, umodel): 
        self.brand = ubrand
        self.model = umodel

    def car_name(self):     
        return f"Car {self.brand} , Model : {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel Fuel !"

e_car = ElectricCar('Tata', 'TiagoEV')
print(e_car.fuel_type())

nexon = Car('Tata', 'Nexon')
print(nexon.fuel_type())

is_child = isinstance(e_car, Car)
print(f"Is e_car an instance of Car? {is_child}")