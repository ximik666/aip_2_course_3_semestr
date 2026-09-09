"""Стартовый файл. Замените NotImplementedError своими реализациями."""

class Student:

    def __init__(self, name, grades=None):
        raise NotImplementedError('Выполните задание практики')

    def add_grade(self, grade):
        raise NotImplementedError('Выполните задание практики')

    def average(self):
        raise NotImplementedError('Выполните задание практики')

    def to_dict(self):
        raise NotImplementedError('Выполните задание практики')
