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
