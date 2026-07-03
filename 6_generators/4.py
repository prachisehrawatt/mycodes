lst = [7, 4, 8, 6]
def gen_sort():
    for i in lst:
        yield i

obj = gen_sort()

new_lst = list(obj)  
new_lst.sort()     
print(new_lst)
