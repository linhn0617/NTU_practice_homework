#有一天王老先生一醒來發現雞和兔子的籠子之間破了一個洞。
#導致雞和兔子的籠子相通了，所以他們互相亂串。
#這下可麻煩了，王老先生算不到他們的數量，所以他要求你來幫他的忙。
#由於王老先生視力衰退，所以衹能夠算到這兩個籠子裏一共有多少個頭和多少只脚。
#所以要你來判斷裏面一共有多少只雞和兔子。
#已知王老先生養的每一只動物都是健康的，所以每隻雞都有2只脚，每隻兔子都有4只脚。
#由於王老先生視力衰退，所以有時候也會有看錯的情況，如果看錯了就輸出 "NO" ,反之"YES" (都是大寫)
#兩個整數 N，M代表頭的數量和脚的數量

def solve_chicken_rabbit(N, M):
    for chicken_count in range(N + 1):
        rabbit_count = N - chicken_count
        total_legs = 2 * chicken_count + 4 * rabbit_count
        if total_legs == M:
            return chicken_count, rabbit_count
    return None, None
N, M = map(int, input().split())
chicken, rabbit = solve_chicken_rabbit(N, M)
if chicken is not None and rabbit is not None:
    # 输出结果
    print("YES")
    print(chicken, rabbit)
else:
    print("NO")







