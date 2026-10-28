# 90 Days of Python

A practical, beginner-friendly path from your first Python program to a finished
project. Learn a little each day, practice by building small things, and share
your progress.

No previous programming experience is needed. You will need a computer and an
internet connection to install Python and look up documentation.

## Start here

1. Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/).
   On Windows, select **Add Python to PATH** during installation.
2. Install [Visual Studio Code](https://code.visualstudio.com/) and its official
   Python extension, or use another editor you like.
3. Get this course:

   ```sh
   git clone https://github.com/PawndersPalace/90DaysofPython.git
   cd 90DaysofPython
   ```

   Or use GitHub's **Code → Download ZIP** button and unzip the download. To
   publish your own changes, fork the repository first and clone your fork.
4. Open the project folder in your editor. Run the first example:

   ```sh
   python lessons/day-01/main.py
   ```

   If `python` is not recognized on Windows, try `py` instead. On macOS or
   Linux, you may need `python3`.
5. Follow the [90-day curriculum](CURRICULUM.md). Every day links to its own
   lesson with a runnable example and a practice task. Aim for 30–60 minutes a
   day; taking a rest day or repeating a lesson is fine.

## How to use the course

- Read the day's topic and write the code yourself instead of only copying it.
- Run your code often. Read error messages carefully and try to fix one thing at
  a time.
- Do the practice task before looking up a solution. There are no grades.
- Keep your own work in a separate folder (for example, `my-work/`) so course
  examples stay unchanged.
- At the end of each week, review what you learned and explain one idea in your
  own words.
- If you get stuck, search the error message, consult the official
  [Python tutorial](https://docs.python.org/3/tutorial/), or open a discussion
  or issue in this repository.

## What's included

- [CURRICULUM.md](CURRICULUM.md): all 90 linked lessons, daily practice
  prompts, weekly projects, and a final capstone.
- [lessons/](lessons): a lesson guide and runnable Python example for each day.
- [lessons/day-01](lessons/day-01/README.md): start with your first program.
- [lessons/day-90](lessons/day-90/README.md): finish by building and sharing a
  personal reading tracker.
- [CONTRIBUTING.md](CONTRIBUTING.md): how to suggest improvements and share
  lessons or projects.

The roadmap is a guide, not a race. If a day takes longer than one day, that's
normal. You can also skip ahead and come back later.

## Following a lesson

Open the day's `README.md`, read its short explanation, predict what the
example will do, and run it from the repository root. Change a value, run the
example again, then try the practice prompt in your own folder. Each example
uses Python's standard library, runs offline, and avoids changing course files.

Some topics mention optional third-party tools such as `requests`, `ruff`,
`matplotlib`, Flask, and Streamlit. The core examples do not require installing
them; use a virtual environment and the tool's official beginner guide when
you want to explore further.

## Share your progress

You can publish your own completed exercises in a fork, create a discussion, or
share a short write-up of what you built. Please don't post passwords, API keys,
or other private information in code or screenshots.

## License

Course code is available under the [MIT License](LICENSE). Lesson text and
curriculum are available under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
