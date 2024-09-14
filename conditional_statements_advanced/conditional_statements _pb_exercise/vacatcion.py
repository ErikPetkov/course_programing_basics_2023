bujet = float(input())
season = input()
place = ""
location = ""
if bujet <= 1000:
    place = "Camp"
    if season == "Summer":
        bujet *= 0.65
        location = "Alaska"
    elif season == "Winter":
        bujet *= 0.45
        location = "Morocco"
elif 1000 < bujet <= 3000:
    place = "Hut"
    if season == "Summer":
        bujet *= 0.8
        location = "Alaska"
    elif season == "Winter":
        bujet *= 0.6
        location = "Morocco"
elif bujet > 3000:
    place = "Hotel"
    if season == "Summer":
        bujet *= 0.9
        location = "Alaska"
    elif season == "Winter":
        bujet *= 0.9
        location = "Morocco"
print(f"{location} - {place} - {bujet:.2f}")
