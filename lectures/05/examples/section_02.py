def validate_grade(value):
    if type(value) is not int or not 2 <= value <= 5:
        raise ValueError("Оценка должна быть целым числом 2–5")
    return value

print(validate_grade(4))
try:
    validate_grade(True)
except ValueError:
    print("Логическое значение отклонено")
