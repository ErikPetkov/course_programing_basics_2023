br_bread = int(input())
br_eggs = int(input())
br_biscuit = int(input())

total_bread = br_bread * 3.2
total_eggs = br_eggs * 4.35
total_biscuit = br_biscuit * 5.4
total_paint = br_eggs * 12 * 0.15
total = total_paint + total_eggs + total_bread + total_biscuit
print(f"{total:.2f}")