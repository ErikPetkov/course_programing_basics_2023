br_students = int(input())
total_grades = 0
br_students_2 = 0
br_students_3 = 0
br_students_4 = 0
br_students_5 = 0
grades_2 = 0
grades_3 = 0
grades_4 = 0
grades_5 = 0

for grade in range(br_students):
    student_grade = float(input())
    total_grades += student_grade

    if 2 <= student_grade < 3:
        br_students_2 += 1
        grades_2 += student_grade
    elif 3 <= student_grade < 4:
        br_students_3 += 1
        grades_3 += student_grade
    elif 4 <= student_grade < 5:
        br_students_4 += 1
        grades_4 += student_grade
    elif student_grade >= 5:
        br_students_5 += 1
        grades_5 += student_grade

average_grade = total_grades / br_students
total_2 = (br_students_2 / br_students) * 100
total_3 = (br_students_3 / br_students) * 100
total_4 = (br_students_4 / br_students) * 100
total_5 = (br_students_5 / br_students) * 100

print(f"Top students: {total_5:.2f}%")
print(f"Between 4.00 and 4.99: {total_4:.2f}%")
print(f"Between 3.00 and 3.99: {total_3:.2f}%")
print(f"Fail: {total_2:.2f}%")
print(f"Average: {average_grade:.2f}")
