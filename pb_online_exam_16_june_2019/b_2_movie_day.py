from math import ceil
time_for_filming = int(input())
br_seins = int(input())
timeing_sein = int(input())

time_for_filming *= 0.85
sein_tot = timeing_sein * br_seins
diff = abs(time_for_filming - sein_tot)
if time_for_filming >= sein_tot:
    print(f"You managed to finish the movie on time! You have {ceil(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {ceil(diff)} minutes.")

