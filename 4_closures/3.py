def multiplier(n):

    def multiply(x):
        return x * n

    return multiply

db = multiplier(2)
tr = multiplier(3)

print(db(5))
print(tr(5))
