def select_group(students, group):
    result = []
    for student in students:
        if student["group"] == group:
            result.append(student)
    return result

rows = [{"name": "Анна", "group": "A"},
        {"name": "Борис", "group": "B"}]
print(select_group(rows, "A"))
