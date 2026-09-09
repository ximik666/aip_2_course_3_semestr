import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_add(self):
        book = {}
        record = {"id":"1", "name":"А", "group":"A"}
        self.assertTrue(m.add_record(book, record))
        self.assertIs(book["1"], record)
    def test_duplicate(self):
        book = {"1":{"id":"1", "name":"А", "group":"A"}}
        self.assertFalse(m.add_record(book, {"id":"1", "name":"Б", "group":"B"}))
        self.assertEqual(book["1"]["name"], "А")
    def test_change(self):
        book = {"1":{"id":"1", "name":"А", "group":"A"}}
        self.assertTrue(m.change_group(book, "1", "B"))
        self.assertEqual(book["1"], {"id":"1", "name":"А", "group":"B"})
        self.assertFalse(m.change_group(book, "X", "B"))
    def test_remove(self):
        book = {"1":{}}
        self.assertTrue(m.remove_record(book, "1"))
        self.assertEqual(book, {})
        self.assertFalse(m.remove_record(book, "1"))
