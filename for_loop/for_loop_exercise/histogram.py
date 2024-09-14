numberss = int(input())
counter_p1 = 0
counter_p2 = 0
counter_p3 = 0
counter_p4 = 0
counter_p5 = 0
for n in range(numberss):
    number = int(input())
    if number < 200:
        counter_p1 += 1
    elif 200 <= number < 400:
        counter_p2 += 1
    elif 400 <= number < 600:
        counter_p3 += 1
    elif 600 <= number < 800:
        counter_p4 += 1
    elif number >= 800:
        counter_p5 += 1
percent_p1 = counter_p1 / numberss * 100
percent_p2 = counter_p2 / numberss * 100
percent_p3 = counter_p3 / numberss * 100
percent_p4 = counter_p4 / numberss * 100
percent_p5 = counter_p5 / numberss * 100
print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")

