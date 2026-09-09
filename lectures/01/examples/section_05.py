def with_grade(grades, grade):
    result = grades.copy()
    result.append(grade)
    return result

original = [4, 5]
updated = with_grade(original, 3)
print(original)
print(updated)
