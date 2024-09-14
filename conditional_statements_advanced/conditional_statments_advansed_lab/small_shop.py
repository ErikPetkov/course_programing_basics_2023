product = input()
city = input()
br = float(input())
price = 0
if city == "Sofia":
    if product == "coffee":
        price = br * 0.5
    elif product == "water":
        price = br * 0.8
    elif product == "beer":
        price = br * 1.2
    elif product == "sweets":
        price = br * 1.45
    elif product == "peanuts":
        price = br * 1.6
elif city == "Plovdiv":
    if product == "coffee":
        price = br * 0.4
    elif product == "water":
        price = br * 0.7
    elif product == "beer":
        price = br * 1.15
    elif product == "sweets":
        price = br * 1.3
    elif product == "peanuts":
        price = br * 1.5
elif city == "Varna":
    if product == "coffee":
        price = br * 0.45
    elif product == "water":
        price = br * 0.7
    elif product == "beer":
        price = br * 1.1
    elif product == "sweets":
        price = br * 1.35
    elif product == "peanuts":
        price = br * 1.55
print(price)