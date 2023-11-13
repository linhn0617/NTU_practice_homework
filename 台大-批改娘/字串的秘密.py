dict = {}
for i in range(26):
    dict[chr(ord('A') + i)] = i + 1
n = int(input())
str_lst = []
str_num_sum = []
for i in range(n):
    password = input()
    str_lst.append(password)
    # 將輸入字串中的字母轉換為數字
    numbers = [dict[char.upper()] for char in password if char.isalpha()]
    num_sum = sum(numbers)
    str_num_sum.append(num_sum)
#找到總和最大的密碼的索引
max_sum_index = str_num_sum.index(max(str_num_sum))
for i in range(n):
    print("{} = {}".format(str_lst[i].upper(), str_num_sum[i]))

print("{} is the key.".format(str_lst[max_sum_index].upper()))