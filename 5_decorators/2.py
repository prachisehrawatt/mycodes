import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("start")
        results = func(*args,**kwargs) 
        print("end")
        return results
    return wrapper
@start_end_decorator
def add5(a):
    return a+5

#main()
print(add5(34))
print(help(add5))
print(add5.__name__)
