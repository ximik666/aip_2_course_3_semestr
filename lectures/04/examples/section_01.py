from pathlib import Path

base = Path("data")
path = base / "journal.json"
print(path.name)
print(path.suffix)
print(path.parent.name)
