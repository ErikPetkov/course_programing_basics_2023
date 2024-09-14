starting_num = int(input())
last_interval = int(input())
magik_num = int(input())
comb = 0
found = False
for num_1 in range(starting_num, last_interval + 1):
    for num_2 in range(starting_num, last_interval + 1):
        comb += 1
        if num_1 + num_2 == magik_num:
            found = True
            break
    if found:
        break
if found:
    print(f"Combination N:{comb} ({num_1} + {num_2} = {magik_num})")
else:
    print(f"{comb} combinations - neither equals {magik_num}")
