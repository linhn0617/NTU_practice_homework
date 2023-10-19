lst = []
while True:
    num = int(input())
    if num == -1:
        break
    else:
        lst.append(num)
total = sum(lst)
print(total)
print(total/len(lst))
print(max(lst))
print(lst.index(max(lst))+1)