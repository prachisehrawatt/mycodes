# Static Method
# Add a static method to the car class that returns a general description of a car.

class Car:
    
    create_class_count = 0
    class_call_count = 0 

    def __init__(self): 
        Car.create_class_count = Car.create_class_count + 1
        # obj of class is created this method gets called !
        
    def __call__(self):
        # when the obj of class is called then this method gets called !
        Car.class_call_count = Car.class_call_count + 1
        
obj1 = Car()    # Created instance of the class
obj2 = Car()    # Created instance of the class

obj1()          # Calling the instance of the class

print(f"The counter : {Car.create_class_count}")
print(f"The counter : {Car.class_call_count}")