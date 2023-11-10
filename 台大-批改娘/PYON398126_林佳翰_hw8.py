class student:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.grades = []
    def add(self,grade):
        self.grades.append(grade)

    def avg(self):
        avg_grades = sum(self.grades) / len(self.grades)
        return "{:.1f}".format(avg_grades)
    
    def fcount(self):
        fail_count = 0
        for grade in self.grades:
            if grade < 60:
                fail_count += 1
        return fail_count
    
    def show(self):
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Grades:",self.grades)
        print("Avg:",self.avg())
        print("Fail Number:",self.fcount())

def top(*students):
    if not students:
        return None  # 如果没有传入学生对象，则返回 None

    highest_avg_student = max(students, key=lambda student: float(student.avg()))
    #通過計算每個學生的平均分數，並找到具有最高平均分數的學生。lambda 函數用於幫助 max 函數在比較學生時使用他們的平均分數。
    return highest_avg_student
s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)


s1.show()
print()
s2.show()
print()
s3.show()
print()
s4.show()
print()
s5.show()
print()

top_student = top(s1,s2,s3,s4,s5)
print("Top Student:")
top_student.show()
print()