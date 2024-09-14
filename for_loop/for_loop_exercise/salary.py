num_websits = int(input())
salary = int(input())
lost_salary = True
for num in range(num_websits):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        lost_salary = False
        break
if lost_salary:
    print(int(salary))
