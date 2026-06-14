def palindrome_num(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

x = -121
print(palindrome_num(x))

