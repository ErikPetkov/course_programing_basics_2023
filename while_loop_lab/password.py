user = input()
pasword = input()
ty = input()
while True:
    if pasword == ty:
        print(f"Welcome {user}!")
        break
    ty = input()

