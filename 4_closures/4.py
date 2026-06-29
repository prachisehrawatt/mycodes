'''square = power(2)
print(square(5))'''

def outer(n): # num
    def inner(x): #power
        return n**x
    
    return inner

square = outer(5)
print(square(2))
