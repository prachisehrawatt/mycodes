
def start_end_decorator(func):  # 
    def wrapper():              # 
        print("start")
        func()
        print("end")
    return wrapper

@start_end_decorator
def print_name():   #
    print("prachi")

#main()

print_name()

#obj = start_end_decorator(print_name)
#print(obj())