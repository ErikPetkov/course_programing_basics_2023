part_of_campoinat = input()
tipe_ticket = input()
br_tickets = int(input())
photo_with_tropy = input()
ticket_price_per_one = 0
free = False

if part_of_campoinat == "Quarter final":
    if tipe_ticket == "Standard":
        ticket_price_per_one = 55.5
    elif tipe_ticket == "Premium":
        ticket_price_per_one = 105.2
    elif tipe_ticket == "VIP":
        ticket_price_per_one = 118.9

elif part_of_campoinat == "Semi final":
    if tipe_ticket == "Standard":
        ticket_price_per_one = 75.88
    elif tipe_ticket == "Premium":
        ticket_price_per_one = 125.22
    elif tipe_ticket == "VIP":
        ticket_price_per_one = 300.4

elif part_of_campoinat == "Final":
    if tipe_ticket == "Standard":
        ticket_price_per_one = 110.1
    elif tipe_ticket == "Premium":
        ticket_price_per_one = 160.66
    elif tipe_ticket == "VIP":
        ticket_price_per_one = 400

total_price_tickets = ticket_price_per_one * br_tickets
if total_price_tickets > 4000:
    total_price_tickets *= 0.75
    free = True
elif total_price_tickets > 2500:
    total_price_tickets *= 0.9

if photo_with_tropy == "Y" and not free:
    total_price_tickets += (br_tickets * 40)

print(f"{total_price_tickets:.2f}")
