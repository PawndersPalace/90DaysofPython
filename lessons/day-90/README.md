# Day 90: Share and reflect

## Goal

Use the ideas in today's example to work through this practice task:

> Publish your project or share it in a fork. Write down what you learned and what you want to build next.

## Today's idea

A small `argparse` interface supports `add` and `list` commands. Choose a data-file path explicitly if you want to keep the catalog outside the current folder.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-90/main.py
   ```

   If `python` is not recognized, try `py lessons/day-90/main.py` on
   Windows or `python3 lessons/day-90/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
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
```

## What to notice

- The lesson's topic is **Share and reflect**. Find the matching Python syntax in
  `main.py` and identify what each name and value represents.
- Follow the program from top to bottom. Trace how data changes and where it
  is displayed or returned.
- Run the file more than once after making small edits; the result should help
  you explain what the changed code does.

## Check your understanding

Explain the example in your own words. What would you change to make it handle
one more value or case? Try that change, run the file, and describe what
happened.

If today's lesson is a weekly review project, use this example as a starting
point and add the actions or features described in the practice task. A
project does not need to be perfect to count as progress.

## Try the finished tracker

The tracker stores data in a JSON file. From the repository root, add a book
and then list the saved books:

```sh
python lessons/day-90/main.py --data my-books.json add "Kindred" "Octavia Butler"
python lessons/day-90/main.py --data my-books.json list
```

The `--data` option makes the file location explicit. Keep the file in your
personal work folder if you do not want it in the repository.
