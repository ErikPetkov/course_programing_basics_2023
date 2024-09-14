size = input()
color = input()
br_paridi = int(input())
partida_price = 0
# ibjhghh
if size == "Large":
    if color == "Red":
        partida_price = 16
    elif color == "Green":
        partida_price = 12
    elif color == "Yellow":
        partida_price = 9
elif size == "Medium":
    if color == "Red":
        partida_price = 13
    elif color == "Green":
        partida_price = 9
    elif color == "Yellow":
        partida_price = 7
elif size == "Small":
    if color == "Red":
        partida_price = 9
    elif color == "Green":
        partida_price = 8
    elif color == "Yellow":
        partida_price = 5
price = br_paridi * partida_price
price *= 0.65
print(f"{price:.2f} leva.")