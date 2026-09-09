import unittest
import io

class GradeTests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([2, 5]), 7)
    def test_empty(self):
        self.assertEqual(sum([]), 0)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(GradeTests)
result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
print(result.testsRun, result.wasSuccessful())
