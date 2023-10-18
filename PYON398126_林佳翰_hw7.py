lst = []
student_avg = []
total = 0
count = 0

def process_student(student_data):
    print(" 1:", student_data[0])
    print(" 2:", student_data[1])
    print(" 3:", student_data[2])
    print(" sum:", sum(student_data))
    avg = sum(student_data) / len(student_data)
    student_avg.append(avg)
    print(" avg: {:.2f}".format(avg))

for i in range(5):
    student_data = [eval(i)for i in input().split()]
    lst.append(student_data)
for i in range(5):
    print("student", i + 1)
    process_student(lst[i])
for i in lst:
    for j in i:
        total += j
for i in lst:
    for j in i:
        count+=1
print("total:",total,end = ", ")
print("avg: {:.2f}".format(total/count))
max_average = max(student_avg)
best_student_index = student_avg.index(max_average)
#print(f"highest avg: student {best_student_index + 1}: {max_average:.2f}")
print("highest avg: student " + str(best_student_index + 1) + ": {:.2f}".format(max_average))
