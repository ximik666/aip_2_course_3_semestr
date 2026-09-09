class Student:
    def __init__(self, grades):
        self.grades = grades.copy()
    def average(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

print(Student([4, 5]).average())
print(Student([]).average())
