lst = []  
while True:
    n = int(input())
    for i in range(n):
        num = int(input())
        lst.append(num)
    for j in range(n):
        print("data",lst.pop())
    break