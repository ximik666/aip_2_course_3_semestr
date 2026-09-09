"""Запускает проверки отдельного файла решения, не меняя исходные тесты."""
import argparse
import importlib.util
from pathlib import Path
import sys
import unittest

parser = argparse.ArgumentParser()
parser.add_argument("--solution", type=Path, default=Path(__file__).with_name("starter.py"))
args = parser.parse_args()
path = args.solution.resolve()
if not path.is_file():
    parser.error(f"Файл решения не найден: {path}")
spec = importlib.util.spec_from_file_location("solution", path)
module = importlib.util.module_from_spec(spec)
sys.modules["solution"] = module
spec.loader.exec_module(module)
tests = unittest.defaultTestLoader.discover(str(Path(__file__).parent), pattern="tests.py")
if tests.countTestCases() == 0:
    parser.error("Проверки не найдены")
print(f"Проверяется: {path}", flush=True)
result = unittest.TextTestRunner(verbosity=2).run(tests)
raise SystemExit(0 if result.wasSuccessful() else 1)
