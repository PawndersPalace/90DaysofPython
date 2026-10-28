class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


catalog = [
    Book("Kindred", "Octavia Butler"),
    Book("The Hobbit", "J. R. R. Tolkien"),
]
for book in catalog:
    print(f"{book.title} — {book.author}")
