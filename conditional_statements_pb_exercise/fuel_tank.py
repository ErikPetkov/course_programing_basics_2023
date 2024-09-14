type_fuel = input()
liters_fuel = float(input())
if type_fuel == "Diesel":
    type_fuel = "diesel"
    if liters_fuel >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")

elif type_fuel == "Gasoline":
    type_fuel = "gasoline"
    if liters_fuel >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
elif type_fuel == "Gas":
    type_fuel = "gas"
    if liters_fuel >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")
