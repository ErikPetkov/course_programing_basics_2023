name = input()
grade = float(input())
clas = 1
bad_grade = 0
average = 0
grades = 0
excluded = False
while clas < 12:
    grades += 1
    if grade < 4:
        bad_grade += 1
        if bad_grade > 1:
            excluded = True
            break
    elif grade >= 4:
        clas += 1
    average += grade
    grade = float(input())
if excluded:
    print(f"{name} has been excluded at {clas} grade")
else:
    average /= grades
    print(f"{name} graduated. Average grade: {average:.2f}")


