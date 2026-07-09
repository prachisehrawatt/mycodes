f = open("books.txt","w")
f.write("maths \n")
f.write("eng \n")
f.write("hindi \n")
f.write("science \n")
f.close()

try:
    with open("books.txt", "r") as f:
        books = f.readlines()
    for i in range(len(books)):
        books[i] = books[i].strip()
    books.sort()

    with open("catalog.txt", "w") as file:
        for book in books:
            file.write(book + "\n")
    print("books sorted successfully !")

except FileNotFoundError:
    print("books.txt not found.")