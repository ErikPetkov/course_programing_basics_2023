p1_name = input()
p2_name = input()
p1_turn = input()
p2_turn = input()

p1_points = 0
p2_points = 0
end_of_game = True

while p1_turn != "End of game" and p2_turn != "End of game":

    p1_card = int(p1_turn)
    p2_card = int(p2_turn)

    if p1_card == p2_card:
        p1_card = int(input())
        p2_card = int(input())
        print("Number wars!")
        end_of_game = False
        if p1_card > p2_card:
            print(f"{p1_name} is winner with {p1_points} points")
            break
        elif p1_card < p2_card:
            print(f"{p2_name} is winner with {p2_points} points")
            break

    elif p1_card > p2_card:
        p1_points += p1_card - p2_card

    elif p1_card < p2_card:
        p2_points += p2_card - p1_card

    if end_of_game:
        p1_turn = input()
        if p1_turn != "End of game":
            p2_turn = input()

if end_of_game:
    print(f"{p1_name} has {p1_points} points")
    print(f"{p2_name} has {p2_points} points")
