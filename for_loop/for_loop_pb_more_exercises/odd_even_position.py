from math import inf

number = int(input())
odd_nums = 0
even_nums = 0
big_odd = -inf
min_odd = inf
big_even = -inf
min_even = inf
for _ in range(number):
    num = float(input())
    if num % 2 == 1:
        odd_nums += 1
        if num > big_odd:
            big_odd = num
        if num < min_odd:
            min_odd = num
    elif num % 2 == 0:
        even_nums += 1
        if num > big_even:
            big_even = num
        if num < min_even:
            min_even = num
print(f"OddSum={odd_nums:.2f},")
if big_odd == -inf:
    print("No")
else:
    print(f"OddMin={min_odd:.2f},")
if min_odd == inf:
    print("No")
else:
    print(f"OddMax={big_odd:.2f},")

print(f"EvenSum={even_nums:.2f},")
if big_even == -inf:
    print("No")
else:
    print(f"EvenMin={min_even:.2f},")
if min_even == inf:
    print("No")
else:
    print(f"EvenMax={big_even:.2f}")
