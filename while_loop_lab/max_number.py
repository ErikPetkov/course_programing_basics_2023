from math import inf
output = input()
max_num = -inf
while output != "Stop":
    number = int(output)
    if number > max_num:
        max_num = number
    output = input()
print(max_num)