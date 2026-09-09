import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(m.parse_grade(" 4 "), 4)
        self.assertEqual(m.parse_grade("+2"), 2)
        for value in ["пять","4.0","6","",4,None,True]:
            with self.subTest(value=value), self.assertRaises(ValueError): m.parse_grade(value)
    def test_add(self):
        grades = [4]
        self.assertIsNone(m.add_grade_safe(grades, 5))
        self.assertEqual(grades, [4,5])
    def test_bad_add_no_mutation(self):
        grades = [4]
        for value in [True, 4.0, "4", 1, 6, None]:
            with self.subTest(value=value), self.assertRaises(ValueError): m.add_grade_safe(grades, value)
        self.assertEqual(grades, [4])
    def test_get(self):
        row = {"name":"А"}
        self.assertIs(m.get_record({"1":row}, "1"), row)
        with self.assertRaises(KeyError): m.get_record({}, "X")
