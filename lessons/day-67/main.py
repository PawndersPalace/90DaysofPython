import os

language = os.getenv("COURSE_LANGUAGE", "Python")
print(f"Today's language: {language}")
print("Use environment variables for local configuration; never print secrets.")
