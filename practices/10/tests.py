import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(m.average([4,4]), 4)
        self.assertIsNone(m.average([]))
    def test_boundaries(self):
        self.assertEqual(m.validate_grade(2), 2)
        self.assertEqual(m.validate_grade(5), 5)
        for value in [1,6]:
            with self.assertRaises(ValueError): m.validate_grade(value)
    def test_types(self):
        for value in [True, 4.0, "4", None]:
            with self.subTest(value=value), self.assertRaises(ValueError): m.validate_grade(value)
    def test_clone(self):
        row = {"name":"А","grades":[4]}
        result = m.clone_record(row)
        self.assertEqual(result, row)
        result["grades"].append(2)
        result["name"] = "Б"
        self.assertEqual(row, {"name":"А","grades":[4]})
