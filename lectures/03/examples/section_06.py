def unique_names(names):
    result, seen = [], set()
    for raw in names:
        name = " ".join(raw.split())
        key = name.casefold()
        if name and key not in seen:
            seen.add(key)
            result.append(name)
    return result

print(unique_names([" Анна ", "Борис", "АННА", ""]))
