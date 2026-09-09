def parse_grade(text):
    value = int(text.strip())
    if not 2 <= value <= 5:
        raise ValueError("Оценка вне диапазона")
    return value

for text in [" 4 ", "пять", "6"]:
    try:
        print(parse_grade(text))
    except ValueError:
        print("Введите целое число от 2 до 5")
