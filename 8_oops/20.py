


# Class : Inheritance
# Class 1 --> make / model
# Class 2 --> electric car - battery_size

class Car:
    def __init__(self, ubrand, umodel): 
        self.brand = ubrand
        self.model = umodel

    def car_name(self):     
        return f"Car {self.brand} , Model : {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel Fuel !"


class ElectricCar(Car):
    def __init__(self, ubrand, umodel, battery_size):
        super().__init__(ubrand, umodel)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

e_car = ElectricCar('Tata', 'TiagoEV', '50kWh')
print(e_car.fuel_type())

nexon = Car('Tata', 'Nexon')
print(nexon.fuel_type())

is_parent = isinstance(ElectricCar, Car)
print(f"Is e_car an instance of Car? {is_parent}")

is_child = isinstance(Car, ElectricCar)
print(f"Is e_car an instance of Car? {is_child}")

is_child = isinstance(e_car, Car)
print(f"Is e_car an instance of Car? {is_child}")