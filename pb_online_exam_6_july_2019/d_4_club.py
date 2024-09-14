needed_earnings = float(input())
drink = input()
earned = 0
while drink != "Party!":
    br_drinks = int(input())
    cost = len(drink)
    price = cost * br_drinks
    if (price % 10) % 2 == 1:
        price *= 0.75
    earned += price
    drink = input()
if needed_earnings == earned:
    print("Target acquired.")
else:
    print(f"We need {(needed_earnings - earned):.2f} leva more.")
print(f"Club income - {earned:.2f} leva.")
