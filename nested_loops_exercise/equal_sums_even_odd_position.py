low_num = int(input())
max_num = int(input())
for num in range(low_num, max_num + 1):
    nun = str(num)
    odd = 0
    even = 0
    for index, digit in enumerate(nun):
        if index % 2 == 0:
            odd += int(digit)
        else:
            even += int(digit)
    if even == odd:
        print(num, end=" ")

