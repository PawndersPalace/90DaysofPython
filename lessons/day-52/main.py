class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"


book = Book("Kindred", "Octavia Butler")
print(book.describe())
