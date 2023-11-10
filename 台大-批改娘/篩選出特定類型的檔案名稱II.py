while True:
    n = input()
    p1 = "T00_"
    p2 = "P00_"
    if n == "-1":
        break
    if n.endswith(".txt"):
        n = p1 + n
        print(n)
    if n.endswith(".py"):
        n = p2 + n
        n = n[:-3]+".c"
        print(n)