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
