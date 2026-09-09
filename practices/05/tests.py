import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(m.tokenize("Кот,пёс! КОТ-2."), ["кот","пёс","кот"])
        self.assertEqual(m.tokenize("Ёж\tи\nёж"), ["ёж","и","ёж"])
        self.assertEqual(m.tokenize("123 !?"), [])
    def test_counts(self):
        self.assertEqual(m.frequencies(["кот","кот","пёс"]), {"кот":2,"пёс":1})
        self.assertEqual(m.frequencies([]), {})
    def test_top(self):
        counts = {"б":2,"а":2,"в":3}
        self.assertEqual(m.top_words(counts, 2), [("в",3),("а",2)])
        self.assertEqual(m.top_words(counts, 10), [("в",3),("а",2),("б",2)])
        self.assertEqual(m.top_words(counts, -1), [])
    def test_pipeline(self):
        self.assertEqual(m.top_words(m.frequencies(m.tokenize("Дом, дом. Кот!")), 1), [("дом",2)])
