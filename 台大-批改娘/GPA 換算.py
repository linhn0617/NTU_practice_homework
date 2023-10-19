grade = int(input())
if grade >= 90:
    print(float(4.3))
    print("A+")
elif grade >= 85:
    print(float(4.0))
    print("A")
elif grade >= 80:
    print(float(3.7))
    print("A-")
elif grade >= 77:
    print(float(3.3))
    print("B+")
elif grade >= 73:
    print(float(3.0))
    print("B")
elif grade >= 70:
    print(float(2.7))
    print("B-")
elif grade >= 67:
    print(float(2.3))
    print("C+")
elif grade >= 63:
    print(float(2.0))
    print("C")
elif grade >= 60:
    print(float(1.7))
    print("C-")
else:
    print(int(0))
    print("F")