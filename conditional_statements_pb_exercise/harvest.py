from math import ceil, floor
x_kv_m_feeld = int(input())
y_harvest_per_kv_m = float(input())
z_needed_liters_wine = int(input())
br_workers = int(input())
harvest = x_kv_m_feeld*y_harvest_per_kv_m
wine = (harvest*0.4)/2.5
difference = abs(wine-z_needed_liters_wine)
wine_per_worker = difference/br_workers
if wine >= z_needed_liters_wine:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
