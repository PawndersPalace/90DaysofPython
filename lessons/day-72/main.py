from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    workspace = Path(folder)
    original = workspace / "draft.txt"
    original.write_text("sample file", encoding="utf-8")
    proposed = original.with_name("draft-backup.txt")
    apply_changes = False
    print(f"Plan: {original.name} -> {proposed.name}")
    if apply_changes:
        original.rename(proposed)
    else:
        print("Preview only; no files were changed.")
