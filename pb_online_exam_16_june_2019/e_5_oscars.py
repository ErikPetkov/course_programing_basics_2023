actor_name = input()
points = float(input())
br_refers = int(input())
enof_to_win = True

for num in range(br_refers):
    name_refer = input()
    num_leters = len(name_refer)
    points_from_refers = float(input())
    refers_points = num_leters*(points_from_refers/2)
    points += refers_points
    if points >= 1250.5:
        enof_to_win = False
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
if enof_to_win:
    print(f"Sorry, {actor_name} you need {abs(points -1250.5 ):.1f} more!")
