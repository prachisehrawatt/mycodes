def fibonacci_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

fib = fibonacci_gen()
n = int(input("enter the range of fibonacci numbers to be printed : "))
for i in range(n):
    print(next(fib))