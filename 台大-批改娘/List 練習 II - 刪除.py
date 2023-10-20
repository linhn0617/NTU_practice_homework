lst = []
while True:
    n = int(input())
    if n == -1:
        break
    else:
        lst.append(n)
i = int(input())
lst1 = sorted(lst)
print(lst1)
lst1.insert(3,10)
print(lst1)
print(lst1.count(10))
lst2 = [x for x in lst1 if x % 10 != i]
lst2.sort(reverse=True)
print(lst2)