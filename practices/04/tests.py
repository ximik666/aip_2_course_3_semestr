import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def setUp(self):
        self.rows = [{"id":"2","name":"анна","group":"A"}, {"id":"3","name":"Борис","group":"B"}, {"id":"1","name":"Анна","group":"A"}]
    def test_filter(self):
        self.assertEqual([r["id"] for r in m.select_group(self.rows, "A")], ["2","1"])
        self.assertEqual(m.select_group(self.rows, "a"), [])
    def test_counts(self):
        self.assertEqual(m.count_by_group(self.rows), {"A":2,"B":1})
        self.assertEqual(m.count_by_group([]), {})
    def test_sort(self):
        self.assertEqual([r["id"] for r in m.sort_records(self.rows)], ["1","2","3"])
        self.assertEqual([r["id"] for r in self.rows], ["2","3","1"])
    def test_empty(self):
        self.assertEqual(m.sort_records([]), [])
        self.assertEqual(m.select_group([], "A"), [])
