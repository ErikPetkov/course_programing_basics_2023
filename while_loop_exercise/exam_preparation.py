bad_grades = int(input())
fail = True
ba = 0
num = 0
grades = 0
name_of = ""
name_of_exersice = input()
while name_of_exersice != "Enough":
    bad = bad_grades

    grade = int(input())
    grades += grade
    num += 1
    if grade <= 4:
        ba += 1
        if ba >= bad:
            fail = False
            break
    if name_of_exersice != "Enough":
        name_of = name_of_exersice
    name_of_exersice = input()
if fail:
    average = grades / num
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {num}")
    print(f"Last problem: {name_of}")
else:
    print(f"You need a break, {ba} poor grades.")
