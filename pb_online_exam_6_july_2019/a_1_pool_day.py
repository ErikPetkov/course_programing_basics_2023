from math import ceil
br_people = int(input())
tax_enterence = float(input())
tax_shezlong = float(input())
tax_umbrela = float(input())
enterence = tax_enterence * br_people
shezlong = ceil(br_people*0.75) * tax_shezlong
umbrela = ceil(br_people*0.5) * tax_umbrela
total = enterence + shezlong + umbrela
print(f"{total:.2f} lv.")
