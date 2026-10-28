from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    notes_file = Path(folder) / "notes.txt"
    notes = ["Practice functions", "Review today's lesson"]
    notes_file.write_text("\n".join(notes) + "\n", encoding="utf-8")
    saved_notes = notes_file.read_text(encoding="utf-8").splitlines()
    for number, note in enumerate(saved_notes, start=1):
        print(f"{number}. {note}")
