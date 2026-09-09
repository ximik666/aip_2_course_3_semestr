from pathlib import Path
import tempfile

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "report.txt"
    path.write_text("Анна: 4.50\n", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "Анна: 4.50\n"
    print("Файловая проверка выполнена")
