bujet_for_actors = float(input())
actor = input()
price = 0
broke = False
while actor != "ACTION":
    if len(actor) > 15:
        bujet_for_actors *= 0.8
    elif len(actor) <= 15:
        takes = float(input())
        bujet_for_actors -= takes
    if bujet_for_actors <= 0:
        broke = True
        break
    actor = input()
if broke:
    print(f"We need {bujet_for_actors * -1:.2f} leva for our actors.")
else:
    print(f"We are left with {bujet_for_actors:.2f} leva.")