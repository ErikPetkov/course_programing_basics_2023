months = int(input())
water = 20
internet = 15
total_water = 0
total_internet = 0
total_tok = 0
total_other = 0
other = 0
for mount in range(months):
    tok_for_mount = float(input())
    total_tok += tok_for_mount
    other = (tok_for_mount + water + internet) * 1.2
    total_other += other
total_water = water * months
total_internet = internet * months
average = (total_tok + total_water + total_internet + total_other)/months
print(f"Electricity: {total_tok:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average:.2f} lv")


