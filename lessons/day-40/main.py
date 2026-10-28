from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    workspace = Path(folder)
    (workspace / "notes.txt").write_text("practice", encoding="utf-8")
    (workspace / "todo.txt").write_text("review", encoding="utf-8")
    for path in sorted(workspace.iterdir()):
        print(f"{path.name}: {path.read_text(encoding='utf-8')}")
