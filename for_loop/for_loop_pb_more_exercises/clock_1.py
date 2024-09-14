hour = 0
minute = 0
while True:
    if minute > 59:
        minute = 0
        hour += 1
    print(f"{hour} : {minute}")
    if hour == 23 and minute == 59:
        break
    minute += 1