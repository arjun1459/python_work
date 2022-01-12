items = [
    ("p1", 23),
    ("p2", 1),
    ("p3", 4)
]

print(list(map(lambda item: item[1], items)))
print([item[1] for item in items])
# for item in x:
#     print(item)

print(list(filter(lambda item: item[1] >= 4, items)))
print([item for item in items if item[1] >= 4])
