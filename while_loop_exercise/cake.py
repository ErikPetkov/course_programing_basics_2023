tall = int(input())
long = int(input())
stoped = False
total_taken = 0
total_cake = tall * long
while total_cake >= 0:
    taken = input()
    last = 0
    if taken == "STOP":
        stoped = True
        break
    else:
        total_taken += int(taken)
        total_cake -= int(taken)
        last = abs(total_cake - int(taken))
diff = abs(total_taken)
if stoped:
    print(f"{total_cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_cake)} pieces more.")
