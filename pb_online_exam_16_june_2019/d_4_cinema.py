capasiti_teatre = int(input())
tim = False
money = 0
while capasiti_teatre > -1:
    br_people = input()

    if br_people == "Movie time!":
        tim = True
        break
    if int(br_people) > capasiti_teatre:
        break
    elif int(br_people) % 3 == 0:
        money -= 5
    money += int(br_people) * 5
    capasiti_teatre -= int(br_people)

if tim:
    print(f"There are {capasiti_teatre} seats left in the cinema.")
else:
    print("The cinema is full.")
print(f"Cinema income - {money} lv.")
