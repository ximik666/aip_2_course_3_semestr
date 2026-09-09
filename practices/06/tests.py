import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(m.normalize_name("  Анна\t Иванова\n"), "Анна Иванова")
        self.assertEqual(m.normalize_name(" \t"), "")
    def test_unique(self):
        names = [" Анна ", "АННА", "Борис", " ", "борис"]
        self.assertEqual(m.unique_names(names), ["Анна","Борис"])
        self.assertEqual(names[0], " Анна ")
    def test_find(self):
        self.assertEqual(m.find_names(["Анна","Антон","Борис"], " АН "), ["Анна","Антон"])
        self.assertEqual(m.find_names(["Анна"], ""), [])
        self.assertEqual(m.find_names(["Анна"], "Борис"), [])
    def test_empty(self):
        self.assertEqual(m.unique_names([]), [])
        self.assertEqual(m.find_names([], "А"), [])
