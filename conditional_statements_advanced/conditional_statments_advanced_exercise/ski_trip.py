days = int(input())
type_room = input()
grade = input()

price_for_night = 0
nights = days-1
discount = 0
price_with_discount = 0

if type_room == "room for one person":
    price_for_night = 18
    discount = 1
elif type_room == "apartment":
    price_for_night = 25
    if days < 10:
        discount = 0.7
    elif 10 <= days <= 15:
        discount = 0.65
    elif days > 15:
        discount = 0.5
elif type_room == "president apartment":
    price_for_night = 35
    if days < 10:
        discount = 0.9
    elif 10 <= days <= 15:
        discount = 0.85
    elif days > 15:
        discount = 0.8

price = price_for_night * nights
price_with_discount = price * discount
if grade == "positive":
    price_with_discount *= 1.25
elif grade == "negative":
    price_with_discount *= 0.9
print(f"{price_with_discount:.2f}")


