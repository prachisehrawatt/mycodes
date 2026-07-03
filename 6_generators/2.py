def generator_squares(n):
    for i in range(n):
        yield i ** 2

a=generator_squares(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
