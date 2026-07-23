# In Class Car, make a attribute read only using a property of decorator

class Car:
    def __init__(self, ubrand, umodel): 
        self._brand = ubrand
        self.model = umodel
    
    @property
    def brand(self):
        return self._brand

    def car_name(self):     
        return f"Car {self.brand} , Model : {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel Fuel !"

nexon = Car('Tata', 'Nexon')
print(nexon.fuel_type())

print(nexon.brand)

try:
    nexon.brand = "Nexon 1"
except Exception as e:
    print(f"The error is {e}")

is_child = isinstance(nexon, Car)
print(f"Result : {is_child}")
nexon.brand = "ede"

print(nexon.brand())

# what kind of error will it throw when accessing brand variable