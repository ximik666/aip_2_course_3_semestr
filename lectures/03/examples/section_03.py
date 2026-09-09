def tokenize(text):
    chars = []
    for char in text.casefold():
        chars.append(char if char.isalpha() else " ")
    return "".join(chars).split()

print(tokenize("Кот,пёс! КОТ-2."))
