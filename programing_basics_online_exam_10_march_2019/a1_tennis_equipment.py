from math import floor, ceil
price_on_one_rocket = float(input())
br_rokets = int(input())
br_shoes = int(input())
one_shoes = price_on_one_rocket / 6
total_rokets = br_rokets * price_on_one_rocket
total_shoes = br_shoes * one_shoes
other_equipment = (total_rokets + total_shoes) * 0.2
total = other_equipment + total_shoes + total_rokets
djocovish_pays = total / 8
sponsors = djocovish_pays * 7
print(f"Price to be paid by Djokovic {floor(djocovish_pays)}")
print(f"Price to be paid by sponsors {ceil(sponsors)}")

