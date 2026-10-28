books = []


def add_book(title, author):
    books.append({"title": title, "author": author})


def find_books(search):
    search = search.casefold()
    return [
        book for book in books
        if search in book["title"].casefold() or search in book["author"].casefold()
    ]


add_book("Kindred", "Octavia Butler")
print(f"Search results: {find_books('butler')}")
