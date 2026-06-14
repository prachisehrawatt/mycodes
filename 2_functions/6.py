def roman_to_int(x):

    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    count = 0
    for i in range(len(x)):

        if i < len(x)-1 and roman[x[i]] < roman[x[i+1]]:
            count -= roman[x[i]]
        else:
            count += roman[x[i]]

    return count

x = "MCMXCIV"
print(roman_to_int(x))