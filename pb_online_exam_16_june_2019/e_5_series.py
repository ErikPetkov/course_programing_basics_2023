bujet = float(input())
br_serials = int(input())
price = 0
for i in range(br_serials):
    name = input()
    price_per_serial = float(input())
    if name == "Thrones":
        price_per_serial *= 0.5
    elif name == "Lucifer":
        price_per_serial *= 0.6
    elif name == "Protector":
        price_per_serial *= 0.7
    elif name == "TotalDrama":
        price_per_serial *= 0.8
    elif name == "Area":
        price_per_serial *= 0.9
    price += price_per_serial
diff = abs(price - bujet)
if price <= bujet:
    print(f"You bought all the series and left with {diff:.2f} lv.")
elif price > bujet:
    print(f"You need {diff:.2f} lv. more to buy the series!")
