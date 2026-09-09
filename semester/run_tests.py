"""Запуск: python semester/run_tests.py --solution semester/submission."""
import argparse
import importlib
from pathlib import Path
import sys
import unittest


def main():
    parser = argparse.ArgumentParser(description="Проверка учебного журнала")
    parser.add_argument("--solution", type=Path, default=Path(__file__).parent / "starter")
    parser.add_argument("--pattern", default="test_*.py", help="Например, test_models.py")
    args = parser.parse_args()
    solution = args.solution.resolve()
    if not (solution / "journal" / "__init__.py").is_file():
        parser.error(f"Нет пакета journal в каталоге {solution}")
    sys.path.insert(0, str(solution))
    package = importlib.import_module("journal")
    if Path(package.__file__).resolve().parent != solution / "journal":
        parser.error("Импортирован посторонний пакет journal")
    print(f"Проверяется: {solution}", flush=True)
    suite = unittest.defaultTestLoader.discover(str(Path(__file__).parent / "tests"), pattern=args.pattern)
    if suite.countTestCases() == 0:
        parser.error("Тесты не найдены: проверьте --pattern")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
