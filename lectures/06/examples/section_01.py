class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

anna = Student("Анна")
boris = Student("Борис")
anna.grades.append(5)
print(anna.name, anna.grades)
print(boris.name, boris.grades)
