country = input()
thing = input()

hard = 0
ting = 0

if country == "Russia":
    if thing == "ribbon":
        hard = 9.1
        ting = 9.4
    elif thing == "hoop":
        hard = 9.3
        ting = 9.8
    elif thing == "rope":
        hard = 9.6
        ting = 9

elif country == "Bulgaria":
    if thing == "ribbon":
        hard = 9.6
        ting = 9.4
    elif thing == "hoop":
        hard = 9.55
        ting = 9.75
    elif thing == "rope":
        hard = 9.5
        ting = 9.4

elif country == "Italy":
    if thing == "ribbon":
        hard = 9.2
        ting = 9.5
    elif thing == "hoop":
        hard = 9.45
        ting = 9.35
    elif thing == "rope":
        hard = 9.7
        ting = 9.

total_points = hard + ting
print(f"The team of {country} get {total_points:.3f} on {thing}.")
left = 20 - total_points
percent = (left / 20) * 100
print(f"{percent:.2f}%")
