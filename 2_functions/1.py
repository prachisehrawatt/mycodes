'''def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

a=fact(5)
print (a)

#find recursive sum of first n numbers

def num(n):
    if n==1:
        return 1
    return n + num(n-1)

q=num(4)
print(q)


def fibonacci(n):
    if n <= 1:   
     return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))'''

def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a

print(fibo(10))

