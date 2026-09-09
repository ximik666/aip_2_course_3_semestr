import csv
import io

source = 'name;grade\n"Анна; староста";5\n'
rows = list(csv.DictReader(io.StringIO(source), delimiter=";"))
print(rows[0]["name"])
print(int(rows[0]["grade"]) + 1)
