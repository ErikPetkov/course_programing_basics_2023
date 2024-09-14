bujet = float(input())
l_fuel = float(input())
day = input()
fuel_price = 2.1 * l_fuel
total_out_d = fuel_price + 100
if day == "Sunday":
    total = total_out_d * 0.8
elif day == "Saturday":
    total = total_out_d * 0.9
diff = abs(bujet - total)
if bujet >= total:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
