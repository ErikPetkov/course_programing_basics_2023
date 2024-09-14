points_float = 0
points_raw = 0
n = int(input())
while True:
    for points in range(n):
        print(f"*", end="")
    points_float = 0
    print()
    points_raw += 1
    if points_raw == n:
        break
