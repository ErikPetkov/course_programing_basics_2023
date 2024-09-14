movie_name = input()
br_days = int(input())
br_tikets = int(input())
price_per_tiket = float(input())
percent_for_cinema = int(input())
price_per_day = br_tikets * price_per_tiket
for_the_period = br_days * price_per_day
percent = (for_the_period * percent_for_cinema)/100
fo = for_the_period - percent
print(f"The profit from the movie {movie_name} is {fo:.2f} lv.")
