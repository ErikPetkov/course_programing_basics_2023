br_tovars = int(input())
microbus = 0
truk = 0
train = 0
all_tovar = 0
for export_tovars in range(br_tovars):
    tovar = int(input())
    all_tovar += tovar
    if tovar <= 3:
        microbus += tovar
    elif 4 <= tovar <= 11:
        truk += tovar
    elif tovar >= 12:
        train += tovar
price = (microbus * 200 + truk * 175 + train * 120)/all_tovar
percent_microbus = microbus / all_tovar * 100
percent_truk = truk / all_tovar * 100
percent_train = train / all_tovar * 100
print(f"{price:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truk:.2f}%")
print(f"{percent_train:.2f}%")

