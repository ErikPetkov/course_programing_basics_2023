price_maze = 2.6
price_talk_dog = 3
price_bear = 4.1
price_minion = 8.2
price_truk = 2
trip_cost = float(input())
br_maze = int(input())
br_doll = int(input())
br_bear = int(input())
br_minions = int(input())
br_truk = int(input())
maze = price_maze*br_maze
doll = price_talk_dog*br_doll
bear = price_bear*br_bear
minion = price_minion*br_minions
truk = price_truk*br_truk
br_toys = br_maze+br_doll+br_bear+br_minions+br_truk
price = maze+doll+bear+minion+truk
if br_toys >= 50:
    price *= 0.75
price *= 0.9
left_money = abs(price-trip_cost)
if price >= trip_cost:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")

