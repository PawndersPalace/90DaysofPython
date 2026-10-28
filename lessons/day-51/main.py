class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("Kindred", "Octavia Butler")
print(f"{book.title} was written by {book.author}.")
