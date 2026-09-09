students = [{"name": "Анна", "group": "A"},
            {"name": "Борис", "group": "B"},
            {"name": "Вера", "group": "A"}]
counts = {}
for student in students:
    group = student["group"]
    counts[group] = counts.get(group, 0) + 1
print(counts)
