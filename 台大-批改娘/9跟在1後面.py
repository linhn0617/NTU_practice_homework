lst = []
ans = 0
while True:
    n = input()
    if n == "q":
        break
    lst.append(n)
for i in range(len(lst)-1):
    if lst[i] == "1" and lst[i+1] == "9":
        ans += 1
print(ans)