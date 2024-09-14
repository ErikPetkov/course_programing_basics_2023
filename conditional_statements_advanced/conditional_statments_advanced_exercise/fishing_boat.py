buget = int(input())
season = input()
br_fishermans = int(input())
boat_rent = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if br_fishermans <= 6:
    boat_rent *= 0.9
elif br_fishermans <= 11:
    boat_rent *= 0.85
elif br_fishermans >= 12:
    boat_rent *= 0.75
if br_fishermans % 2 == 0 and season != "Autumn":
    boat_rent *= 0.95
differense = abs(buget-boat_rent)
if buget >= boat_rent:
    print(f"Yes! You have {differense:.2f} leva left.")
else:
    print(f"Not enough money! You need {differense:.2f} leva.")
