n = int(input())
input_str = input().split()
input_str_sorted = sorted(input_str)
ans = " ".join(input_str_sorted)+ " "
#ans1 = ans + input_str_sorted[-1]
print(ans)