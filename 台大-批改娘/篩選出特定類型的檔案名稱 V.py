total_list = []
txt_list = []
py_list = []
while True:
    n = input()
    p1 = "S0"
    p2 = "S0"

    if n == "-1": 
        break

    total_list.append(n)

    if n.endswith(".txt"):
        n1 = n.capitalize()
        n1 = p1 + str(total_list.index(n) + 1) + "_" + n1
        txt_list.append(n1)

    if n.endswith(".py"):
        n2 = n.upper()
        n2 = p2 + str(total_list.index(n) + 1) + "_" + n2
        n2 = n2[:-3]+".py"
        py_list.append(n2) 

print(txt_list)
print(py_list)