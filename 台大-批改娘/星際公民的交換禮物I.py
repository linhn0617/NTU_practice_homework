n = int(input())
ans = 0
def decimal_to_septenary(decimal):
    if decimal == 0:
        return "0"  # 十进制数为0时，七进制数也是0
    septenary = ""
    while decimal > 0:
        remainder = decimal % 7
        septenary = str(remainder) + septenary
        decimal //= 7
    return septenary
weight = input().split()
int_weight = [int(x) for x in weight]
sorted_weight = sorted(int_weight)
ans += int(sorted_weight[-1])
ans += int(sorted_weight[-3])
print(decimal_to_septenary(ans))