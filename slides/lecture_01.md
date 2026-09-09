# Функции и организация программы

Алгоритмизация и программирование
2 курс · Лекция 1
Python

---

# Результат занятия

Сформулировать контракт функции до написания кода

Отделить вычисления от input и print

Обработать пустой список и избежать случайного изменения данных

Собрать отчёт из нескольких небольших функций

---

# Декомпозиция задачи

Одна функция решает одну понятную задачу

Входные данные передаются параметрами

Результат возвращается вызывающему коду

---

# Декомпозиция задачи · пример

```python
def count_debts(grades):
    count = 0
    for grade in grades:
        if grade == 2:
            count += 1
    return count

print(count_debts([5, 2, 4, 2]))
```

---

# Контракт функции и пустые данные

Вход: список оценок от 2 до 5

Пустой список даёт None

Округление выполняется при отображении

---

# Контракт функции и пустые данные · пример

```python
def average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

print(average([5, 4, 5]))
print(average([]))
```

---

# return и print

return передаёт значение

print выводит текст

Форматирование тоже может возвращать строку

---

# return и print · пример

```python
def format_average(value):
    if value is None:
        return "нет оценок"
    return f"{value:.2f}"

result = format_average(14 / 3)
print("Средний балл:", result)
print(format_average(None))
```

---

# Параметры и именованные аргументы

Параметр задаёт роль входного значения

Именованный аргумент поясняет вызов

Для изменяемых значений по умолчанию нужен отдельный разбор

---

# Параметры и именованные аргументы · пример

```python
def passing(grades, minimum=3):
    result = []
    for grade in grades:
        if grade >= minimum:
            result.append(grade)
    return result

print(passing([2, 3, 4, 5]))
print(passing([2, 3, 4, 5], minimum=4))
```

---

# Изменение списка и копирование

Передача списка не создаёт копию

copy создаёт новый внешний список

Изменение входа должно быть частью контракта

---

# Изменение списка и копирование · пример

```python
def with_grade(grades, grade):
    result = grades.copy()
    result.append(grade)
    return result

original = [4, 5]
updated = with_grade(original, 3)
print(original)
print(updated)
```

---

# Сборка результата из функций

Небольшие функции можно соединять

Именованные поля поясняют результат

Каждый этап учитывает контракт предыдущего

---

# Сборка результата из функций · пример

```python
def average(grades):
    return sum(grades) / len(grades) if grades else None

def summary(grades):
    return {"count": len(grades),
            "average": average(grades),
            "debt": 2 in grades}

print(summary([2, 4, 5]))
```

---

# Самопроверка и читаемость

Ожидаемый результат рассчитывается заранее

assert подходит для учебной самопроверки

Валидация пользователя требует обычного кода

---

# Самопроверка и читаемость · пример

```python
def count_debts(grades):
    return grades.count(2)

assert count_debts([]) == 0
assert count_debts([3, 4, 5]) == 0
assert count_debts([2, 5, 2]) == 2
print("3 проверки выполнены")
```

---

# Самопроверка и практика

Чем отсутствие оценок отличается от среднего балла 2?

Почему нельзя заменить grades.copy() на grades?

Практики 1 и 2: применение материала
