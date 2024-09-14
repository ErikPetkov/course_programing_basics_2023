grups = int(input())
climbers_musala = 0
climbers_monblan = 0
climbers_kilimandjaro = 0
climbers_k2 = 0
climbers_everest = 0
total_climbers = 0
for num in range(grups):
    people_in_grup = int(input())
    total_climbers += people_in_grup
    if people_in_grup <= 5:
        climbers_musala += people_in_grup
    elif people_in_grup <= 12:
        climbers_monblan += people_in_grup
    elif people_in_grup <= 25:
        climbers_kilimandjaro += people_in_grup
    elif people_in_grup <= 40:
        climbers_k2 += people_in_grup
    elif people_in_grup >= 41:
        climbers_everest += people_in_grup
percent_musala = climbers_musala / total_climbers * 100
percent_monblan = climbers_monblan / total_climbers * 100
percent_kilimanjaro = climbers_kilimandjaro / total_climbers * 100
percent_k2 = climbers_k2 / total_climbers * 100
percent_everest = climbers_everest / total_climbers * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
