book = ["Анна"]

def load_invalid():
    raise ValueError("Повреждённый файл")

try:
    loaded = load_invalid()
    book = loaded
except ValueError:
    print("Загрузка отменена")
print(book)
