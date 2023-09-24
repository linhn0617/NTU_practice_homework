# 撰寫一個程式，先從鍵盤輸入三個整數，然後顯示此三個整數的總和、平均值、乘積、最小值和最大值。螢幕的對話過程應該如下所述。
a = int(input())
b = int(input())
c = int(input())
total = a+b+c
print("sum is",total)
print("average is","%.2f"%(total/3))
print("product is",a*b*c)
print("smallest is",min(a,b,c))
print("largest is",max(a,b,c))
