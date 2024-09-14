month = input()
br_nights = int(input())
studeo = 0
apartment = 0
if month == "May" or month == "October":
    studeo = 50
    apartment = 65
    if 7 < br_nights <= 14 and studeo != 0:
        studeo *= 0.95
        apartment *= 0.95
    elif br_nights > 14 and studeo != 0:
        studeo *= 0.7
        apartment *= 0.9
elif month == "June" or month == "September":
    studeo = 75.2
    apartment = 68.7
    if br_nights > 14 and studeo != 0:
        studeo *= 0.8
        apartment *= 0.9
elif month == "July" or month == "August":
    studeo = 76
    apartment = 77
    if br_nights > 14 and studeo != 0:
        studeo *= 1
        apartment *= 0.9
studeo *= br_nights
apartment *= br_nights
print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studeo:.2f} lv.")
