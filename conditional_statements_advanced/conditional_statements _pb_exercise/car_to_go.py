buget = float(input())
season = input()
car = ""
tipe = ""
if buget <= 100:
    tipe = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        buget *= 0.35
    elif season == "Winter":
        car = "Jeep"
        buget *= 0.65
elif 100 < buget <= 500:
    tipe = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        buget *= 0.45
    elif season == "Winter":
        car = "Jeep"
        buget *= 0.8
elif buget > 500:
    tipe = "Luxury class"
    car = "Jeep"
    buget *= 0.9
print(f"{tipe}")
print(f"{car} - {buget:.2f}")
