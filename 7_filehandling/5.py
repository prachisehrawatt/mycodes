with open("cities.txt", "w") as f:
    f.write("Tokyo\n")
    f.write("Paris\n")
    f.write("New York\n")
    f.write("Sydney\n")

with open("cities.txt", "r") as f:
    cities = f.readlines()
    print("Number of cities saved:", len(cities))
    