lv_strobery = float(input())
kg_banana = float(input())
kg_orange = float(input())
kg_swetbery = float(input())
kg_strobery = float(input())

lv_sletbery = lv_strobery / 2
lv_oranges = lv_sletbery - (0.4*lv_sletbery)
lv_bananas = lv_sletbery - (0.8*lv_sletbery)

sum_swetbery = lv_sletbery * kg_swetbery
sum_orange = lv_oranges * kg_orange
sum_banana = lv_bananas * kg_banana
sum_strobery = lv_strobery * kg_strobery

tot_sum = sum_strobery + sum_banana + sum_orange + sum_swetbery

print(f"{tot_sum:.2f}")
