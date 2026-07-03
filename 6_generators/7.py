def grep_lines(filename, keyword):
    with open(filename, "r") as obj:
        for i in obj:
            if keyword in i:
                yield i.strip()

filename = "log.txt"
keyword = "ERROR"
for j in grep_lines(filename, keyword):
    print(j)