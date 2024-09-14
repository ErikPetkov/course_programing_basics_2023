needed_money_for_trip = float(input())
bujet_now = float(input())
only_spend = 0
only_sp = False
days = 0
while bujet_now < needed_money_for_trip:
    tipe_done = input()
    money = float(input())
    days += 1
    if tipe_done == "spend":
        bujet_now -= money
        only_spend += 1
    elif tipe_done == "save":
        bujet_now += money
        only_spend = 0
    if bujet_now <= 0:
        bujet_now = 0
    if only_spend >= 5:
        only_sp = True
        break
if only_sp:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
