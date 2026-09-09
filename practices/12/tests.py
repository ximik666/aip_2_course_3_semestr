import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_add_get(self):
        b, s = m.GradeBook(), m.Student("А")
        self.assertIsNone(b.add("1", s))
        self.assertIs(b.get("1"), s)
        with self.assertRaises(ValueError): b.add("1", m.Student("Б"))
        self.assertIs(b.get("1"), s)
    def test_invalid(self):
        b = m.GradeBook()
        for key in ["", " 1", None]:
            with self.assertRaises(ValueError): b.add(key, m.Student("А"))
        with self.assertRaises(ValueError): b.add("1", {})
        with self.assertRaises(KeyError): b.get("X")
    def test_grade(self):
        b = m.GradeBook()
        b.add("1", m.Student("А"))
        b.add_grade("1", 5)
        self.assertEqual(b.get("1").grades, [5])
        with self.assertRaises(ValueError): b.add_grade("1", True)
        with self.assertRaises(KeyError): b.add_grade("X", 5)
        self.assertEqual(b.get("1").grades, [5])
    def test_report(self):
        b = m.GradeBook()
        self.assertEqual(b.report(), [])
        b.add("2", m.Student("А"))
        b.add("1", m.Student("Б", [4,5]))
        self.assertEqual(b.report(), [{"id":"1","name":"Б","average":4.5},{"id":"2","name":"А","average":None}])
