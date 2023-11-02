while True:
    n = input()
    try:
        num = int(n)
        num > 0
        print("n="+str(num))
        break
    except:
        print("is not a number")
