time = int(input())
day_of_week = input()
shop = ""
if 10 <= time <= 18:
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday":
        shop = "open"
    elif day_of_week == "Sunday":
        shop = "closed"
else:
    shop = "closed"
print(f"{shop}")


