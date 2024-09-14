count = int(input())
leftSum = 0
rightSum = 0

for i in range(count):
    leftSum += int(input())

for i in range(count):
    rightSum += int(input())

if leftSum == rightSum:
    print(f"Yes, sum = {leftSum}")
else:
    print(f"No, diff = {abs(leftSum - rightSum)}")

# n = int(input())

# left_sum = 0
# right_sum = 0

# for _ in range(n):
    # left_sum += int(input())

# for _ in range(n):
    # right_sum += int(input())

#if left_sum == right_sum:
#    print(f"Yes, sum = {left_sum}")

#else:
#    diff = abs(left_sum - right_sum)
#    print(f"No, diff = {diff}")
