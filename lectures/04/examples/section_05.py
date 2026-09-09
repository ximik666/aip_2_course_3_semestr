import csv
import io

stream = io.StringIO(newline="")
writer = csv.DictWriter(stream, fieldnames=["name", "average"], delimiter=";")
writer.writeheader()
writer.writerow({"name": "Анна", "average": f"{14 / 3:.2f}"})
print(stream.getvalue(), end="")
