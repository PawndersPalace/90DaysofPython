# Day 46: Installing packages

## Goal

Use the ideas in today's example to work through this practice task:

> Create a virtual environment and install a package with `pip`.

## Today's idea

A virtual environment keeps a project's packages separate from other Python projects. Install packages with `python -m pip` inside it.

## Work through the example

1. Read `main.py` once before running it. Look for the values, operations, and
   output that match today's topic.
2. Predict what it will print. Then run it from the repository root:

   ```sh
   python lessons/day-46/main.py
   ```

   If `python` is not recognized, try `py lessons/day-46/main.py` on
   Windows or `python3 lessons/day-46/main.py` on macOS and Linux.
3. Compare the output with your prediction. Change one value or condition and
   run the example again.
4. Make a separate copy of the example in your own work folder and try the
   practice task above. Keep the lesson files as a reference.

### Example code

```python
import sys

print(f"Python version: {sys.version.split()[0]}")
print("Create a virtual environment with: python -m venv .venv")
print("Activate it, then install a package with: python -m pip install requests")
```

## What to notice

- The lesson's topic is **Installing packages**. Find the matching Python syntax in
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

## Optional: create a virtual environment

Run these commands from your own project folder. A virtual environment keeps
packages for one project separate from your other Python projects.

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install requests
```

On macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
```

When you are finished, type `deactivate` to leave the environment. The
`requests` package is optional for this course; the daily examples do not need
it.
