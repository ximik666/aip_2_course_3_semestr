def average(grades):
    return sum(grades) / len(grades) if grades else None

assert average([4, 4]) == 4
assert average([2]) == 2
assert average([]) is None
print("Обычный, граничный и пустой случаи проверены")
