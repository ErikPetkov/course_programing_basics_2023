from math import ceil
tall_wall = int(input())
fat_wall = int(input())
percent = int(input())
liters = input()
room = tall_wall * fat_wall*4
room = ceil(room)
persen = abs(percent/100)
room -= room * persen
left = False
perfect = False
while liters != "Tired!":
    room -= int(liters)
    if room < 0:
        left = True
        break
    elif room == 0:
        perfect = True
        break
    liters = input()
if left == False and perfect == False:
    print(f"{int(room)} quadratic m left.")
elif left == True and perfect == False:
    print(f"All walls are painted and you have {abs(int(room))} l paint left!")
elif left == True and perfect == False:
    print("All walls are painted! Great job, Pesho!")
