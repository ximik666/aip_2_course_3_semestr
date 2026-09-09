# Основы объектно-ориентированного программирования

Алгоритмизация и программирование
2 курс · Лекция 6
Python

---

# Результат занятия

Создать независимые экземпляры класса

Объяснить self и назначение __init__

Проверять данные при создании объекта и добавлении оценки

Собрать класс-контейнер из объектов другого класса

---

# Класс и объект

Класс описывает сущность, объект хранит конкретное состояние

self обозначает текущий экземпляр

__init__ задаёт начальные атрибуты

---

# Класс и объект · пример

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

anna = Student("Анна")
boris = Student("Борис")
anna.grades.append(5)
print(anna.name, anna.grades)
print(boris.name, boris.grades)
```

---

# Методы и ответственность объекта

Метод получает доступ к состоянию через self

Вычислительный контракт сохраняется

Модель не содержит интерактивного ввода

---

# Методы и ответственность объекта · пример

```python
class Student:
    def __init__(self, grades):
        self.grades = grades.copy()
    def average(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

print(Student([4, 5]).average())
print(Student([]).average())
```

---

# Проверка состояния

Конструктор отклоняет неверные начальные данные

Методы изменения повторно проверяют вход

Правила обращения к атрибутам описываются в контракте

---

# Проверка состояния · пример

```python
class Student:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя не может быть пустым")
        self.name = " ".join(name.split())

print(Student("  Анна   Иванова ").name)
try:
    Student(" ")
except ValueError:
    print("Пустое имя отклонено")
```

---

# Общие и индивидуальные атрибуты

Состояние экземпляра создаётся через self

Изменяемый атрибут класса может стать общим

Независимость проверяется на двух объектах

---

# Общие и индивидуальные атрибуты · пример

```python
class Student:
    def __init__(self, grades=None):
        self.grades = [] if grades is None else grades.copy()

a, b = Student(), Student()
a.grades.append(5)
assert b.grades == []
print(a.grades, b.grades)
```

---

# Композиция: журнал содержит студентов

Журнал управляет коллекцией студентов

Студент управляет собственными оценками

Одна операция делегирует часть работы другой сущности

---

# Композиция: журнал содержит студентов · пример

```python
class Student:
    def __init__(self, student_id):
        self.student_id = student_id

class GradeBook:
    def __init__(self):
        self.students = {}
    def add(self, student):
        self.students[student.student_id] = student

book = GradeBook()
book.add(Student("S01"))
print(book.students["S01"].student_id)
```

---

# Преобразование объекта в словарь

to_dict возвращает простые значения для JSON

Вложенный список копируется

from_dict создаёт объект через обычный конструктор

---

# Преобразование объекта в словарь · пример

```python
class Student:
    def __init__(self, name):
        self.name = name
    def to_dict(self):
        return {"name": self.name}
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])

student = Student.from_dict({"name": "Анна"})
print(student.to_dict())
```

---

# Тестирование класса

Проверяются результат и состояние

Копирование требуется только там, где его обещает контракт

Класс удобно развивать по одному методу

---

# Тестирование класса · пример

```python
class Student:
    def __init__(self):
        self.grades = []
    def add_grade(self, grade):
        if type(grade) is not int or not 2 <= grade <= 5:
            raise ValueError("Неверная оценка")
        self.grades.append(grade)

s = Student()
s.add_grade(5)
assert s.grades == [5]
print("Метод изменил состояние по контракту")
```

---

# Самопроверка и практика

Зачем копировать входной список в __init__?

Кто должен проверять диапазон оценки: Student или меню?

Практики 11 и 12: применение материала
