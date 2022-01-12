# REVSTRPT
number = int(input())

for i in range(number-1):
    for _ in range(i, number):
        print("* ", end="")
    print("\n")
