pens = 5.8
markers = 7.2
preparat = 1.2
br_pens = int(input())
br_markers = int(input())
br_preparat = int(input())
br_discount = int(input())
all_pens = pens*br_pens
all_markers = markers * br_markers
all_preparat = preparat * br_preparat
all_things = all_pens+all_preparat+all_markers
price_with_discount= all_things-(all_things*(br_discount/100))
print(price_with_discount)