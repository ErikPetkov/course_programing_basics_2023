juri = int(input())
name_precentation = input()
total_grades = 0
br_precentations = 0
while name_precentation != "Finish":
    grades = 0
    br_precentations += 1
    for _ in range(1, juri+1):
        grade = float(input())
        grades += grade
    grades_av = grades / juri
    total_grades += grades_av
    print(f"{name_precentation} - {grades_av:.2f}.")
    name_precentation = input()
total_grades_av = total_grades/br_precentations
print(f"Student's final assessment is {total_grades_av:.2f}.")
