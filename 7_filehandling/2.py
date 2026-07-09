books = [

    "The Alchemist",
    "Harry Potter and the Philosopher's Stone",
    "To Kill a Mockingbird",
    "The Great Gatsby",
    "Pride and Prejudice",
    "The Hobbit",
    "The Catcher in the Rye",
    "1984",
    "The Lord of the Rings",
    "The Da Vinci Code"

]

with open("book_1.txt", "w") as input_file:
    input_file.write("\n".join(books))
with open("book_1.txt", "r") as input_file:
    with open("catalog.txt", "w") as output_file:
        book = input_file.read().split("\n")
        print(book)
        book.sort()
        output_file.write("".join(book))