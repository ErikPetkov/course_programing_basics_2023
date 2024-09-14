from sys import maxsize
br_numbers = int(input())
bigest_num = - maxsize
smalest_num = maxsize

for _ in range(br_numbers):
    number = int(input())
    if bigest_num < number:
        bigest_num = number
    if smalest_num > number:
        smalest_num = number
print(f"Max number: {bigest_num}")
print(f"Min number: {smalest_num}")

