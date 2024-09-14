fitnes_visitors = int(input())
back = 0
chest = 0
legs = 0
abc = 0
protein_shake = 0
protein_bar = 0
buyd_shake = 0
buyd_bar = 0

for person in range(fitnes_visitors):
    thing = input()

    if thing == "Back":
        back += 1
    elif thing == "Chest":
        chest += 1
    elif thing == "Legs":
        legs += 1
    elif thing == "Abs":
        abc += 1
    elif thing == "Protein shake":
        protein_shake += 1
        buyd_shake += 1
    elif thing == "Protein bar":
        protein_bar += 1
        buyd_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abc} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")

percent_train = ((back + chest + legs + abc) / fitnes_visitors) * 100
percent_buied = ((protein_bar + protein_shake) / fitnes_visitors) * 100

print(f"{percent_train:.2f}% - work out")
print(f"{percent_buied:.2f}% - protein")
