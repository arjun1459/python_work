def multyply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total



print(multyply(1, 2, 3, 4, 5))
