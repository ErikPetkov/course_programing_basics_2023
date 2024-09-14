x = float(input())
y = float(input())
h = float(input())
door = 1.2 * 2
windows = (1.5*1.5)*2
front_and_back = ((x*x)*2)-door
left_and_right = ((x*y)*2)-windows
all_green = front_and_back+left_and_right
roof_triangle = (x*h/2)*2
roof_sqer = (x*y)*2
roof = roof_sqer+roof_triangle
red = roof/4.3
green = all_green/3.4
print(f"{green:.2f}")
print(f"{red:.2f}")
