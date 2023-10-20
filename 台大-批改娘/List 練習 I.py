lst = []
while True:
    n = int(input())
    if n == -1:
        break
    else:
        lst.append(n)
lst1 = sorted(lst)
print(lst1)
lst1.insert(3,10)
print(lst1)
print(lst1.count(10))
lst1.sort(reverse=True)
print(lst1)