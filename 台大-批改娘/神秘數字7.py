n,m = map(int,input().split())
seven_multiples = []
contains_seven = []
for num in range(n, m + 1):
    if num % 7 == 0:
        seven_multiples.append(num)

    # 将整数转换为字符串，然后检查字符串中是否包含字符"7"
    if '7' in str(num):
        contains_seven.append(num)
# 打印结果
str_seven_multiples = " & ".join(map(str, seven_multiples))
str_contains_seven = " & ".join(map(str, contains_seven))
print(str_seven_multiples)
print(str_contains_seven)