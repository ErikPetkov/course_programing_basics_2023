seasons = input()
km_on_mount = float(input())
price_per_km = 1

if km_on_mount <= 5000:
    if seasons == "Spring" or seasons == "Autumn":
        price_per_km = 0.75
    elif seasons == "Summer":
        price_per_km = 0.9
    elif seasons == "Winter":
        price_per_km = 1.05
elif 5000 < km_on_mount <= 10000:
    if seasons == "Spring" or seasons == "Autumn":
        price_per_km = 0.95
    elif seasons == "Summer":
        price_per_km = 1.1
    elif seasons == "Winter":
        price_per_km = 1.25
elif 10000 < km_on_mount <= 20000:
    price_per_km = 1.45

price_per_momth = km_on_mount * price_per_km
price_per_momth *= 4
price_per_momth *= 0.9

print(f"{price_per_momth:.2f}")
