years = int(input())
peralny = float(input())
price_per_toy = int(input())
toy = 0
money = 10
mony = 0
for year in range(1, years+1):
    if year % 2 == 1:
        toy += 1
    else:
        mony += money
        money += 10
total_toy_price = toy*price_per_toy
broter_take = years//2
saved_money = (mony + total_toy_price) - broter_take
diff = abs(saved_money - peralny)
if saved_money >= peralny:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
