price_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
br_eggs = int(input())
br_maq = int(input())
sugar_price = price_flour * 0.75
eggs_price = price_flour * 1.1
price_maq = sugar_price * 0.2
sum_flour = price_flour * kg_flour
sum_sugar = sugar_price * kg_sugar
sum_eggs = eggs_price * br_eggs
sum_maq = br_maq * price_maq
total = sum_maq + sum_sugar + sum_eggs + sum_flour
print(f"{total:.2f}")
