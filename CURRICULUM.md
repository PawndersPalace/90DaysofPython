# 90-day curriculum

This curriculum assumes no prior programming experience. Each day has a topic
and a small task. Try to write and run code for every task; notes and pseudocode
are useful if you get stuck. Weekly projects combine the ideas you have
practiced.

## Week 1: Getting started

- [ ] **Day 1 — Your first program:** Run `lessons/day-01/main.py`, change its
  message, and add a second `print()`.
- [ ] **Day 2 — Values and variables:** Store your name, a favorite number, and
  a goal in variables; print them.
- [ ] **Day 3 — Numbers and arithmetic:** Calculate the total cost of three
  items, including tax.
- [ ] **Day 4 — Text and strings:** Make a short introduction using string
  concatenation and an f-string.
- [ ] **Day 5 — Getting input:** Ask for a name and greet the person.
- [ ] **Day 6 — Converting types:** Ask for two numbers and print their sum.
- [ ] **Day 7 — Review project:** Make a tip calculator that asks for a bill
  and tip percentage.

## Week 2: Decisions and repetition

- [ ] **Day 8 — Comparisons:** Compare two numbers and print which is larger.
- [ ] **Day 9 — `if` and `else`:** Ask for an age and report whether the person
  is an adult.
- [ ] **Day 10 — Multiple conditions:** Make a score-to-grade checker using
  `if`, `elif`, and `else`.
- [ ] **Day 11 — Boolean logic:** Check whether a number is in a range using
  `and`, `or`, and `not`.
- [ ] **Day 12 — `while` loops:** Repeat a prompt until the user enters
  `quit`.
- [ ] **Day 13 — `for` loops:** Print a multiplication table for a chosen
  number.
- [ ] **Day 14 — Review project:** Build a number-guessing game with a limited
  number of attempts.

## Week 3: Strings and collections

- [ ] **Day 15 — String methods:** Clean up user-entered text with
  `strip()`, `lower()`, and `title()`.
- [ ] **Day 16 — Indexes and slices:** Display the first, last, and middle
  characters of a word.
- [ ] **Day 17 — Lists:** Store a shopping list and let the user add an item.
- [ ] **Day 18 — List operations:** Add, remove, sort, and count items in a
  list.
- [ ] **Day 19 — Tuples:** Represent a point or RGB color as a tuple and read
  its values.
- [ ] **Day 20 — Dictionaries:** Make a contact card with a name, email, and
  phone number.
- [ ] **Day 21 — Review project:** Create a simple quiz that tracks the score.

## Week 4: Working with collections

- [ ] **Day 22 — Sets:** Find common and unique items between two lists.
- [ ] **Day 23 — Nested data:** Represent a small menu as a list of
  dictionaries and print each item.
- [ ] **Day 24 — Looping through data:** Count how often each word appears in
  a sentence.
- [ ] **Day 25 — List comprehensions:** Build a list of the squares of even
  numbers.
- [ ] **Day 26 — Sorting and keys:** Sort a list of names by length.
- [ ] **Day 27 — Membership and copying:** Filter a list without accidentally
  changing the original.
- [ ] **Day 28 — Review project:** Build a command-line shopping list with
  add, show, and remove actions.

## Week 5: Functions

- [ ] **Day 29 — Defining functions:** Put a repeated greeting into a
  function.
- [ ] **Day 30 — Parameters and return values:** Write a function that converts
  minutes to seconds.
- [ ] **Day 31 — Default and keyword arguments:** Create a customizable
  greeting function.
- [ ] **Day 32 — Scope:** Experiment with local variables and function
  parameters.
- [ ] **Day 33 — Breaking down a problem:** Split a calculator into small
  functions.
- [ ] **Day 34 — Docstrings:** Add a useful docstring to each function in a
  small program.
- [ ] **Day 35 — Review project:** Build a unit converter with separate
  conversion functions.

## Week 6: Errors, files, and data

- [ ] **Day 36 — Reading errors:** Intentionally cause a `NameError`, then fix
  it using the traceback.
- [ ] **Day 37 — Handling exceptions:** Catch invalid number input and ask
  again.
- [ ] **Day 38 — Reading files:** Read a text file and print its contents.
- [ ] **Day 39 — Writing files:** Save a journal entry to a text file.
- [ ] **Day 40 — Paths and folders:** Use `pathlib` to list files in a folder.
- [ ] **Day 41 — CSV files:** Read a small CSV and calculate a total from one
  column.
- [ ] **Day 42 — Review project:** Make a notes app that saves and reloads
  notes from a file.

## Week 7: Modules and testing

- [ ] **Day 43 — Imports:** Use `random` to choose a random item from a list.
- [ ] **Day 44 — Standard library:** Use `datetime` to calculate days until a
  chosen date.
- [ ] **Day 45 — Your own modules:** Move a helper function into a second
  Python file and import it.
- [ ] **Day 46 — Installing packages:** Create a virtual environment and
  install a package with `pip`.
- [ ] **Day 47 — Testing with `assert`:** Check a function's expected output
  with a few assertions.
