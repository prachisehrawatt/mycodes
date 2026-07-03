def take(gen, n):
    lst = []
    for i in range(n):
        value = next(gen)
        lst.append(value)
    return lst


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print(take(fib, 10))