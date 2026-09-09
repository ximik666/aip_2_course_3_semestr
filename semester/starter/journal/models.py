"""Заполните методы по контракту из semester/SPECIFICATION.md."""

class Student:
    def __init__(self, student_id, name, group, grades=None):
        raise NotImplementedError("Реализуйте создание и проверку Student")

    def add_grade(self, grade):
        raise NotImplementedError

    def average(self):
        raise NotImplementedError

    def has_debt(self):
        raise NotImplementedError

    def to_dict(self):
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data):
        raise NotImplementedError


class GradeBook:
    def __init__(self):
        raise NotImplementedError

    def add_student(self, student):
        raise NotImplementedError

    def get_student(self, student_id):
        raise NotImplementedError

    def remove_student(self, student_id):
        raise NotImplementedError

    def add_grade(self, student_id, grade):
        raise NotImplementedError

    def list_students(self, group=None):
        raise NotImplementedError

    def find_students(self, query):
        raise NotImplementedError

    def report(self, group=None):
        raise NotImplementedError
