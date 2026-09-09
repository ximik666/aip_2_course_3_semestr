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
