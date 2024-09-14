n_br_kilometers = int(input())
part_of_the_day = input()
taksi = False
price = 0
price_per_km = 0

if n_br_kilometers >= 100:
    price_per_km = 0.06

elif n_br_kilometers >= 20:
    price_per_km = 0.09
else:
    taksi = True
    if part_of_the_day == "day":
        price_per_km = 0.79
    else:
        price_per_km = 0.9
if taksi == True:
    price = 0.70 + price_per_km * n_br_kilometers
else:
    price = price_per_km * n_br_kilometers
    
print(f"{price:.2f}")

