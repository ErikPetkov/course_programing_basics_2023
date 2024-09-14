gaved_money = float(input())
year_to_live = int(input())
year_in_range = 1800
age = 18
lost_money = True
money = 0

for year_in_range in range(year_in_range, year_to_live+1):

    if year_in_range % 2 == 0:
        gaved_money -= 12000

    else:
        spend_for_year = 12000 + 50 * age
        gaved_money -= spend_for_year
    age += 1
    if gaved_money < 0:
        lost_money = False

if lost_money:
    print(f"Yes! He will live a carefree life and will have {gaved_money:.2f} dollars left.")
else:
    left = abs(abs(gaved_money))
    print(f"He will need {left:.2f} dollars to survive.")
