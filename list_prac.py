items = [
    ("p1", 23),
    ("p2", 1),
    ("p3", 4)
]

prices = []

for item in items:
    prices.append(item[1])
print(prices)

x = list(map(lambda item: item[1], items))
print(x)

#fil = list(filter(lambda item: item[1] > 1, items))
fil = [item for item in items if item[1] > 1]
print(fil)
