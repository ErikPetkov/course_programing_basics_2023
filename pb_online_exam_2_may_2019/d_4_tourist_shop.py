bujet = float(input())
counter = 0
d_counter = 0
ting = input()
enought = True
tot_p = 0
while ting != "Stop":
    price = float(input())
    counter += 1
    d_counter += 1
    if d_counter == 3:
        price *= 0.5
        d_counter = 0
    if bujet < price:
        enought = False
        break
    bujet -= price
    tot_p += price
    ting = input()
if enought:
    print(f"You bought {counter} products for {tot_p:.2f} leva.")
else:
    print("You don't have enough money!")
    diff = abs(price - bujet)
    print(f"You need {diff:.2f} leva!")
