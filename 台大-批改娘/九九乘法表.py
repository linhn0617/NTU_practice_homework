# 输入整数 m 和 n
m = int(input())
n = int(input())

# 打印 m*n 的九九乘法表，乘数和被乘数之间没有空格
for i in range(1, m + 1):
    for j in range(1, n + 1):
        product = i * j
        # 使用 str.format 进行格式化
        print("{}*{}={:2}".format(i, j, product), end=" ")
    print()  # 换行以打印下一行的乘法表