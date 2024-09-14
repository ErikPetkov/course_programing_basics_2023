max_gran1 = int(input())
max_gran2 = int(input())
max_gran3 = int(input())
num = 0
num1 = 0
num2 = 0
num3 = 0
n = 0
while num1 % 2 == 0:
    for num1 in range(2, max_gran1):
        if num1 % 2 == 0 and num1 <= max_gran1:
            print(num1, end=" ")
    for num2 in range(1, max_gran2):
        if num == 0 or num2 % num == 0:
            n += 1
        if n > 1:
            print(num2, end=" ")
        num += 1
    for num3 in range(2, max_gran3):
        if num3 % 2 == 0 and num3 <= max_gran3:
            print(num3)
