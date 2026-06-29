def outer():
    x = 42

    def inner():
        return x

    return inner

func = outer()

# stores cell objects address where value is stored
print(func.__closure__)
print(func.__closure__[1].cell_contents)