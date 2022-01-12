# DIFACTRS
number = int(input())
factors = []
for i in range(1, number+1):
    if number % i == 0:
        factors.append(i)
print(len(factors))
print(*factors)
