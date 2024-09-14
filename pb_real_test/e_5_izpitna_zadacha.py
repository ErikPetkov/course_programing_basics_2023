br_sea_pakets = int(input())
br_mounten_pakets = int(input())
paket = input()
profit = 0
all_sold = False
while paket != "Stop":

    if paket == "sea":
        if br_sea_pakets > 0:
            br_sea_pakets -= 1
            profit += 680
    elif paket == "mountain":
        if br_mounten_pakets > 0:
            br_mounten_pakets -= 1
            profit += 499

    if br_mounten_pakets == 0 and br_sea_pakets == 0:
        all_sold = True
        break
    paket = input()
if all_sold:
    print(" Good job! Everything is sold.")
print(f"Profit: {profit} leva.")
