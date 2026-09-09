def frequencies(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

words = ["кот", "кот", "пёс"]
counts = frequencies(words)
print(counts)
print(len(words), len(counts))
