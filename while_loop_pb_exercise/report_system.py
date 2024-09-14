cards_payd = 0
cash_payd = 0
people_cash = 0
people_card = 0
expected_money = int(input())
comand = input()
num = 1
total = 0
done = False
while comand != "End":
    buyd_things = int(comand)
    if num % 2 == 1:
        if buyd_things > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            people_cash += 1
            cash_payd += buyd_things
            total += buyd_things
    else:
        if buyd_things < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            people_card += 1
            cards_payd += buyd_things
            total += buyd_things
    num += 1
    if total >= expected_money:
        done = True
        break
    comand = input()
if done:
    cash_pay = cash_payd/people_cash
    cards_pay = cards_payd/people_card
    print(f"Average CS: {cash_pay:.2f}")
    print(f"Average CC: {cards_pay:.2f}")
else:
    print("Failed to collect required money for charity.")

