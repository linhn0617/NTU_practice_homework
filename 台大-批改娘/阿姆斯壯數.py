n, m = map(int, input().split())
armstrong_numbers = []

for i in range(n, m + 1):
    l = len(str(i))
    digits = []
    total = 0

    temp = i  # 使用 temp 存储当前的数字

    while temp > 0:
        # 使用取余运算符来获取最后一位数字
        digit = temp % 10
        digits.append(digit)  # 将该位数添加到列表中
        temp //= 10  # 去掉已经提取的位数

    for j in digits:
        total += j**l

    if i == total:
        armstrong_numbers.append(i)

# 在循环结束后，输出所有找到的 Armstrong 数
if armstrong_numbers:
    armstrong_str = " & ".join(map(str, armstrong_numbers))
    print(armstrong_str)
else:
    print("none")