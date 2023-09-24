#請撰寫一程式，令使用者輸入一整數半徑r，請列出圓形之圓周率，半徑，圓周長及圓面積
import math
math.pi
radius = int(input())
print("圓周率",math.pi)
print("半徑"+" "+str(radius))
print("圓周長"+" "+str(2*radius*math.pi))
print("圓面積"+" "+str(radius*radius*math.pi))
