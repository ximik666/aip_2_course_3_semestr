def average(grades):
    return sum(grades) / len(grades) if grades else None

def summary(grades):
    return {"count": len(grades),
            "average": average(grades),
            "debt": 2 in grades}

print(summary([2, 4, 5]))
