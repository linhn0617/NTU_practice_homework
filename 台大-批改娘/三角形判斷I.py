a = int(input())
b = int(input())
c = int(input())
while True:
    if a + b > c and a + c > b and b + c > a :
        print("True")
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Right Triangle")
            break
        else:
            print("Non-Right Triangle")
            break
    elif a + b == c or a + c == b or b + c == a:
        print("False")
        break
    else:
        print("False")
        break