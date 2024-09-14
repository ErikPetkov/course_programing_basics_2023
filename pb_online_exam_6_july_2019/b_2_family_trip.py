bujet = float(input())
br_nights = int(input())
price_per_one = float(input())
percent_dr = int(input())
if br_nights > 7:
    price_per_one *= 0.95
tot_nights = price_per_one * br_nights
percent_dr /= 100
percent_dr *= bujet
total = tot_nights + percent_dr
diff = abs(total-bujet)
if total > bujet:
    print(f"{diff:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
