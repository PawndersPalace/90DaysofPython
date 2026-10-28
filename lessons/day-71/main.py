from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    workspace = Path(folder)
    for name in ["draft.txt", "notes.txt"]:
        (workspace / name).write_text("sample", encoding="utf-8")
    for old_path in sorted(workspace.glob("*.txt")):
        new_path = old_path.with_name(f"archived-{old_path.name}")
        print(f"Preview: {old_path.name} -> {new_path.name}")
