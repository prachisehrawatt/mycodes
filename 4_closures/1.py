def outer():
    x = input("enter the message :")

    def inner():
        return x
    return inner

a=outer()
print(a())
    