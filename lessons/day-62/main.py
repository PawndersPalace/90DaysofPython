import sqlite3
from tempfile import TemporaryDirectory
from pathlib import Path

with TemporaryDirectory() as folder:
    database = Path(folder) / "reading.sqlite"
    connection = sqlite3.connect(database)
    with connection:
        connection.execute("CREATE TABLE books (title TEXT, pages INTEGER)")
        connection.execute("INSERT INTO books VALUES (?, ?)", ("Kindred", 264))
        rows = connection.execute("SELECT title, pages FROM books").fetchall()
    connection.close()
    print(rows)
