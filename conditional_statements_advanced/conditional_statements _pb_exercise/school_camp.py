season = input()
tipe_grup = input()
br_students = int(input())
br_nights = int(input())
price_per_student = 0
sport = ""

if tipe_grup == "boys" or tipe_grup == "girls":
    if season == "Winter":
        price_per_student = 9.6
    elif season == "Spring":
        price_per_student = 7.2
    elif season == "Summer":
        price_per_student = 15
elif tipe_grup == "mixed":
    if season == "Winter":
        price_per_student = 10
    elif season == "Spring":
        price_per_student = 9.5
    elif season == "Summer":
        price_per_student = 20

price = price_per_student * br_students * br_nights

if br_students >= 50:
    price *= 0.5
elif 50 >= br_students >= 20:
    price *= 0.85
elif 20 >= br_students >= 10:
    price *= 0.95

if tipe_grup == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif tipe_grup == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif tipe_grup == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {price:.2f} lv.")
