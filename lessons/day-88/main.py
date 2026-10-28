def validate_book(title, author):
    title = title.strip()
    author = author.strip()
    if not title or not author:
        raise ValueError("Both title and author are required.")
    return {"title": title, "author": author}


for title, author in [(" Kindred ", "Octavia Butler"), ("", "Unknown")]:
    try:
        print(validate_book(title, author))
    except ValueError as error:
        print(f"Could not add book: {error}")
