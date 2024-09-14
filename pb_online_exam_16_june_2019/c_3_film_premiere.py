projection = input()
someting_for_movie = input()
br_tikets = int(input())

one_tiket = 0
if projection == "John Wick":
    if someting_for_movie == "Drink":
        one_tiket = 12
    elif someting_for_movie == "Popcorn":
        one_tiket = 15
    elif someting_for_movie == "Menu":
        one_tiket = 19
elif projection == "Star Wars":
    if someting_for_movie == "Drink":
        one_tiket = 18
    elif someting_for_movie == "Popcorn":
        one_tiket = 25
    elif someting_for_movie == "Menu":
        one_tiket = 30
    if br_tikets >= 4:
        one_tiket *= 0.7
elif projection == "Jumanji":
    if someting_for_movie == "Drink":
        one_tiket = 9
    elif someting_for_movie == "Popcorn":
        one_tiket = 11
    elif someting_for_movie == "Menu":
        one_tiket = 14
    if br_tikets == 2:
        one_tiket*=0.85
end_price = br_tikets * one_tiket
print(f"Your bill is {end_price:.2f} leva.")
