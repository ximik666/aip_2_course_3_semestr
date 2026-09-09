import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(m.average([5, 4, 5]), 14 / 3)
        self.assertIsNone(m.average([]))
        self.assertEqual(m.average([2]), 2)
    def test_debts(self):
        self.assertEqual(m.count_debts([2, 5, 2]), 2)
        self.assertEqual(m.count_debts([]), 0)
    def test_format(self):
        self.assertEqual(m.format_summary("Анна", [4, 5]), "Анна: средний 4.50; двоек 0")
        self.assertEqual(m.format_summary("Борис", []), "Борис: средний нет оценок; двоек 0")
    def test_no_mutation(self):
        grades = [2, 5, 4]
        m.format_summary("А", grades)
        self.assertEqual(grades, [2, 5, 4])
