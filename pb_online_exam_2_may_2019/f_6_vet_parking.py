days = int(input())
hours = int(input())
dayt = 0
tdt = 0
for d in range(1, days+1):
    for h in range(1, hours+1):
        if d % 2 == 0 and h % 2 == 1:
            dayt += 2.5
        elif d % 2 == 1 and h % 2 == 0:
            dayt += 1.25
        else:
            dayt += 1
    print(f"Day: {d} - {dayt:.2f} leva")
    tdt += dayt
    dayt = 0
print(f"Total: {tdt:.2f} leva")
