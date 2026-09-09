"""Стартовый файл. Замените NotImplementedError своими реализациями."""

class Student:

    def __init__(self, name, grades=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Пустое имя')
        self.name = ' '.join(name.split())
        if grades is not None and (not isinstance(grades, list)):
            raise ValueError('Ожидается список оценок')
        self.grades = []
        for grade in [] if grades is None else grades:
            self.add_grade(grade)

    def add_grade(self, grade):
        if type(grade) is not int or not 2 <= grade <= 5:
            raise ValueError('Неверная оценка')
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else None

    def to_dict(self):
        return {'name': self.name, 'grades': self.grades.copy()}

class GradeBook:

    def __init__(self):
        raise NotImplementedError('Выполните задание практики')

    def add(self, student_id, student):
        raise NotImplementedError('Выполните задание практики')

    def get(self, student_id):
        raise NotImplementedError('Выполните задание практики')

    def add_grade(self, student_id, grade):
        raise NotImplementedError('Выполните задание практики')

    def report(self):
        raise NotImplementedError('Выполните задание практики')
