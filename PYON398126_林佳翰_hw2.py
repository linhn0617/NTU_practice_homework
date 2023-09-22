role = eval(input())
if role ==1 or role ==2:
    score = eval(input())
    if score >= 0 and score <= 100:
        if role == 1 and score >= 60:
            print("pass")
        elif role == 2 and score >= 70:
            print("pass")
        else:
            print("fail")
    else:
        print("score error")
else:
    print("role error")