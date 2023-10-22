n = int(input())
ans = ''.join(str(i) for i in range(1, n + 1))
ans +=''.join(str(i) for i in range(n - 1, 0, -1))+'\n'
print(int(ans))