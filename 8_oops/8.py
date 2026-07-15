'''Class - Human, 
method 1 : get_age : return age of person
method 2 : set_age : adds yrs as per users request.'''


class Human:
    def __init__(self, age):
        self.__age = age 

    def get_age(self):           # getter() - reads private data
        return self.__age

    def set_age(self,yrs):       # setter() - write / update / validate data
        self.__age += yrs
        return self.__age

person = Human(17)

print("your current age is", person.get_age())
person.set_age(5)
print("your new age is", person.get_age())
