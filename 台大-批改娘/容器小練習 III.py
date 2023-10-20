lst = []
for i in range(5):
    num = int(input())
    lst.append(num)
lst1 = sorted(lst)
for i in lst1:
    print(str(i)+"\t"+i*"*")