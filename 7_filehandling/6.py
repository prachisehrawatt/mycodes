with open("temp_c.txt", "r") as c_f, open("temp_f.txt", "w") as f_f:
    for line in c_f:
        celsius = float(line.strip())
        fahrenheit = celsius * 9/5+32
        f_f.write(f"{fahrenheit}\n")
        print(fahrenheit)