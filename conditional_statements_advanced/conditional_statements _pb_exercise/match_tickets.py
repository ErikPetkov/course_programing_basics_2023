bujet = float(input())
type_bilets = input()
grup = int(input())
price_tiket = 0
trip = 0
if type_bilets == "VIP":
    price_tiket = 499.99
elif type_bilets == "Normal":
    price_tiket = 249.99
if grup <= 4:
    trip = 0.25
elif 5 <= grup <= 9:
    trip = 0.4
elif 10 <= grup <= 24:
    trip = 0.5
elif 25 <= grup <= 49:
    trip = 0.6
elif grup >= 50:
    trip = 0.75
bujet *= trip
tikets = price_tiket*grup
if bujet >= tikets:
    print(f"Yes! You have {(bujet - tikets):.2f} leva left.")
else:
    print(f"Not enough money! You need {(tikets-bujet):.2f} leva.")

