from math import floor
br_tournaments = int(input())
start_points = int(input())

won_tornaments = 0
points = 0

for tournament in range(br_tournaments):
    stage = input()
    if stage == "W":
        won_tornaments += 1
        points += 2000
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

total_points = points + start_points
average_points = points / br_tournaments
persent_won = won_tornaments / br_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{persent_won:.2f}%")

