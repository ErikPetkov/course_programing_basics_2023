from math import inf
output = input()
min_num = inf
while output != "Stop":
    number = int(output)
    if number < min_num:
        min_num = number
    output = input()
print(min_num)