win = 0
lost = 0
draw = 0
for match in range(3):
    game1 = input()
    team1 = game1[0]
    team2 = game1[2]

    if team1 > team2:
        win += 1
    elif team1 < team2:
        lost += 1
    else:
        draw += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")
