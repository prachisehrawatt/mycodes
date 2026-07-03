def even_num():
    for i in range(1, 11):
        if i%2==0:
            yield i

obj = even_num()
while True:
    try:
        print(next(obj))
    except StopIteration:
        break
    