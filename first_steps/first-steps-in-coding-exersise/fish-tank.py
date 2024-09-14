long = int(input())
fat = int(input())
tall = int(input())
persent = float(input())
s_in_fish_tank = long*fat*tall
s_in_liters = s_in_fish_tank*0.001
persent=persent/100
needed_liters = s_in_liters*(1-persent)
print(needed_liters)
