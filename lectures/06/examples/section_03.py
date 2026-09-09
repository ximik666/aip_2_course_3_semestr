class Student:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя не может быть пустым")
        self.name = " ".join(name.split())

print(Student("  Анна   Иванова ").name)
try:
    Student(" ")
except ValueError:
    print("Пустое имя отклонено")
