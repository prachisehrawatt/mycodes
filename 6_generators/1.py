def new_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
obj = new_generator()
'''for i in obj:
    print(i)'''

value = next(obj)
print(value)
print(next(obj))
print(next(obj))
print(next(obj))
