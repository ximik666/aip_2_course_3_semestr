class Student:
    def __init__(self, grades=None):
        self.grades = [] if grades is None else grades.copy()

a, b = Student(), Student()
a.grades.append(5)
assert b.grades == []
print(a.grades, b.grades)
