txt_list = []
py_list = []
count_txt = 0
count_py = 0
while True:
    n = input()
    p1 = "T0"
    p2 = "P0"
    if n == "-1":
        break
    if n.endswith(".txt"):
        count_txt += 1
        n1 = n.capitalize()
        n1 = p1 + str(count_txt) + "_" + n1
        txt_list.append(n1)
    if n.endswith(".py"):
        count_py += 1
        n2 = n.upper()
        n2 = p2 + str(count_py) + "_" + n2
        n2 = n2[:-3]+".py"
        py_list.append(n2)
 
print(txt_list)
print(py_list)