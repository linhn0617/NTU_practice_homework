class student:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.grades = []
    def add(self,grade):
        self.grades.append(grade)

    def avg(self):
        avg_grades = sum(self.grades) / len(self.grades)
        return "{:.2f}".format(avg_grades)
    
    def fcount(self):
        fail_count = 0
        for grade in self.grades:
            if grade < 60:
                fail_count += 1
        return fail_count
    
    def show(self):
        print(self.name)
        print(self.avg())
        print(self.fcount())
n = input()
g = input()
grade1 = int(input())
grade2 = int(input())
grade3 = int(input())
p1 = student(n,g)
p1.add(grade1)
p1.add(grade2)
p1.add(grade3)
p1.show()