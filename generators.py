first_dict = {"x": 1}
second_dict = {"x": 12, "y": 2}
combined = {**first_dict, **second_dict}
print(combined)

# from sys import getsizeof
# values = (x*2 for x in range(10000000))
# print(getsizeof(values))

# values = [x*2 for x in range(10000000)]
# print(getsizeof(values))

# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers)

# values = [*range(5)]
# print(values)
