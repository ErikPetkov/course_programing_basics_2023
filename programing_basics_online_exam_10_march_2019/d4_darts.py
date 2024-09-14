player_name = input()
points = 301
won = False
god_points = 0
bad_points = 0
terain = input()
while terain != "Retire":
    point = int(input())
    sqared = 0
    if terain == "Single":
        sqared = 1
    elif terain == "Double":
        sqared = 2
    elif terain == "Triple":
        sqared = 3
    poin = point * sqared
    if point <= poin <= points:
        points -= poin
        god_points += 1
    else:
        bad_points += 1
    if points <= 0:
        won = True
        break
    terain = input()

if won:
    print(f"{player_name} won the leg with {god_points} shots.")
else:
    print(f"{player_name} retired after {bad_points} unsuccessful shots.")
