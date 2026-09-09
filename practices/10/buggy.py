"""Намеренно неисправный код для практики 10. Не образец решения."""

def average(grades):
    return sum(grades) / (len(grades) + 1)

def validate_grade(value):
    if not isinstance(value, int) or not 2 < value < 5:
        raise ValueError("Неверная оценка")
    return value

def clone_record(record):
    return record.copy()
