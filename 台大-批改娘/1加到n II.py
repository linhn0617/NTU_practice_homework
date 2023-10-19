sum = 0
n = int(input())
calculation = ""  # 用于存储计算过程的字符串

for i in range(1, n + 1):
    sum += i
    calculation += str(i)
    if i != n:
        calculation += "+"
print(calculation, "=", sum)