def counter():
    print("Count down is starting!")
    for i in range(10,0,-1):
        yield i

gen = counter()
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("Countdown finished!")
        break
        
