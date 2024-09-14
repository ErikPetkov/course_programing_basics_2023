videocard_price_per_one = 250
discount = 1

peters_money = float(input())
br_videocards = int(input())
br_procesors = int(input())
br_ram_memories = int(input())
videocard = videocard_price_per_one*br_videocards
procesor_price_per_one = videocard*0.35
ram_memorie_price_per_one = videocard*0.1
if br_videocards > br_procesors:
    discount = 0.85


procesor = procesor_price_per_one*br_procesors
ram = ram_memorie_price_per_one*br_ram_memories
bill = videocard+procesor+ram
bill_with_discount = bill*discount
left = abs(peters_money-bill_with_discount)
if peters_money >= bill_with_discount:
    print(f"You have {left:.2f} leva left!")
else:
    print(f"Not enough money! You need {left:.2f} leva more!")
