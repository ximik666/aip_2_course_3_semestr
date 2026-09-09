# Хранение данных в JSON и CSV

Алгоритмизация и программирование
2 курс · Лекция 4
Python

---

# Результат занятия

Выбрать JSON для вложенных данных и CSV для таблицы

Прочитать и записать UTF-8 файл с помощью with

Преобразовать строки CSV в числа

Разделить чтение файла и проверку структуры данных

---

# Состояние программы и файл

Память процесса не сохраняется после выхода

JSON хранит структуру, CSV представляет таблицу

Относительный путь зависит от рабочего каталога

---

# Состояние программы и файл · пример

```python
from pathlib import Path

base = Path("data")
path = base / "journal.json"
print(path.name)
print(path.suffix)
print(path.parent.name)
```

---

# JSON и типы данных

dumps создаёт JSON-строку, loads разбирает её

ensure_ascii=False сохраняет читаемую кириллицу

Корректный JSON может содержать неверные учебные данные

---

# JSON и типы данных · пример

```python
import json

student = {"name": "Анна", "grades": [4, 5], "active": True}
text = json.dumps(student, ensure_ascii=False)
print(text)
restored = json.loads(text)
print(restored == student)
```

---

# Чтение и запись UTF-8

Кодировка указывается явно

Режим w заменяет содержимое

Проверка включает повторное чтение

---

# Чтение и запись UTF-8 · пример

```python
import json
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "data.json"
    path.write_text(json.dumps(["Анна"], ensure_ascii=False), encoding="utf-8")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    print(loaded)
```

---

# CSV и разделители

Разделитель задаётся явно

DictReader использует имена из заголовка

Значения CSV нужно преобразовывать из строк

---

# CSV и разделители · пример

```python
import csv
import io

source = 'name;grade\n"Анна; староста";5\n'
rows = list(csv.DictReader(io.StringIO(source), delimiter=";"))
print(rows[0]["name"])
print(int(rows[0]["grade"]) + 1)
```

---

# Экспорт отчёта

fieldnames задаёт порядок столбцов

Заголовок нужен и пустому отчёту

Оформление чисел выполняется на границе экспорта

---

# Экспорт отчёта · пример

```python
import csv
import io

stream = io.StringIO(newline="")
writer = csv.DictWriter(stream, fieldnames=["name", "average"], delimiter=";")
writer.writeheader()
writer.writerow({"name": "Анна", "average": f"{14 / 3:.2f}"})
print(stream.getvalue(), end="")
```

---

# Версия и схема документа

version отличает форматы документа

Проверка структуры следует после разбора JSON

Новый журнал заменяет текущий только после успешной загрузки

---

# Версия и схема документа · пример

```python
def valid_root(data):
    return (isinstance(data, dict)
            and set(data) == {"version", "students"}
            and type(data["version"]) is int
            and data["version"] == 1
            and isinstance(data["students"], list))

print(valid_root({"version": 1, "students": []}))
print(valid_root({"version": True, "students": []}))
```

---

# Проверка полного цикла

Проверяется содержимое после загрузки

Нужны ошибки синтаксиса и ошибки схемы

Демонстрационные данные сохраняются отдельно от рабочих

---

# Проверка полного цикла · пример

```python
import json

original = {"version": 1, "students": [{"grades": [4]}]}
restored = json.loads(json.dumps(original))
assert restored == original
restored["students"][0]["grades"].append(5)
print(original["students"][0]["grades"])
print(restored["students"][0]["grades"])
```

---

# Самопроверка и практика

Можно ли считать оценки верными только потому, что loads завершился успешно?

Зачем сохранять заголовок, если в отчёте нет студентов?

Практики 7 и 8: применение материала
