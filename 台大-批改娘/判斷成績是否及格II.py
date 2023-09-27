# Write your code here :-)
Student_status = int(input())
score = int(input())
if Student_status == 1:
    if score >= 60:
        print("pass")
    else:
        print("fail")
elif Student_status == 2:
    if score >= 70:
        print("pass")
    else:
        print("fail")
