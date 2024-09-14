br_seld_games = int(input())
h = 0
f = 0
ov = 0
ot = 0
for game in range(br_seld_games):
    game_n = input()
    if game_n == "Hearthstone":
        h += 1
    elif game_n == "Fornite":
        f += 1
    elif game_n == "Overwatch":
        ov += 1
    else:
        ot += 1
pr_h = h / br_seld_games * 100
pr_f = f / br_seld_games * 100
pr_ov = ov / br_seld_games * 100
pr_ot = ot / br_seld_games * 100
print(f"Hearthstone - {pr_h:.2f}%")
print(f"Fornite - {pr_f:.2f}%")
print(f"Overwatch - {pr_ov:.2f}%")
print(f"Others - {pr_ot:.2f}%")
