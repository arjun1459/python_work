from typing import ValuesView


values = []

for i in range(10):
    values.append(i*2)

x = [num*2 for num in range(10)]

print(values)
print(x)

set_ex = {x*2 for x in range(5)}
print(set_ex)

dict_ex = {x: x*2 for x in range(5)}
print(dict_ex)
