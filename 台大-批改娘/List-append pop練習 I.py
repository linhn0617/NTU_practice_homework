n = int(input())
lst = []
for i in range(n,0,-1):
    lst.append(i)
    print("data",i)
print()
for j in range(n):
    print("data",lst.pop())