bujet = float(input())
season = input()
place_to_go = ""
tipe_rest = ""
spend_money = 0
if bujet <= 100:
    place_to_go = "Bulgaria"
    if season == "summer":
        tipe_rest = "Camp"
        spend_money = bujet * 0.3
    else:
        tipe_rest = "Hotel"
        spend_money = bujet * 0.7
elif bujet <= 1000:
    place_to_go = "Balkans"
    if season == "summer":
        tipe_rest = "Camp"
        spend_money = bujet * 0.4
    else:
        tipe_rest = "Hotel"
        spend_money = bujet * 0.8
elif bujet >= 1000:
    tipe_rest = "Hotel"
    place_to_go = "Europe"
    spend_money = bujet * 0.9

print(f"Somewhere in {place_to_go}")
print(f"{tipe_rest} - {spend_money:.2f}")
