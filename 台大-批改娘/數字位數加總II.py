# 接受用户输入的数字
num = int(input())

# 初始化各位数字之和
num_sum = 0

# 计算各位数字之和
while num > 0:
    digit = num % 10  # 获取最右边的数字
    num_sum += digit  # 累加到各位数字之和
    num //= 10  # 去掉最右边的数字

# 输出各位数字之和
print(num_sum)