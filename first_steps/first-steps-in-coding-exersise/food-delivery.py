chiken_menu = 10.35
fish_menu = 12.40
vegi_menu = 8.15
br_chiken = int(input())
br_fish = int(input())
br_vegi = int(input())
br_chiken_menu = br_chiken*chiken_menu
br_fish_menu = br_fish*fish_menu
br_vegi_menu = br_vegi*vegi_menu
all_food = br_chiken_menu+br_fish_menu+br_vegi_menu
dessert = all_food*0.2
order = all_food+dessert+2.5
print(order)