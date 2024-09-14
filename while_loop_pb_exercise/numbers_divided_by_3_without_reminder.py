num = 1
pop = 1
while True:
    if num > 100:
        break
    if pop == 3:
        print(num)
        pop = 0
    num += 1
    pop += 1
    