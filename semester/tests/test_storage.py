import csv
import json
from pathlib import Path
import tempfile
import unittest
from journal.models import Student, GradeBook
from journal.storage import load_book, save_book, export_report


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "журнал.json"
        self.book = GradeBook()
        self.book.add_student(Student("2", 'Борис; "Б"', "B", [2, 5]))
        self.book.add_student(Student("1", "Анна", "A", [5, 4, 5]))
        self.book.add_student(Student("3", "Вера", "A"))

    def write_document(self, document):
        self.path.write_text(json.dumps(document, ensure_ascii=False), encoding="utf-8")

    def test_save_format_and_order(self):
        self.assertIsNone(save_book(self.book, self.path))
        document = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(set(document), {"version", "students"})
        self.assertEqual(document["version"], 1)
        self.assertIs(type(document["version"]), int)
        self.assertEqual([s["id"] for s in document["students"]], ["1", "2", "3"])
        self.assertIn("Анна", self.path.read_text(encoding="utf-8"))

    def test_round_trip(self):
        save_book(self.book, str(self.path))
        loaded = load_book(str(self.path))
        self.assertIsInstance(loaded, GradeBook)
        self.assertEqual(loaded.report(), self.book.report())
        loaded.add_grade("1", 2)
        self.assertEqual(self.book.get_student("1").grades, [5, 4, 5])

    def test_empty_round_trip(self):
        save_book(GradeBook(), self.path)
        self.assertEqual(load_book(self.path).report(), [])

    def test_overwrites_existing_file(self):
        self.path.write_text("старое содержимое" * 100, encoding="utf-8")
        save_book(GradeBook(), self.path)
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8")), {"version":1, "students":[]})

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_book(self.path)

    def test_missing_parent_save_and_export(self):
        for action in [save_book, export_report]:
            with self.subTest(action=action.__name__), self.assertRaises(OSError):
                action(self.book, self.path / "missing" / "file")

    def test_broken_json(self):
        self.path.write_text('{"students":', encoding="utf-8")
        with self.assertRaises(ValueError):
            load_book(self.path)

    def test_invalid_utf8(self):
        self.path.write_bytes(b'\xff\xfe\xfa')
        with self.assertRaises(ValueError):
            load_book(self.path)

    def test_document_schema(self):
        invalids = [None, [], {}, {"version":1}, {"students":[]},
                    {"version":2,"students":[]}, {"version":True,"students":[]},
                    {"version":1.0,"students":[]}, {"version":"1","students":[]},
                    {"version":1,"students":{}}, {"version":1,"students":[],"extra":1}]
        for value in invalids:
            with self.subTest(value=value):
                self.write_document(value)
                with self.assertRaises(ValueError):
                    load_book(self.path)

    def test_bad_student_rejects_whole_file(self):
        valid = Student("1", "Анна", "A", [4]).to_dict()
        for bad in [{**valid, "grades":[6]}, {**valid, "grades":None}, {**valid, "name":" "}, [], {}]:
            with self.subTest(bad=bad):
                self.write_document({"version":1,"students":[valid, bad]})
                with self.assertRaises(ValueError):
                    load_book(self.path)

    def test_duplicate_ids(self):
        record = Student("1", "Анна", "A", [4]).to_dict()
        self.write_document({"version":1,"students":[record, {**record, "id":" 1 "}]})
        with self.assertRaises(ValueError):
            load_book(self.path)

    def test_csv_values_escaping_and_order(self):
        self.assertIsNone(export_report(self.book, self.path))
        with self.path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, delimiter=";")
            self.assertEqual(reader.fieldnames, ["id","name","group","count","average","debt"])
            rows = list(reader)
        self.assertEqual([row["id"] for row in rows], ["1","2","3"])
        self.assertEqual(rows[0]["average"], "4.67")
        self.assertEqual(rows[1]["name"], 'Борис; "Б"')
        self.assertEqual(rows[1]["debt"], "yes")
        self.assertEqual(rows[1]["average"], "3.50")
        self.assertEqual(rows[2]["count"], "0")
        self.assertEqual(rows[2]["average"], "")
        self.assertEqual(rows[2]["debt"], "no")

    def test_csv_group_filter(self):
        export_report(self.book, self.path, "A")
        with self.path.open(encoding="utf-8", newline="") as stream:
            self.assertEqual([r["id"] for r in csv.DictReader(stream, delimiter=";")], ["1","3"])

    def test_csv_empty_header_only(self):
        export_report(GradeBook(), self.path)
        with self.path.open(encoding="utf-8", newline="") as stream:
            self.assertEqual(list(csv.reader(stream, delimiter=";")), [["id","name","group","count","average","debt"]])

    def test_csv_unknown_group_header_only(self):
        export_report(self.book, self.path, "Нет")
        with self.path.open(encoding="utf-8", newline="") as stream:
            self.assertEqual(len(list(csv.reader(stream, delimiter=";"))), 1)

    def test_sample_report(self):
        data = Path(__file__).resolve().parents[1] / "data"
        book = load_book(data / "demo.json")
        export_report(book, self.path)
        with self.path.open(encoding="utf-8", newline="") as actual:
            with (data / "expected_report.csv").open(encoding="utf-8", newline="") as expected:
                self.assertEqual(list(csv.reader(actual, delimiter=";")), list(csv.reader(expected, delimiter=";")))


if __name__ == "__main__":
    unittest.main()
