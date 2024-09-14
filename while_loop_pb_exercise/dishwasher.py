br_bottles_preparad = int(input())
bottles_preparad = br_bottles_preparad * 750
coman = 0
tenjeri = 0
enouf_preparad = True
plates = 0
comand = input()
while comand != "End":
    if bottles_preparad < 0:
        enouf_preparad = False
        break
    dashed = int(comand)
    if coman == 2:
        coman = 0
        tenjeri += dashed
        bottles_preparad -= dashed * 15
    else:
        coman += 1
        plates += dashed
        bottles_preparad -= dashed * 5

    if bottles_preparad < 0:
        enouf_preparad = False
        break
    comand = input()
if enouf_preparad:
    print("Detergent was enough!")
    print(f"{plates} dishes and {tenjeri} pots were washed.")
    print(f"Leftover detergent {bottles_preparad} ml.")
else:
    print(f"Not enough detergent, {abs(bottles_preparad)} ml. more necessary!")
