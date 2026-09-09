steps = ["Проверить версию Python",
         "Перейти в каталог с папкой journal",
         "Выполнить python -m journal",
         "Выполнить публичные и собственные тесты"]
for index, step in enumerate(steps, 1):
    print(f"{index}. {step}")
