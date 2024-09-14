from math import floor,ceil
magnoli = 3.25
zumbuli = 4
roses = 3.5
kaktus = 8

br_magnoli = int(input())
br_zumbuli = int(input())
br_roses = int(input())
br_kaktus = int(input())
price_for_the_gift = float(input())

price_magnoli = br_magnoli * magnoli
price_zumbuli = br_zumbuli * zumbuli
price_roses = br_roses * roses
price_kaktus = br_kaktus * kaktus
bill = price_magnoli + price_zumbuli + price_roses + price_kaktus
bill_with_ddc = bill*0.95
diferense = abs(bill_with_ddc - price_for_the_gift)
if bill_with_ddc >= price_for_the_gift:
    print(f"She is left with {floor(diferense)} leva.")
else:
    print(f"She will have to borrow {ceil(diferense)} leva.")

