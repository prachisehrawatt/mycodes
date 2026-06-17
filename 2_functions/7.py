#ques 2
celsius_to_fahrenheit = lambda celsius: celsius * 1.8 + 32
print(celsius_to_fahrenheit(0)) 
print(celsius_to_fahrenheit(100)) 
print(celsius_to_fahrenheit(-40)) 



#ques 3
raw_data = ["apple", "cat", "python", "ok", "code"]
lst = []
clean_strings = [x for x in raw_data if len(x)>3 ]
print(clean_strings)  



#ques 4
cart = [
    ("Wireless Mouse", 25),
    ("Gaming Monitor", 299),
    ("Mechanical Keyboard", 85),
    ("USB-C Cable", 12)
]

lst = []
sorted_cart = [x for x in cart]
sorted(cart,reverse=True)
print(sorted_cart)