br_students = int(input())
fail = 0
betwen = 0
good = 0
very_good = 0
all_grades = 0
for num in range(br_students):
    grade = float(input())
    all_grades += grade
    if 2 <= grade < 3:
        fail += 1
    elif 3 <= grade < 4:
        betwen += 1
    elif 4 <= grade < 5:
        good += 1
    elif grade >= 5:
        very_good += 1
percent_fail = fail / br_students * 100
percent_betwen = betwen / br_students * 100
percent_good = good / br_students * 100
percent_very_good = very_good / br_students * 100
averige = all_grades/br_students
print(f"Top students: {percent_very_good:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_betwen:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {averige:.2f}")
