number = int(input())
left=0
right = 0
for number in range(number):
    num1 = int(input())
    if number%2 == 0:
        left += num1
    else:
        right += num1
if left == right:
    print(f"Yes, sum = {left}")
else:
    diff = abs(left-right)
    print(f"No, diff = {diff}")