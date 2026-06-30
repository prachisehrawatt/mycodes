'''Write a function make_accumulator() that returns an inner function add(value).
Each call to add should add value to a running total (maintained via closure) and return the new total.
For example :

acc = make_accumulator()
acc(10)   # returns 10
acc(5)    # returns 15'''

def make_accumulator():
    total = 0
    def add(value):
        nonlocal total
        total += value
        return total
    return add



acc = make_accumulator()
print(acc(10))   
print(acc(5))    
 
