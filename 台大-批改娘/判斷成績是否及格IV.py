while True:
    score = int(input())
    if score >= 60:
        print("pass")
    else:
        print("fail")
    iscontinue = input()
    if iscontinue == "y":
        continue
    else:
        break
