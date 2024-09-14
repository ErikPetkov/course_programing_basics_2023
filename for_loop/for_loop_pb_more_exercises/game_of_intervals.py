moves_of_game = int(input())
invalid_move = 0
mov = 0
to_9 = 0
to_19 = 0
to_29 = 0
to_39 = 0
to_50 = 0

for moves in range(moves_of_game):
    move = int(input())
    if 0 <= move <= 9:
        move *= 0.2
        mov += move
        to_9 += 1
    elif 10 <= move <= 19:
        move *= 0.3
        mov += move
        to_19 += 1
    elif 20 <= move <= 29:
        move *= 0.4
        mov += move
        to_29 += 1
    elif 30 <= move <= 39:
        mov += 50
        to_39 += 1
    elif 40 <= move <= 50:
        mov += 100
        to_50 += 1
    else:
        mov /= 2
        invalid_move += 1
percent_to_9 = to_9 / moves_of_game * 100
percent_to_19 = to_19 / moves_of_game * 100
percent_to_29 = to_29 / moves_of_game * 100
percent_to_39 = to_39 / moves_of_game * 100
percent_to_50 = to_50 / moves_of_game * 100
percent_to_inv = invalid_move / moves_of_game * 100
print(f"{mov:.2f}")
print(f"From 0 to 9: {percent_to_9:.2f}%")
print(f"From 10 to 19: {percent_to_19:.2f}%")
print(f"From 20 to 29: {percent_to_29:.2f}%")
print(f"From 30 to 39: {percent_to_39:.2f}%")
print(f"From 40 to 50: {percent_to_50:.2f}%")
print(f"Invalid numbers: {percent_to_inv:.2f}%")

