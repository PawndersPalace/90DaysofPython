# Day 79: Visualization

## Goal

Use the ideas in today's example to work through this practice task:

> Install `matplotlib` in a virtual environment and chart a small dataset.

## Today's idea

A bar chart maps numeric values to visual lengths. The standard-library example is text-only; a `matplotlib` extension is optional.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-79/main.py
   ```

   If `python` is not recognized, try `py lessons/day-79/main.py` on
   Windows or `python3 lessons/day-79/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
months = {"Jan": 4, "Feb": 7, "Mar": 5}
for month, value in months.items():
    print(f"{month}: {'#' * value} ({value})")
print("Optional: install matplotlib to turn a dataset into a plotted chart.")
```

## What to notice

- The lesson's topic is **Visualization**. Find the matching Python syntax in
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

## Optional: make a chart with matplotlib

After completing Day 46, install `matplotlib` in a virtual environment. Save
this as `chart.py` in your own project folder and run `python chart.py`:

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar"]
visitors = [4, 7, 5]
plt.bar(months, visitors)
plt.title("Visitors by month")
plt.ylabel("Visitors")
plt.show()
```

The daily `main.py` uses a text-only chart, so it remains runnable without
extra packages or a graphical display.
