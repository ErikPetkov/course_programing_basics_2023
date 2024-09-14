times_input = int(input())
diff_sum = 0
number1 = int(input())
number2 = int(input())
sum1 = number1 + number2
max_sum = sum1
min_sum = sum1
for i in range(times_input - 1):
    number3 = int(input())
    number4 = int(input())
    sum2 = number3 + number4
    if sum2 > sum1:
        max_sum = sum2
        min_sum = sum1
    else:
        min_sum = sum2

diff_sum = abs(max_sum - min_sum)
if diff_sum == 0:
    print(f'Yes, value={sum2}')
else:
    print(f'No, maxdiff={diff_sum}')
