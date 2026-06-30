# create a custom discounnt function.
# students discount - 10%, vip discount - 20%
# pass amt & discount for calculation

def outer(amt):
    def inner(per):
        discount = (amt*per) / 100
        total_bill = amt - discount
        return total_bill
    return inner




amt = int(input("enter the cost of billing :"))
obj = outer(amt)
print(obj(10))

