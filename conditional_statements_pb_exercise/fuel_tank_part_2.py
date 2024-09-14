benzin = 2.22
diesel = 2.33
gas = 0.93
all_fuel_price = 0
type_fuel = input()
liters_fuel = float(input())
card = input()

if card == "Yes":
    benzin = 2.22 - 0.18
    diesel = 2.33 - 0.12
    gas = 0.93 - 0.08

if type_fuel == "Gas":
    all_fuel_price = liters_fuel * gas
elif type_fuel == "Gasoline":
    all_fuel_price = liters_fuel * benzin
elif type_fuel == "Diesel":
    all_fuel_price = liters_fuel * diesel

if 20 <= liters_fuel <= 25:
    all_fuel_price = all_fuel_price * 0.92
elif liters_fuel > 25:
    all_fuel_price = all_fuel_price * 0.90

print(f"{all_fuel_price:.2f} lv.")
