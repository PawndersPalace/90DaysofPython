# Day 33: Breaking down a problem

## Goal

Use the ideas in today's example to work through this practice task:

> Split a calculator into small functions.

## Today's idea

Small functions give a program one clear job per step. Check invalid inputs, such as division by zero, before calculating.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-33/main.py
   ```

   If `python` is not recognized, try `py lessons/day-33/main.py` on
   Windows or `python3 lessons/day-33/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
def add(first, second):
    return first + second


def divide(first, second):
    if second == 0:
        raise ValueError("The divisor cannot be zero.")
    return first / second


print(f"4 + 3 = {add(4, 3)}")
print(f"8 / 2 = {divide(8, 2)}")
```

## What to notice

- The lesson's topic is **Breaking down a problem**. Find the matching Python syntax in
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
