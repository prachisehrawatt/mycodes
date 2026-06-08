'''Q4. Write a single line of Python code that modifies the passwords list in-place so that the longest strings appear at index 0, and the shortest strings appear at the end. (Using sort function only)

passwords = ["qwerty", "admin123", "P@ss", "SuperSecretCode99", "12345678", "dev"]'''


passwords = ["qwerty", "admin123", "P@ss", "SuperSecretCode99", "12345678", "dev"]

passwords.sort(key=len, reverse=True)
print(passwords)