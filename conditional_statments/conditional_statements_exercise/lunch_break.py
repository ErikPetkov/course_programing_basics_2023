from math import ceil
name_of_serial = input()
ep_time = int(input())
break_time = int(input())
lunch = break_time/8
rest = break_time/4
break_tim = break_time - lunch - rest
left = abs(break_tim-ep_time)
left = ceil(left)
if break_tim >= ep_time:
    print(f"You have enough time to watch {name_of_serial} and left with {left} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {left} more minutes.")
