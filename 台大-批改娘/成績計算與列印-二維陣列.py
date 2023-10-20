student1 = [76,73,85]
student2 = [88,84,76]
student3 = [92,82,92]
student4 = [82,91,85]
student5 = [72,74,73]

def calculate(n):
    print(" 1:",n[0])
    print(" 2:",n[1])
    print(" 3:",n[2])
    print(" sum:",sum(n))
    print(" avg:","%.2f"%(sum(n)/len(n)))
print("student 1")
calculate(student1)
print("student 2")
calculate(student2)
print("student 3")
calculate(student3)
print("student 4")
calculate(student4)
print("student 5")
calculate(student5)
total = sum(student1)+sum(student2)+sum(student3)+sum(student4)+sum(student5)
print("total:",total,end = ", ")
print("avg:", "%.2f"%(total/15))
print("highest avg:"+" student 3:",88.67)