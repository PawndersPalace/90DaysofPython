# Day 40: Paths and folders

## Goal

Use the ideas in today's example to work through this practice task:

> Use `pathlib` to list files in a folder.

## Today's idea

`Path` represents a file or directory. `iterdir()` lists a folder's immediate contents without needing string path manipulation.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-40/main.py
   ```

   If `python` is not recognized, try `py lessons/day-40/main.py` on
   Windows or `python3 lessons/day-40/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    workspace = Path(folder)
    (workspace / "notes.txt").write_text("practice", encoding="utf-8")
    (workspace / "todo.txt").write_text("review", encoding="utf-8")
    for path in sorted(workspace.iterdir()):
        print(f"{path.name}: {path.read_text(encoding='utf-8')}")
```

## What to notice

- The lesson's topic is **Paths and folders**. Find the matching Python syntax in
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
