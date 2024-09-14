br_bought_hrizantemas = int(input())
br_bought_roses = int(input())
br_bought_laletas = int(input())
season = input()
holiday = input()
all_br_flowers = br_bought_hrizantemas+br_bought_laletas+br_bought_roses
hrizantemas = 0
roses = 0
lale = 0
if season == "Spring" or season == "Summer":
    hrizantemas = 2
    roses = 4.1
    lale = 2.5
elif season == "Autumn" or season == "Winter":
    hrizantemas = 3.75
    roses = 4.5
    lale = 4.15
buket = br_bought_hrizantemas*hrizantemas + br_bought_roses*roses + br_bought_laletas*lale
if holiday == "Y":
    buket *= 1.15
if br_bought_laletas >= 7 and season == "Spring":
    buket *= 0.95
if br_bought_laletas >= 10 and season == "Winter":
    buket *= 0.9
if all_br_flowers >= 20:
    buket *= 0.8
buket += 2
print(f"{buket:.2f}")

