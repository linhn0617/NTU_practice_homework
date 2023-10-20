lst = []
while True:
    n = int(input())
    if n == -1:
        break
    else:
        lst.append(n)
lst1 = sorted(lst)
max_num = max(lst)
min_num = min(lst)
print(lst1)
print(len(lst))
print(sum(lst))
print("%.2f"%(sum(lst)/len(lst)))
print(str(max_num)+"@"+str(lst.index(max_num)+1))
print(str(min_num)+"@"+str(lst.index(min_num)+1))
print(lst)