br_etages = int(input())
br_ap = int(input())
ap = 0
for etages in range(br_etages, 0, -1):
    for aps in range(br_ap):
        if etages == br_etages:
            print(f"L{etages}{ap}", end=" ")
        elif etages % 2 == 1:
            print(f"A{etages}{ap}", end=" ")
        elif etages % 2 == 0:
            print(f"O{etages}{ap}", end=" ")
        ap += 1
    ap = 0
    print()