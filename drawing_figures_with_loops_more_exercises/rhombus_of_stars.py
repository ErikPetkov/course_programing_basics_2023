n = int(input())
i = 1
while True:
    if i == n:
        break
    for row in range(i):
        print("*", end=" ")
    print()
    i += 1
