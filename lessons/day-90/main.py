import argparse
import json
from pathlib import Path


def load_books(path):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description="A small personal reading tracker.")
    parser.add_argument("--data", type=Path, default=Path("books.json"))
    commands = parser.add_subparsers(dest="command")
    add_command = commands.add_parser("add", help="Add a book")
    add_command.add_argument("title")
    add_command.add_argument("author")
    commands.add_parser("list", help="List saved books")
    args = parser.parse_args()
    books = load_books(args.data)

    if args.command == "add":
        title, author = args.title.strip(), args.author.strip()
        if not title or not author:
            parser.error("title and author must not be empty")
        books.append({"title": title, "author": author})
        args.data.write_text(json.dumps(books, indent=2), encoding="utf-8")
        print(f"Added {title}.")
    elif args.command == "list":
        if not books:
            print("No books saved yet.")
        for book in books:
            print(f"{book['title']} by {book['author']}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
