# SQALPAT
number = int(input())
# seq = 0
# # numbers = [i for i in (range(number*5))]
# # print(numbers)
for num in range(0, number*5, 5):
    if num % 2 == 0:
        for i in range(num, num+5):
            print(i+1, end=" ")
    else:
        for i in range(num+5, num, -1):
            print(i, end=" ")
    print("")
