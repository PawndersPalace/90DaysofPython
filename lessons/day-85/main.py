books = []


def add_book(title, author):
    books.append({"title": title, "author": author})


add_book("Kindred", "Octavia Butler")
for book in books:
    print(f"{book['title']} by {book['author']}")
