try:
    grade = int("пять")
except ValueError as error:
    print(type(error).__name__)
    print("Нужно целое число, например 5")
