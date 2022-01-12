test_cases = int(input())
numbers = list(map(int, input().split()))
numbers.reverse()
# print(numbers)
for number in numbers:
    print(number, end=" ")
