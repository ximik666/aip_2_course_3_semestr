import json

student = {"name": "Анна", "grades": [4, 5], "active": True}
text = json.dumps(student, ensure_ascii=False)
print(text)
restored = json.loads(text)
print(restored == student)
