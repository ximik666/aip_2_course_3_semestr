def valid_root(data):
    return (isinstance(data, dict)
            and set(data) == {"version", "students"}
            and type(data["version"]) is int
            and data["version"] == 1
            and isinstance(data["students"], list))

print(valid_root({"version": 1, "students": []}))
print(valid_root({"version": True, "students": []}))
