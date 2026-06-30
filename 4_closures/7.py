def outer():
    x = int(input("enter the initial balance : "))
    def inner():
        nonlocal x
        x+=500
        return x
    return inner

obj = outer()

print(obj())
print(obj())
print(obj())
