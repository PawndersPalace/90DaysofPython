from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    journal = Path(folder) / "journal.txt"
    journal.write_text("Today I practiced Python.\n", encoding="utf-8")
    print(journal.read_text(encoding="utf-8"), end="")
