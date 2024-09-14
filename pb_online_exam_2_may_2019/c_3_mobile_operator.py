br_years = input()
pceje = input()
mobil_internet = input()
monts_pay = int(input())

tax = 0
discount = 1

if br_years == "one":
    if pceje == "Small":
        tax = 9.98
    elif pceje == "Middle":
        tax = 18.99
    elif pceje == "Large":
        tax = 25.98
    elif pceje == "ExtraLarge":
        tax = 35.99
elif br_years == "two":
    discount = 0.9625
    if pceje == "Small":
        tax = 8.58
    elif pceje == "Middle":
        tax = 17.09
    elif pceje == "Large":
        tax = 23.59
    elif pceje == "ExtraLarge":
        tax = 31.79

if mobil_internet == "yes":
    if tax <= 10:
        tax += 5.5
    elif tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85
        
tax *= discount
total = tax * monts_pay
print(f"{total:.2f} lv.")
