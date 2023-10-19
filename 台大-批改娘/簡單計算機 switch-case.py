a = float(input())
b = float(input())
calculate = input()
if calculate == "+":
    print(str("%.2f"%a)+" "+"+ "+str("%.2f"%b)+" = "+str("%.2f"%(a+b)))
elif calculate == "-":
    print(str("%.2f"%a)+" "+"- "+str("%.2f"%b)+" = "+str("%.2f"%(a-b)))
elif calculate == "*":
    print(str("%.2f"%a)+" "+"* "+str("%.2f"%b)+" = "+str("%.2f"%(a*b)))
elif calculate == "/":
    print(str("%.2f"%a)+" "+"/ "+str("%.2f"%b)+" = "+str("%.2f"%(a/b)))