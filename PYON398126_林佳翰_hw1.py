egg = eval(input())
if egg % 12 == 0:
    print(str(int(egg/12)) + " dozen")
else:
    print(str(int(egg/12)) + " dozen and " + str(int(egg%12)))