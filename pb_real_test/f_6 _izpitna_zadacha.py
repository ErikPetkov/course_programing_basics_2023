n = int(input())
a = 1
b = 9
c = 0
d = 9
not_found = False
while not not_found:
    A = 0
    B = 0
    A = a*b*c*d
    B = a+b+c+d
    nstr = n
    if A == B and nstr[2] == "5":
        a *= 1000
        b *= 100
        c *= 10
        number = a+b+c+d
        print(f"{number}")
        not_found = True
        break
    elif A//B == 3 and n % 3 == 0:
        d *= 1000
        c *= 100
        b *= 10
        number = a+b+c+d
        print(f"{number}")
        not_found = True
        break
    if a == 9 and b == a and c == 9 and d == c:
        print("Nothing found")
        not_found = True
        break
    if a != 9:
        a += 1
    if b != a:
        b -= 1
    if c != 9:
        c += 1
    if d != c:
        d -= 1
