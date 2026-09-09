book = {"1": {"name": "Анна", "group": "A"},
        "2": {"name": "Борис", "group": "B"}}
book["1"]["group"] = "B"
keys = [key for key in book if book[key]["name"] == "Борис"]
for key in keys:
    del book[key]
print(book)
