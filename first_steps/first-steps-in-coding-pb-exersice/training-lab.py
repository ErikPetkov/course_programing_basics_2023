w = float(input())
h = float(input())

chair_w = 120
width_h = 70

total_w = w * 100
total_h = h * 100

free_row_h = total_h - 100
chair_row_h = free_row_h // width_h
chair_row_w = total_w // chair_w
total = int((chair_row_h * chair_row_w) - 3)

print(total)
