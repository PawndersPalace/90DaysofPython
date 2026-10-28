# Day 87: Save or retrieve data

## Goal

Use the ideas in today's example to work through this practice task:

> Add a file, JSON, SQLite, or API feature if your project needs it.

## Today's idea

JSON lets a small application save records between runs. This example uses a temporary file; the final project adds an explicit file path.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-87/main.py
   ```

   If `python` is not recognized, try `py lessons/day-87/main.py` on
   Windows or `python3 lessons/day-87/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
import json
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    data_file = Path(folder) / "books.json"
    books = [{"title": "Kindred", "author": "Octavia Butler"}]
    data_file.write_text(json.dumps(books, indent=2), encoding="utf-8")
    loaded_books = json.loads(data_file.read_text(encoding="utf-8"))
    print(f"Saved and loaded {len(loaded_books)} book.")
```

## What to notice

- The lesson's topic is **Save or retrieve data**. Find the matching Python syntax in
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
