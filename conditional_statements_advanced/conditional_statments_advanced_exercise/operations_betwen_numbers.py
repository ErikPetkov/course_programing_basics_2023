number1 = int(input())
number2 = int(input())
operator = input()
result = 0
o = 0
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif number1 == 0 or number2 == 0:
    o = 1
elif operator == "/":
    result = number1 / number2
elif operator == "%":
    result = number1 % number2
if operator == "+" or operator == "-" or operator == "*":
    odd_even = result % 2 == 1
    if odd_even == 1:
        print(f"{number1} {operator} {number2} = {result} - odd")
    else:
        print(f"{number1} {operator} {number2} = {result} - even")
elif o == 1:
    print(f"Cannot divide {number1} by zero")
elif operator == "/":
    print(f"{number1} / {number2} = {result:.2f}")
elif operator == "%":
    print(f"{number1} % {number2} = {result}")

