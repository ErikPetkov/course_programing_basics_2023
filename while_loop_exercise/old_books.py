neded_book = input()
book = input()
found = False
br_book = 0

while book != "No More Books":

    if book == neded_book:
        found = True
        break
    book = input()
    br_book += 1
if found:
    print(f"You checked {br_book} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {br_book} books.")


