num = input().split(",")
int_num = [int(x) for x in num]
even = []
odd_number = []
for i in int_num:
    if i%2 == 0:
        even.append(i)
    else:
        odd_number.append(i)
print(sum(odd_number))
print(sum(even))
print(sum(int_num))