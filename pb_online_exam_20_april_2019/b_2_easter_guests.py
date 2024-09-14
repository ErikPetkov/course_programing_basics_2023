from math import ceil
br_gests = int(input())
bujet = int(input())

bread = ceil(br_gests/3)
eggs = br_gests * 2
price_bread = bread * 4
price_eggs = eggs * 0.45
total = price_bread + price_eggs
diff = abs(total - bujet)
if total <= bujet:
    print(f"Lyubo bought {bread} Easter bread "
          f"and {eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
