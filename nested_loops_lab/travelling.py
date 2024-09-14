destination = input()
while destination != "End":
    needed_money = float(input())
    money_ernd = 0
    while money_ernd < needed_money:
        money = float(input())
        money_ernd += money
    print(f"Going to {destination}!")
    destination = input()

