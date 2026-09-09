def passing(grades, minimum=3):
    result = []
    for grade in grades:
        if grade >= minimum:
            result.append(grade)
    return result

print(passing([2, 3, 4, 5]))
print(passing([2, 3, 4, 5], minimum=4))
