original = {"id": "1", "grades": [4, 5]}
copied = {"id": original["id"],
          "grades": original["grades"].copy()}
copied["grades"].append(2)
print(original)
print(copied)
