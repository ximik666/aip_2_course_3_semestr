# Ошибки, отладка и автоматические тесты

Алгоритмизация и программирование
2 курс · Лекция 5
Python

---

# Результат занятия

Различать синтаксическую, исполнительную и логическую ошибку

Выбирать ValueError и KeyError по смыслу

Сохранять прежнее состояние при неудачной операции

Писать тесты unittest с временными файлами

---

# Виды ошибок и чтение traceback

Исключение и неверный результат требуют разных проверок

Traceback читается от типа ошибки к строке своего кода

Минимальный воспроизводимый вход ускоряет поиск

---

# Виды ошибок и чтение traceback · пример

```python
try:
    grade = int("пять")
except ValueError as error:
    print(type(error).__name__)
    print("Нужно целое число, например 5")
```

---

# Проверка данных и raise

Контракт определяет допустимые типы и значения

Проверка предшествует изменению состояния

Преобразование ввода отделяется от проверки модели

---

# Проверка данных и raise · пример

```python
def validate_grade(value):
    if type(value) is not int or not 2 <= value <= 5:
        raise ValueError("Оценка должна быть целым числом 2–5")
    return value

print(validate_grade(4))
try:
    validate_grade(True)
except ValueError:
    print("Логическое значение отклонено")
```

---

# Обработка ошибок на границе интерфейса

Модель сообщает об ошибке, интерфейс объясняет её пользователю

Перехватываются ожидаемые типы исключений

Молчаливое подавление мешает обнаружить проблему

---

# Обработка ошибок на границе интерфейса · пример

```python
def parse_grade(text):
    value = int(text.strip())
    if not 2 <= value <= 5:
        raise ValueError("Оценка вне диапазона")
    return value

for text in [" 4 ", "пять", "6"]:
    try:
        print(parse_grade(text))
    except ValueError:
        print("Введите целое число от 2 до 5")
```

---

# План тестирования

Ожидаемый результат определяется независимо

Нужны обычные и граничные случаи

Числа и их строковое оформление проверяются по-разному

---

# План тестирования · пример

```python
def average(grades):
    return sum(grades) / len(grades) if grades else None

assert average([4, 4]) == 4
assert average([2]) == 2
assert average([]) is None
print("Обычный, граничный и пустой случаи проверены")
```

---

# unittest

Тестовые методы начинаются с test_

Названия описывают проверяемое правило

Успех требует найденных и выполненных тестов

---

# unittest · пример

```python
import unittest
import io

class GradeTests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([2, 5]), 7)
    def test_empty(self):
        self.assertEqual(sum([]), 0)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(GradeTests)
result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
print(result.testsRun, result.wasSuccessful())
```

---

# Проверка исключения и сохранности данных

Проверяется конкретный тип исключения

После ошибки проверяется прежнее состояние

Загрузка заменяет данные только после полного успеха

---

# Проверка исключения и сохранности данных · пример

```python
grades = [4]

def add_grade(value):
    if type(value) is not int or not 2 <= value <= 5:
        raise ValueError("Неверная оценка")
    grades.append(value)

try:
    add_grade(6)
except ValueError:
    pass
print(grades)
```

---

# Тестирование файлов

Временный каталог изолирует файлы теста

Проверяется содержимое, а не только наличие

Каждый тест создаёт собственные исходные данные

---

# Тестирование файлов · пример

```python
from pathlib import Path
import tempfile

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "report.txt"
    path.write_text("Анна: 4.50\n", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "Анна: 4.50\n"
    print("Файловая проверка выполнена")
```

---

# Самопроверка и практика

Почему int(value) внутри модели может скрыть ошибку?

Почему сообщение «Ran 0 tests» не подтверждает корректность решения?

Практики 9 и 10: применение материала
