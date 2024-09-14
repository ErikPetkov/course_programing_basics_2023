number = input()
prime = 0
non_prime = 0
while number != "stop":
    number = int(number)
    n = 0
    if number < 0:
        print("Number is negative.")
    else:
        for num in range(2, number + 1):
            if number % num == 0:
                n += 1
        if n > 1:
            non_prime += number
        else:
            prime += number
    number = input()
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
