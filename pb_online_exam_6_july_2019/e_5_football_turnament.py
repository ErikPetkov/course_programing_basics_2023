team_name = input()
br_season_matches = int(input())

points = 0
w = 0
d = 0
l = 0

for match in range(br_season_matches):
    stats = input()
    if stats == "W":
        points += 3
        w += 1
    elif stats == "D":
        points += 1
        d += 1
    elif stats == "L":
        l += 1

if br_season_matches > 0:
    win_rate = w / br_season_matches * 100
    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {win_rate:.2f}%")

elif br_season_matches == 0:
    print(f"{team_name} hasn't played any games during this season.")