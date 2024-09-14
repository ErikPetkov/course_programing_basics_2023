br_people = int(input())
season = input()
price_per_person = 0
if br_people <= 5:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.5
    elif season == "autumn":
        price_per_person = 60
    elif season == "winter":
        price_per_person = 86
elif br_people > 5:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.5
    elif season == "winter":
        price_per_person = 85

total_sum = br_people * price_per_person

if season == "summer":
    total_sum *= 0.85
if season == "winter":
    total_sum *= 1.08

print(f"{total_sum:.2f} leva.")