- [ ] **Day 48 — `unittest`:** Write and run a test case for a conversion
  function.
- [ ] **Day 49 — Review project:** Add tests and a README to one of your
  earlier projects.

## Week 8: Object-oriented Python

- [ ] **Day 50 — Classes and objects:** Create a `Book` class and make two
  books.
- [ ] **Day 51 — `__init__` and attributes:** Give a class attributes based on
  constructor arguments.
- [ ] **Day 52 — Instance methods:** Add a method that describes an object.
- [ ] **Day 53 — Class design:** Model a bank account with deposit and
  withdrawal methods.
- [ ] **Day 54 — Inheritance:** Extend a base class with one specialized
  behavior.
- [ ] **Day 55 — Dataclasses:** Represent a simple record using `dataclass`.
- [ ] **Day 56 — Review project:** Build a small library catalog using classes.

## Week 9: Practical Python tools

- [ ] **Day 57 — JSON:** Save a dictionary to JSON and load it back.
- [ ] **Day 58 — Command-line arguments:** Read an argument with `argparse`.
- [ ] **Day 59 — Logging:** Record program events with Python's `logging`
  module.
- [ ] **Day 60 — Regular expressions:** Find email-like strings in sample
  text; discuss what a simple pattern misses.
- [ ] **Day 61 — Dates and times:** Parse a date string and format it for
  display.
- [ ] **Day 62 — SQLite basics:** Create a database table and insert a sample
  record with `sqlite3`.
- [ ] **Day 63 — Review project:** Make a command-line task tracker that stores
  tasks in SQLite.

## Week 10: APIs and web data

- [ ] **Day 64 — What is an API?:** Read an API's documentation and identify
  its endpoint and response format.
- [ ] **Day 65 — HTTP requests:** In a virtual environment, install `requests`
  and fetch a public JSON endpoint.
- [ ] **Day 66 — API responses:** Check a response's status and handle
  malformed or missing data.
- [ ] **Day 67 — Secrets and configuration:** Read a setting from an
  environment variable; never commit a real secret.
- [ ] **Day 68 — Pagination and limits:** Inspect an API's rate limits and
  practice following pagination using its documented test endpoint.
- [ ] **Day 69 — Data cleanup:** Convert a list of JSON records into a
  readable summary.
- [ ] **Day 70 — Review project:** Build a small API-powered lookup tool,
  following the service's terms and rate limits.

## Week 11: Automation and code quality

- [ ] **Day 71 — Automating repetitive work:** Write a script that renames
  sample files in a temporary folder.
- [ ] **Day 72 — Safe file operations:** Preview proposed file changes before
  applying them.
- [ ] **Day 73 — Type hints:** Add parameter and return annotations to a
  function.
- [ ] **Day 74 — Formatting:** Install and run `ruff format` in a virtual
  environment.
- [ ] **Day 75 — Linting:** Run `ruff check` and fix a few reported issues.
- [ ] **Day 76 — Project structure:** Organize a small project into a package,
  README, and tests.
- [ ] **Day 77 — Review project:** Polish one earlier project, add usage
  instructions, and run its tests.

## Week 12: Choose a direction

- [ ] **Day 78 — Data exploration:** Load a small public CSV with Python's
  built-in `csv` module and answer a question about it.
- [ ] **Day 79 — Visualization:** Install `matplotlib` in a virtual
  environment and chart a small dataset.
- [ ] **Day 80 — Web apps:** Explore a beginner-friendly framework such as
  Flask or Streamlit; run its official hello-world example.
- [ ] **Day 81 — Games:** Use `turtle` or another beginner tool to make a
  simple interactive drawing.
- [ ] **Day 82 — Automation idea:** Pick a safe, repetitive task you understand
  and write down its inputs, steps, and expected result.
- [ ] **Day 83 — Compare approaches:** Pick one direction and list what you
  would need to learn to build a small project in it.
- [ ] **Day 84 — Capstone planning:** Choose a project, write a short feature
  list, and split it into small tasks.

## Final six days: Build and share

- [ ] **Day 85 — Capstone setup:** Create the project folder, README, and a
  working first version.
- [ ] **Day 86 — Core feature:** Implement the most important user-facing
  feature.
- [ ] **Day 87 — Save or retrieve data:** Add a file, JSON, SQLite, or API
  feature if your project needs it.
- [ ] **Day 88 — Make it reliable:** Handle a common error and write tests for
  the most important behavior.
- [ ] **Day 89 — Polish:** Improve names, messages, formatting, and setup
  instructions; ask someone to try it.
- [ ] **Day 90 — Share and reflect:** Publish your project or share it in a
  fork. Write down what you learned and what you want to build next.

## Capstone ideas

- A personal budget or habit tracker
- A command-line flashcard quiz
- A recipe organizer with search
- A weather lookup using a documented public API
- A small CSV report generator
- A text-based adventure game
- A personal website or dashboard using a beginner web framework

Choose a project small enough to finish. A useful, simple version is better
than a large unfinished one.
