hour = 0
minute = 0
second = 0
while True:
    if second > 59:
        second = 0
        minute += 1
    if minute > 59:
        minute = 0
        hour += 1

    print(f"{hour} : {minute} : {second}")
    if hour == 23 and minute == 59 and second == 59:
        break
    second += 1