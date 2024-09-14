price_for_t_shirt = float(input())
price_to_get_ball = float(input())

shorts = price_for_t_shirt * 0.75
soks = shorts * 0.2
butonki = (price_for_t_shirt + shorts) * 2

total_sum = price_for_t_shirt + shorts + soks + butonki
sum_with_discount = total_sum * 0.85

if price_to_get_ball <= sum_with_discount:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {sum_with_discount:.2f} lv.")
elif price_to_get_ball > sum_with_discount:
    needed = price_to_get_ball - sum_with_discount
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed:.2f} lv. more.")
