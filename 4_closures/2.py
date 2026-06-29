def make_greeting(name):

    def greet():
        print(f"Hello {name} !")

    return greet

a = make_greeting("John")
b = make_greeting("Alice")

a()
b()