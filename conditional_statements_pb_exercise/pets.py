from math import ceil, floor

br_days = int(input())
kg_food = int(input())
food_per_day_dog_kg = float(input())
food_per_day_cat_kg = float(input())
food_per_day_tirtle_g = float(input())

needed_dog = br_days * food_per_day_dog_kg
needed_cat = br_days * food_per_day_cat_kg
needed_tirtle = br_days * food_per_day_tirtle_g
total_needed_food = needed_dog+needed_cat+(needed_tirtle/1000)

if total_needed_food <= kg_food:
    print(f"{floor(kg_food-total_needed_food)} kilos of food left.")
else:
    print(f"{ceil(total_needed_food-kg_food)} more kilos of food are needed.")


