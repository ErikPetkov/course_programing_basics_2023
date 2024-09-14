from math import floor
br_tournaments = int(input())
br_points_in_start = int(input())
total_points = 0
won = 0

for num in range(br_tournaments):
    place_on_turnament = input()
    if place_on_turnament == "SF":
        total_points += 720
    elif place_on_turnament == "F":
        total_points += 1200
    elif place_on_turnament == "W":
        total_points += 2000
        won += 1
averege_points_per_tournament = total_points//br_tournaments
total_points += br_points_in_start
percent = (won/br_tournaments)*100
print(f"Final points: {total_points}")
print(f"Average points: {floor(averege_points_per_tournament)}")
print(f"{percent:.2f}%")


