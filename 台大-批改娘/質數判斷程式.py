n = int(input())
fct = 0
for i in range(1,n+1):
    if n % i == 0:
        fct += 1
if fct == 2:
    print(n,"is prime")
else:
    print(n,"is not prime")