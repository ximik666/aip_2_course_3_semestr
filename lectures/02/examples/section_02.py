def add_record(book, record):
    key = record["id"]
    if key in book:
        return False
    book[key] = record
    return True

book = {}
print(add_record(book, {"id": "S01", "name": "Анна"}))
print(add_record(book, {"id": "S01", "name": "Борис"}))
print(book["S01"]["name"])
