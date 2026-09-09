import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            rows = [{"name":"Анна", "grades":[4,5]}]
            self.assertIsNone(m.save_records(rows, path))
            self.assertIn("Анна", path.read_text(encoding="utf-8"))
            self.assertEqual(m.load_records(str(path)), rows)
    def test_empty_and_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            m.save_records([{"name":"длинная запись"}], path)
            m.save_records([], path)
            self.assertEqual(m.load_records(path), [])
    def test_errors(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            with self.assertRaises(FileNotFoundError): m.load_records(path)
            path.write_text('{}', encoding="utf-8")
            with self.assertRaises(ValueError): m.load_records(path)
            path.write_text('[', encoding="utf-8")
            with self.assertRaises(ValueError): m.load_records(path)
    def test_copy(self):
        rows = [{"grades":[4]}]
        result = m.copy_records(rows)
        result[0]["grades"].append(5)
        self.assertEqual(rows, [{"grades":[4]}])
