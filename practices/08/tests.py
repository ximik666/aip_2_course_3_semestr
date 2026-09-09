import unittest
import tempfile
from pathlib import Path
import csv
import solution as m


class PracticeTests(unittest.TestCase):
    def test_read(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "grades.csv"
            path.write_text('name;grade\n"Анна; староста";5\n', encoding="utf-8")
            self.assertEqual(m.read_grades(path), [{"name":"Анна; староста","grade":5}])
    def test_summary(self):
        rows = [{"name":"Б","grade":3},{"name":"А","grade":4},{"name":"А","grade":5}]
        self.assertEqual(m.summarize_rows(rows), [{"name":"А","count":2,"average":4.5},{"name":"Б","count":1,"average":3.0}])
    def test_write(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "report.csv"
            row = {"name":'Анна; "А"',"count":3,"average":14/3}
            self.assertIsNone(m.write_summary([row], path))
            with path.open(encoding="utf-8", newline="") as stream:
                self.assertEqual(list(csv.reader(stream, delimiter=";")), [["name","count","average"],['Анна; "А"',"3","4.67"]])
            self.assertIsInstance(row["average"], float)
    def test_empty(self):
        self.assertEqual(m.summarize_rows([]), [])
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "empty.csv"
            path.write_text('name;grade\n', encoding="utf-8")
            self.assertEqual(m.read_grades(path), [])
            m.write_summary([], path)
            self.assertEqual(path.read_text(encoding="utf-8").strip(), "name;count;average")
