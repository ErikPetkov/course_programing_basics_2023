n = int(input())
p1 = 0
p2 = 0
p3 = 0
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1
pr1 = p1/n * 100
pr2 = p2/n * 100
pr3 = p3/n * 100
print(f"{pr1:.2f}%")
print(f"{pr2:.2f}%")
print(f"{pr3:.2f}%")
