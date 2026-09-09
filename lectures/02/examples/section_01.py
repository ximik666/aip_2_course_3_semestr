student = {"id": "S01", "name": "Анна",
           "group": "ИС-21", "grades": [4, 5]}
print(student["name"])
print(student.get("email", "не указан"))
student["grades"].append(3)
print(student["grades"])
