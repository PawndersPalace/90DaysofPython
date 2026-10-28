# Day 78: Data exploration

## Goal

Use the ideas in today's example to work through this practice task:

> Load a small public CSV with Python's built-in `csv` module and answer a question about it.

## Today's idea

`csv.DictReader` lets you explore tabular data by column name. Convert text values before finding averages or maximums.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-78/main.py
   ```

   If `python` is not recognized, try `py lessons/day-78/main.py` on
   Windows or `python3 lessons/day-78/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
import csv
from io import StringIO

data = StringIO("month,visitors\nJan,12\nFeb,18\nMar,15\n")
rows = list(csv.DictReader(data))
best_month = max(rows, key=lambda row: int(row["visitors"]))
average = sum(int(row["visitors"]) for row in rows) / len(rows)
print(f"Most visitors: {best_month['month']} ({best_month['visitors']})")
print(f"Monthly average: {average:.1f}")
```

## What to notice

- The lesson's topic is **Data exploration**. Find the matching Python syntax in
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
