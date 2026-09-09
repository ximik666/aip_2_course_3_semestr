import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_create(self):
        s = m.Student("  Анна   Иванова ", [4])
        self.assertEqual(s.name, "Анна Иванова")
        for value in ["", " ", None]:
            with self.assertRaises(ValueError): m.Student(value)
    def test_independence(self):
        source = [4]
        a, b = m.Student("А", source), m.Student("Б")
        source.append(2)
        a.add_grade(5)
        self.assertEqual(a.grades, [4,5])
        self.assertEqual(b.grades, [])
    def test_validation(self):
        s = m.Student("А")
        for value in [True, 4.0, "4", 1, 6]:
            with self.assertRaises(ValueError): s.add_grade(value)
        self.assertEqual(s.grades, [])
        with self.assertRaises(ValueError): m.Student("А", (4,5))
        with self.assertRaises(ValueError): m.Student("А", [6])
    def test_average_and_export(self):
        s = m.Student("А", [4,5])
        self.assertEqual(s.average(), 4.5)
        self.assertIsNone(m.Student("Б").average())
        data = s.to_dict()
        self.assertEqual(data, {"name":"А","grades":[4,5]})
        data["grades"].append(2)
        self.assertEqual(s.grades, [4,5])
