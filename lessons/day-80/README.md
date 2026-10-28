# Day 80: Web apps

## Goal

Use the ideas in today's example to work through this practice task:

> Explore a beginner-friendly framework such as Flask or Streamlit; run its official hello-world example.

## Today's idea

A web app turns a request into a response such as an HTML page. This standard-library example builds a page string without starting a server.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-80/main.py
   ```

   If `python` is not recognized, try `py lessons/day-80/main.py` on
   Windows or `python3 lessons/day-80/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
def make_page(title, message):
    return (
        "<!doctype html>\n"
        "<html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{title}</title></head>"
        f"<body><h1>{title}</h1><p>{message}</p></body></html>"
    )


print(make_page("My first page", "I built this with Python."))
print("Optional next step: follow the official Flask or Streamlit quickstart.")
```

## What to notice

- The lesson's topic is **Web apps**. Find the matching Python syntax in
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

## Optional: start a tiny Flask app

After completing Day 46, install Flask in a virtual environment. Save the
following as `app.py` in your own project folder:

```python
from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "<h1>Hello, Python!</h1>"
```

Run it locally with `flask --app app run --debug`, then open the local address
shown in the terminal. The development server is for learning on your own
computer, not for hosting a public website. The daily `main.py` builds HTML
without requiring Flask or starting a server.
