film_bujet = float(input())
destination = input()
seasson = input()
br_days = int(input())
price_per_day = 0
if destination == "Dubai":
    if seasson == "Winter":
        price_per_day = 45000
    elif seasson == "Summer":
        price_per_day = 40000
elif destination == "Sofia":
    if seasson == "Winter":
        price_per_day = 17000
    elif seasson == "Summer":
        price_per_day = 12500
elif destination == "London":
    if seasson == "Winter":
        price_per_day = 24000
    elif seasson == "Summer":
        price_per_day = 20250

price = br_days * price_per_day
if destination == "Dubai":
    price *= 0.7
elif destination == "Sofia":
    price *= 1.25
diff = abs(film_bujet - price)
if film_bujet >= price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
