name = input()
clas = 0
bad_grades = 0
total_grades = 0
faild = False
while True:
    grade = float(input())

    if grade < 4:
        bad_grades += 1
        if bad_grades > 1:
            faild = True
            break
        continue
    total_grades += grade
    clas += 1
    if clas == 12:
        break
if faild:
    clas += 1
    print(f"{name} has been excluded at {clas} grade")
else:
    total = total_grades / clas
    print(f"{name} graduated. Average grade: {total:.2f}")


