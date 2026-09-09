import json

original = {"version": 1, "students": [{"grades": [4]}]}
restored = json.loads(json.dumps(original))
assert restored == original
restored["students"][0]["grades"].append(5)
print(original["students"][0]["grades"])
print(restored["students"][0]["grades"])
