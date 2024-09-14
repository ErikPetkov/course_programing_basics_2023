stadion_capaciti = int(input())
br_fens = int(input())
A = 0
B = 0
V = 0
G = 0
for _ in range(br_fens):
    sector = input()
    if sector == "A":
        A += 1
    elif sector == "B":
        B += 1
    elif sector == "V":
        V += 1
    elif sector == "G":
        G += 1
precent_A = A/br_fens*100
precent_B = B/br_fens*100
precent_V = V/br_fens*100
precent_G = G/br_fens*100
stadion = br_fens/stadion_capaciti*100
print(f"{precent_A:.2f}%")
print(f"{precent_B:.2f}%")
print(f"{precent_V:.2f}%")
print(f"{precent_G:.2f}%")
print(f"{stadion:.2f}%")

