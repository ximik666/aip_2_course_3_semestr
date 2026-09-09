def format_average(value):
    if value is None:
        return "нет оценок"
    return f"{value:.2f}"

result = format_average(14 / 3)
print("Средний балл:", result)
print(format_average(None))
