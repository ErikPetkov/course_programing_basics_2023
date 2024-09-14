woned_matches = 0
lost_matches = 0
matches = 0
name_of_turnament = input()

while name_of_turnament != "End of tournaments":
    br_matches_per_toutnament = int(input())
    for n in range(1, br_matches_per_toutnament + 1):
        desi_team = int(input())
        enemy_team = int(input())
        matches += 1
        diff = abs(desi_team - enemy_team)
        if desi_team > enemy_team:
            woned_matches += 1
            print(f"Game {n} of tournament ", end="")
            print(f"{name_of_turnament}: win with {diff} points.")
        elif enemy_team > desi_team:
            lost_matches += 1
            print(f"Game {n} of tournament {name_of_turnament}: lost with {diff} points.")
    name_of_turnament = input()

percent_won = woned_matches / matches * 100
percent_lost = lost_matches / matches * 100

print(f"{percent_won:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")
