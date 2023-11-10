txt_list = []
py_list = []
while True:
    n = input()
    p1 = "T00_"
    p2 = "P00_"
    if n == "-1":
        break
    if n.endswith(".txt"):
        n1 = n.capitalize()
        n1 = p1 + n1
        txt_list.append(n1)
    if n.endswith(".py"):
        n2 = n.upper()
        n2 = p2 + n2
        n2 = n2[:-3]+".py"
        py_list.append(n2)

print(txt_list)
print(py_list)