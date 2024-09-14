rows = int(input())
line = rows
curent_row = 0
for _ in range(rows):
    sim = 0
    for _ in range(line):
        if curent_row == 0 and sim == 0 or curent_row == 0 and sim == line-1:
            print("+", end=" ")
        elif curent_row == rows-1 and sim == 0 or curent_row == rows-1 and sim == line-1:
            print("+", end=" ")
        elif sim == 0 or sim == line-1:
            print("|", end=" ")
        else:
            print("-", end=" ")
        sim += 1
    print()
    curent_row += 1
