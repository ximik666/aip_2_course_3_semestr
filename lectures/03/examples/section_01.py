def normalize_name(text):
    return " ".join(text.split())

print(normalize_name("  Анна\t  Иванова\n"))
print(repr(normalize_name(" \t ")))
