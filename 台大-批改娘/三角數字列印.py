n = int(input())
current_number = 1
for i in range(1,n+1):
    row = ""
    for j in range(1,i+1):
        row += str(current_number) + " "
        current_number += 1
    print(row)
