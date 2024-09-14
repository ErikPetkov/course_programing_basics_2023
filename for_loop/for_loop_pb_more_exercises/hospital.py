period_of_days = int(input())
treated_patients = 0
untreated_patients = 0
chek = 3
doctors = 7
for days in range(1, period_of_days+1):
    patients_for_the_day = int(input())
    if days == chek:
        chek += 3
        if untreated_patients > treated_patients:
            doctors += 1

    if patients_for_the_day < doctors:
        treated_patients += patients_for_the_day
    else:
        treated_patients += doctors
        untreated_patients += abs(doctors - patients_for_the_day)
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

