work_days_time_for_tom = 63
rest_days_time_for_tom = 127
needed_time_for_tom_per_year = 30000
br_rest_days = int(input())

work_days = 365 - br_rest_days
work_days_with_tom = work_days * work_days_time_for_tom
rest_days_with_tom = br_rest_days * rest_days_time_for_tom
time_for_tom_per_year = work_days_with_tom+rest_days_with_tom
diference = abs(time_for_tom_per_year - needed_time_for_tom_per_year)
hours = diference // 60
minutes = diference % 60

if time_for_tom_per_year >= needed_time_for_tom_per_year:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
