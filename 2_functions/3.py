#lambda function

'''Q1 : Using Lambda function, find the square of x.

Code :
square = lambda x: x ** 2
print(square(5))'''



lst = []
obj = [lambda x=x: x**2 for x in range(1,6)]
lst.append(obj)
print([i() for i in obj])



