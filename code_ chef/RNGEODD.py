start, end = map(int, input().split())
for i in range(start, end+1):
    if i % 2 == 1:
        print(i, end=" ")
