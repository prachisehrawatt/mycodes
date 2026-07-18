class Car:
    def __init__(self, ubrand, umodel): # declaration of variables
        self.__brand = ubrand       # private variable
        self.__model = umodel       # Private variable

    def get_model(self):
        return self.__model + " !"
    
    def fuel_type(self):
        return "Petrol/Diesel fuel"
    

    def car_name(self):     # function is called as method in python/coding lang
        return f"Car {self.__brand} , Model : {self.__model}"

class ElectricCar(Car):
    def __init__(self, ubrand, umodel, battery_size):
        super().__init__(ubrand, umodel)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

e_car = ElectricCar('Tata', 'TiagoEV' ,'50kWh')
print(e_car.fuel_type())

nexon = Car('Tata', 'Nexon')
print(nexon.fuel_type())

