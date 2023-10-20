K = int(input())
L = int(input())
grade_lst=['A+','A','A-','B+','B','B-','C+','C','C-','F']
total_k = 0
total_l = 0
while True:
    grade = input()
    if grade == "q":
        break
    else:
        grade1 = grade.split(",")
        if grade1[2]=="R" and grade1[1]!= "F":
            total_k += int(grade1[3])
        elif grade1[2]=="E" and grade1[1]!= "F":
            total_l += int(grade1[3])
if total_k >= K and total_l >= L:
   print("yes")
else:
    print("no")
