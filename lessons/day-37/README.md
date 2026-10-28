# Day 37: Handling exceptions

## Goal

Use the ideas in today's example to work through this practice task:

> Catch invalid number input and ask again.

## Today's idea

`try` runs code that might fail; `except ValueError` handles a specific invalid conversion. Validate the range as well as the type.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-37/main.py
   ```

   If `python` is not recognized, try `py lessons/day-37/main.py` on
   Windows or `python3 lessons/day-37/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
def parse_quantity(text):
    try:
        quantity = int(text)
    except ValueError:
        print(f"{text!r} is not a whole number.")
        return None
    if quantity < 0:
        print("Quantity cannot be negative.")
        return None
    return quantity


print(parse_quantity("3"))
print(parse_quantity("three"))
```

## What to notice

- The lesson's topic is **Handling exceptions**. Find the matching Python syntax in
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
