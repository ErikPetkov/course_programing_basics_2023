fruit = input()
day = input()
br = float(input())
price_per_one = 0
error = 0
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price_per_one = 2.5
    elif fruit == "apple":
        price_per_one = 1.2
    elif fruit == "orange":
        price_per_one = 0.85
    elif fruit == "grapefruit":
        price_per_one = 1.45
    elif fruit == "kiwi":
        price_per_one = 2.7
    elif fruit == "pineapple":
        price_per_one = 5.5
    elif fruit == "grapes":
        price_per_one = 3.85
    else:
         error += 1
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price_per_one = 2.7
    elif fruit == "apple":
        price_per_one = 1.25
    elif fruit == "orange":
        price_per_one = 0.9
    elif fruit == "grapefruit":
        price_per_one = 1.6
    elif fruit == "kiwi":
        price_per_one = 3
    elif fruit == "pineapple":
        price_per_one = 5.6
    elif fruit == "grapes":
        price_per_one = 4.2
    else:
        error = 1
else:
    error = 1
if error == 0:
    total_price = br * price_per_one
    print(f"{total_price:.2f}")
else:
    print("error")

