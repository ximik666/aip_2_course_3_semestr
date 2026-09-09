def count_debts(grades):
    return grades.count(2)

assert count_debts([]) == 0
assert count_debts([3, 4, 5]) == 0
assert count_debts([2, 5, 2]) == 2
print("3 проверки выполнены")
