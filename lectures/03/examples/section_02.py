def find_names(names, query):
    query = query.strip().casefold()
    if not query:
        return []
    return [name for name in names if query in name.casefold()]

print(find_names(["Анна", "Борис", "Антон"], " АН "))
print(find_names(["Анна"], " "))
