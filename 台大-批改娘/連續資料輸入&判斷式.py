ans = []
while True:
    input_num = input()
    if input_num == "q":
        break
    try:
        input_num = float(input_num)
        ans.append(input_num)
    except:
        continue
final_ans  = "%.2f"%sum(num % 1 for num in ans)
print(final_ans)