# Day 66: API responses

## Goal

Use the ideas in today's example to work through this practice task:

> Check a response's status and handle malformed or missing data.

## Today's idea

A server response can be malformed or omit expected fields. Catch `JSONDecodeError`, then validate the type and presence of values you use.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-66/main.py
   ```

   If `python` is not recognized, try `py lessons/day-66/main.py` on
   Windows or `python3 lessons/day-66/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
import json

def read_title(response_text):
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError as error:
        print(f"Response was not valid JSON: {error.msg}")
        return None
    title = data.get("title")
    if not isinstance(title, str):
        print("Response has no text title.")
        return None
    return title


print(read_title('{"title": "Practice parsing"}'))
print(read_title("{broken"))
```

## What to notice

- The lesson's topic is **API responses**. Find the matching Python syntax in
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
