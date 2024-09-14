bujet_for_movie = float(input())
br_statists = int(input())
price_dressing_one_statist = float(input())
decor = bujet_for_movie*0.1
dressing = price_dressing_one_statist*br_statists
if br_statists > 150:
    dressing *= 0.9
rashod = decor+dressing
if bujet_for_movie-rashod >= 0:
    print("Action!")
    print(f"Wingard starts filming with {bujet_for_movie-rashod:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(bujet_for_movie-rashod):.2f} leva more.")
