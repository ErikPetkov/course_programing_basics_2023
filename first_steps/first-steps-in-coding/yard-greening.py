kv_meters = float(input())
price_with_out_discount = kv_meters * 7.61
discount = price_with_out_discount*0.18
price_with_discount = price_with_out_discount - discount
print(price_with_discount)
print(discount)
