with open("log.txt", "r") as f1:
    with open("cities.txt", "a") as f2:
        for i in f1:
            f2.write(i)