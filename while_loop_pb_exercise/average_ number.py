number = int(input())
n = 0
total = 0
for num in range(number):
    nim = int(input())
    n += nim
total = n/number
print(f"{total:.2f}")
