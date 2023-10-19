n = int(input())
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)
print(max(lst),lst.index(max(lst))+1)
print(min(lst),lst.index(min(lst))+1)