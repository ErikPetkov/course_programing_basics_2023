n = int(input())
i = 0
for number in range(1111, 9999 + 1):
    number = str(number)
    for index, digit in enumerate(number):
        if int(digit) == 0 or n % int(digit) != 0:
            break
        else:
            i += 1
    if i == 4:
        print(number, end=" ")
    i = 0

