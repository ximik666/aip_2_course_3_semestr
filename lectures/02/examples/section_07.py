rows = [{"id": "2", "name": "анна"},
        {"id": "1", "name": "Анна"},
        {"id": "3", "name": "Борис"}]
ordered = sorted(rows, key=lambda row: (row["name"].casefold(), row["id"]))
print([row["id"] for row in ordered])
