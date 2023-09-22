m = eval(input())
for num in range(2,m+1):
    fct = 0
    for i in range(1,num+1):
        if num % i == 0:
            fct += 1
    if fct == 2:
        print(num,"is prime")