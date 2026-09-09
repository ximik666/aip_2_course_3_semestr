def top_words(counts, limit):
    if limit <= 0:
        return []
    pairs = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return pairs[:limit]

print(top_words({"пёс": 2, "кот": 3, "дом": 2}, 2))
