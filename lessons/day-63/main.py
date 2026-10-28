import sqlite3
from tempfile import TemporaryDirectory
from pathlib import Path

with TemporaryDirectory() as folder:
    db = sqlite3.connect(Path(folder) / "tasks.sqlite")
    with db:
        db.execute("CREATE TABLE tasks (name TEXT, done INTEGER DEFAULT 0)")
        db.executemany("INSERT INTO tasks (name) VALUES (?)", [("Practice",), ("Review",)])
        for name, done in db.execute("SELECT name, done FROM tasks ORDER BY name"):
            status = "done" if done else "to do"
            print(f"{name}: {status}")
    db.close()
