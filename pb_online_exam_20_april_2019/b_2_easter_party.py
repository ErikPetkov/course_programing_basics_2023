br_gests = int(input())
price_per_person = float(input())
bujet = float(input())
discount = 1
if 10 <= br_gests <= 15:
    discount = 0.85
elif 15 < br_gests <= 20:
    discount = 0.8
elif 20 < br_gests:
    discount = 0.75

price_per_person *= discount
cake = bujet * 0.1
total = br_gests * price_per_person + cake
diff = abs(total-bujet)
if total <= bujet:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
