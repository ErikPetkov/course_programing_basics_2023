screen_type = input ()
rows = int(input())
coloms = int(input())
price_per_one = 0
seats = rows * coloms
if screen_type == "Premiere":
    price_per_one = 12
elif screen_type == "Normal":
    price_per_one = 7.5
elif screen_type == "Discount":
    price_per_one = 5
price = seats * price_per_one
print(f"{price:.2f}")