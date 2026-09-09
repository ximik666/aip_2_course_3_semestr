import unittest
from journal.models import Student, GradeBook


class StudentTests(unittest.TestCase):
    def test_create_normalizes_text(self):
        s = Student(" S01 ", "  Анна   Иванова\t", " ИС-21 ")
        self.assertEqual((s.student_id, s.name, s.group, s.grades), ("S01", "Анна Иванова", "ИС-21", []))

    def test_each_text_field_is_required(self):
        for index in range(3):
            for invalid in ["", " \t\n", None, 12, True]:
                args = ["S01", "Анна", "ИС-21"]
                args[index] = invalid
                with self.subTest(index=index, invalid=invalid), self.assertRaises(ValueError):
                    Student(*args)

    def test_grade_range_and_type(self):
        for invalid in [1, 6, -2, 0, 3.0, "4", True, False, None]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                Student("1", "Анна", "A", [invalid])

    def test_grades_container(self):
        for invalid in [(4, 5), "45", {4, 5}, 4]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                Student("1", "Анна", "A", invalid)

    def test_constructor_copies_grades(self):
        grades = [4]
        student = Student("1", "Анна", "A", grades)
        grades.append(2)
        self.assertEqual(student.grades, [4])

    def test_default_lists_are_independent(self):
        a, b = Student("1", "А", "A"), Student("2", "Б", "A")
        a.add_grade(5)
        self.assertEqual(b.grades, [])

    def test_average_empty(self):
        self.assertIsNone(Student("1", "А", "A").average())

    def test_average_is_not_rounded(self):
        self.assertAlmostEqual(Student("1", "А", "A", [5, 4, 5]).average(), 14 / 3)

    def test_add_all_valid_grades(self):
        student = Student("1", "А", "A")
        for grade in range(2, 6):
            self.assertIsNone(student.add_grade(grade))
        self.assertEqual(student.grades, [2, 3, 4, 5])

    def test_invalid_add_leaves_state_unchanged(self):
        student = Student("1", "А", "A", [5])
        for invalid in [6, 1, True, "4", 4.0, None]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                student.add_grade(invalid)
        self.assertEqual(student.grades, [5])

    def test_debt_means_at_least_one_two(self):
        self.assertTrue(Student("1", "А", "A", [5, 2, 5]).has_debt())
        self.assertFalse(Student("1", "А", "A", [3, 4]).has_debt())
        self.assertFalse(Student("1", "А", "A", []).has_debt())

    def test_to_dict_and_independent_list(self):
        student = Student("1", "А", "A", [4])
        data = student.to_dict()
        self.assertEqual(data, {"id": "1", "name": "А", "group": "A", "grades": [4]})
        data["grades"].append(2)
        self.assertEqual(student.grades, [4])

    def test_from_dict_round_trip(self):
        data = {"id": "1", "name": "А", "group": "A", "grades": [4]}
        student = Student.from_dict(data)
        self.assertIsInstance(student, Student)
        self.assertEqual(student.to_dict(), data)
        data["grades"].append(2)
        self.assertEqual(student.grades, [4])

    def test_from_dict_invalid_fields(self):
        base = {"id": "1", "name": "А", "group": "A", "grades": [4]}
        invalids = [None, [], {}, {**base, "extra": 1}, {**base, "grades": None}, {**base, "grades": [6]}]
        invalids += [{key: value for key, value in base.items() if key != missing} for missing in base]
        for data in invalids:
            with self.subTest(data=data), self.assertRaises(ValueError):
                Student.from_dict(data)


class GradeBookTests(unittest.TestCase):
    def setUp(self):
        self.book = GradeBook()
        self.students = [Student("2", "борис", "B", [2, 5]), Student("3", "Анна", "A"), Student("1", "анна", "A", [5, 4, 5])]
        for student in self.students:
            self.book.add_student(student)

    def test_empty_book(self):
        self.assertEqual(GradeBook().list_students(), [])
        self.assertEqual(GradeBook().report(), [])

    def test_get_returns_stored_object(self):
        self.assertIs(self.book.get_student("2"), self.students[0])

    def test_ids_are_case_sensitive(self):
        book = GradeBook()
        book.add_student(Student("a", "А", "A"))
        book.add_student(Student("A", "Б", "A"))
        self.assertEqual(len(book.list_students()), 2)

    def test_duplicate_rejected_without_replacement(self):
        with self.assertRaises(ValueError):
            self.book.add_student(Student("2", "Новый", "C"))
        self.assertIs(self.book.get_student("2"), self.students[0])

    def test_non_student_rejected(self):
        for value in [None, {}, "Анна"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.book.add_student(value)

    def test_missing_id_raises_key_error(self):
        for action in [lambda: self.book.get_student("X"), lambda: self.book.remove_student("X"), lambda: self.book.add_grade("X", 5)]:
            with self.assertRaises(KeyError):
                action()

    def test_remove(self):
        self.assertIsNone(self.book.remove_student("2"))
        self.assertEqual(len(self.book.list_students()), 2)
        with self.assertRaises(KeyError):
            self.book.get_student("2")

    def test_add_grade(self):
        self.assertIsNone(self.book.add_grade("3", 4))
        self.assertEqual(self.book.get_student("3").grades, [4])

    def test_invalid_grade_no_mutation(self):
        with self.assertRaises(ValueError):
            self.book.add_grade("3", True)
        self.assertEqual(self.book.get_student("3").grades, [])

    def test_sort_by_casefold_name_then_id(self):
        self.assertEqual([s.student_id for s in self.book.list_students()], ["1", "3", "2"])

    def test_list_container_is_independent(self):
        result = self.book.list_students()
        result.clear()
        self.assertEqual(len(self.book.list_students()), 3)

    def test_exact_group_filter(self):
        self.assertEqual([s.student_id for s in self.book.list_students("A")], ["1", "3"])
        self.assertEqual(self.book.list_students("a"), [])
        self.assertEqual(self.book.list_students("X"), [])

    def test_find_casefold_substring_and_strip(self):
        self.assertEqual([s.student_id for s in self.book.find_students(" АН ")], ["1", "3"])
        self.assertEqual(self.book.find_students("нет совпадения"), [])

    def test_find_empty(self):
        self.assertEqual(self.book.find_students(" \t"), [])

    def test_find_non_string(self):
        with self.assertRaises(ValueError):
            self.book.find_students(None)

    def test_report_contract(self):
        rows = self.book.report("A")
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], {"id":"1", "name":"анна", "group":"A", "count":3, "average":14 / 3, "debt":False})
        self.assertEqual(rows[1], {"id":"3", "name":"Анна", "group":"A", "count":0, "average":None, "debt":False})
        rows[0]["name"] = "Подмена"
        self.assertEqual(self.book.get_student("1").name, "анна")


if __name__ == "__main__":
    unittest.main()
