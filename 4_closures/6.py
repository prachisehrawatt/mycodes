# CHALLENGE 1

def make_greeting(language):

    def greet(name):
        if language == "English":
            print("Hello", name)
        elif language == "Spanish":
            print("Hola", name)

    return greet


english = make_greeting("English")
spanish = make_greeting("Spanish")

english("Prachi")
spanish("Niket")


# CHALLENGE 2

def converter(x):

    def convert(temp):
        if x == "C":
            return (temp-32) * 5/9   
        elif x == "F":
            return (temp*9/5) + 32    

    return convert


cels = converter("C")
fahr = converter("F")

print(cels(98.6))
print(fahr(37))


# CHALLENGE 3

def click_counter():
    count = 0
    def click():
        count += 1
        print("Click", count)

    return click

counter = click_counter()
counter()
counter()
counter()
counter()