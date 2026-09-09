def average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

print(average([5, 4, 5]))
print(average([]))
