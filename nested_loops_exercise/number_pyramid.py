number = int(input())
curent_number = 1
same = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if number < curent_number:
            same = True
            break
        print(curent_number, end=" ")
        curent_number += 1

    if same:
        break
    print()



