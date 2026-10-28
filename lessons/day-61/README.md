# Day 61: Dates and times

## Goal

Use the ideas in today's example to work through this practice task:

> Parse a date string and format it for display.

## Today's idea

`strptime()` parses text using an explicit format. `strftime` formatting codes create readable dates from a date or datetime.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-61/main.py
   ```

   If `python` is not recognized, try `py lessons/day-61/main.py` on
   Windows or `python3 lessons/day-61/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
from datetime import datetime

date_text = "2026-10-28"
parsed_date = datetime.strptime(date_text, "%Y-%m-%d")
print(f"Long form: {parsed_date:%B %d, %Y}")
print(f"ISO form: {parsed_date.date().isoformat()}")
```

## What to notice

- The lesson's topic is **Dates and times**. Find the matching Python syntax in
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
