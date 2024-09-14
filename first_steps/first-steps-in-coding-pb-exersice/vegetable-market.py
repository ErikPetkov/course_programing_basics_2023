price_kg_vegetable = float(input())
price_kg_fruit = float(input())
all_kg_vegetable = int(input())
all_kg_fruit = int(input())
vegatable_cost = price_kg_vegetable*all_kg_vegetable
fruit_cost = price_kg_fruit*all_kg_fruit
alll = vegatable_cost+fruit_cost
euro = alll/1.94
print(f"{euro:.2f}")