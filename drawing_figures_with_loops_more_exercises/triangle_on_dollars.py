rows = int(input())
coloms = 1
for i in range(rows):
    for _ in range(coloms):
        print("$", end=" ")
    print()
    coloms += 1
        