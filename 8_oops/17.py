class Car:
    def __init__(self, brand, model):
        self._brand = brand
        self.model = model

    @property
    def brand(self):
        return self._brand

c = Car("Mercedes", "GLS")
print("Brand:", c.brand)
c.brand = "Toyota"