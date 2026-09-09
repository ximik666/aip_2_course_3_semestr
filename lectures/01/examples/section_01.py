def count_debts(grades):
    count = 0
    for grade in grades:
        if grade == 2:
            count += 1
    return count

print(count_debts([5, 2, 4, 2]))
