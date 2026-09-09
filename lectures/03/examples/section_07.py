def normalize_name(text):
    return " ".join(text.split())

cases = [("  Анна   Иванова ", "Анна Иванова"),
         ("\t\n", ""), ("Борис", "Борис")]
for source, expected in cases:
    assert normalize_name(source) == expected
print("Проверка нормализации завершена")
