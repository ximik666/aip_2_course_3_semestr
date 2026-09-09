import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_append_independent(self):
        original = [4]
        result = m.append_grade(original, 5)
        self.assertEqual(result, [4, 5])
        self.assertEqual(original, [4])
        self.assertIsNot(original, result)
    def test_summary(self):
        self.assertEqual(m.student_summary("А", [2, 5]), {"name":"А", "count":2, "average":3.5, "debt":True})
    def test_empty(self):
        self.assertEqual(m.student_summary("А", []), {"name":"А", "count":0, "average":None, "debt":False})
        self.assertEqual(m.make_report([]), [])
    def test_report(self):
        source = [{"name":"Б", "grades":[5]}, {"name":"А", "grades":[]}]
        self.assertEqual([r["name"] for r in m.make_report(source)], ["Б", "А"])
        self.assertEqual(source[0]["grades"], [5])
