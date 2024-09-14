monney = input()
money_balance = 0
while monney != "NoMoreMoney":
    if float(monney) > 0:
        monmey = float(monney)
        money_balance += monmey
        print(f"Increase: {monmey:.2f}")
    else:
        print("Invalid operation!")
        break
    monney = input()
print(f"Total: {money_balance:.2f}")
