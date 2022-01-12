points = {"x": 1, "y": 2}
print(points)
points = dict(x=1, y=2)
points["z"] = 3
print(points.get("a", "not here"))


for key in points:
    print(key, points[key])

for key, value in points.items():
    print(key, value)
