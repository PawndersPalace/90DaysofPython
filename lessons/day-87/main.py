import json
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    data_file = Path(folder) / "books.json"
    books = [{"title": "Kindred", "author": "Octavia Butler"}]
    data_file.write_text(json.dumps(books, indent=2), encoding="utf-8")
    loaded_books = json.loads(data_file.read_text(encoding="utf-8"))
    print(f"Saved and loaded {len(loaded_books)} book.")
