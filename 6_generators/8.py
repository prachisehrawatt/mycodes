def take(gen, n):
    lst = []
    for num in range(n):
        value = next(gen)
        lst.append(value)
    return lst

def inf_counter():
    num=0
    while True:
        yield num
        num=num+1

obj = inf_counter()
print(take(obj,5))

