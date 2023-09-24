#已知，片的重點從影片的第L秒開始，而現在阿宅在影片的第S秒。
#已知阿宅按一次快轉會快轉5秒，而如果超過了第L秒阿宅就需要倒帶,按倒帶一次會回去前2秒。
#PS:如果現在阿宅在1秒，但是他要按倒帶的話，會不成功,因爲影片沒有負數秒。所以那次的操作不算。
#請問阿宅需要最少按幾次才能到達第L秒呢？已知按遙控器時影片時暫停的。

L, S = map(int, input().split())
count = 0
while S != L:
    if S > L:
        S = S-2
        count += 1
        if S > L:
            S = S-2
            count +=1
        elif S < L:
            S = S+5
            count += 1
        else:
            print(count)
            break
    elif S < L:
        S = S + 5
        count += 1
        if S > L:
            S = S-2
            count +=1
        elif S < L:
            S = S+5
            count += 1
        else:
            print(count)
            break
while S == L :
    count+=1
    print(count)
    break
