from math import pi
figure = input()
s=0
if figure == "square":
    a = float(input())
    s = a*a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    s = a*b
elif figure == "circle":
    r = float(input())
    s = pi*r**2
elif figure == "triangle":
    a = float(input())
    ha = float(input())
    s = a*ha/2
print(s)
