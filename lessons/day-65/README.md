# Day 65: HTTP requests

## Goal

Use the ideas in today's example to work through this practice task:

> In a virtual environment, install `requests` and fetch a public JSON endpoint.

## Today's idea

`Request` describes an HTTP request, but this example deliberately does not send it. Keeping the demonstration offline makes it reliable and free of unexpected network calls.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-65/main.py
   ```

   If `python` is not recognized, try `py lessons/day-65/main.py` on
   Windows or `python3 lessons/day-65/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
import json
from urllib.request import Request

url = "https://jsonplaceholder.typicode.com/todos/1"
request = Request(url, headers={"Accept": "application/json"})
sample_response = '{"userId": 1, "id": 1, "title": "learn Python", "completed": false}'
print(f"Prepared a GET request for: {request.full_url}")
print(f"Sample JSON title: {json.loads(sample_response)['title']}")
print("The example does not need a network connection to run.")
```

## What to notice

- The lesson's topic is **HTTP requests**. Find the matching Python syntax in
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

## Optional: fetch a public JSON example

After completing Day 46, install `requests` in your virtual environment. This
example makes a read-only request to a public practice API. It needs an
internet connection and may be unavailable if that service is down:

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1",
    timeout=10,
)
response.raise_for_status()
todo = response.json()
print(todo["title"])
```

The runnable `main.py` deliberately does not contact the internet, so the core
lesson works offline. Check any real service's documentation, terms, and rate
limits before using it.
