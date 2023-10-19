float_product_sum = 1.0
int_product_sum = 1
while True:
    number = input()
    if number == "q":
        break
    else:
        number = float(number)
        if number.is_integer():
            int_product_sum *= int(number)
        else:
            float_product_sum *= number
if float_product_sum > int_product_sum:
    print("%.2f"%float_product_sum)
    print(int_product_sum)
    print("Float > Int")
elif float_product_sum == int_product_sum:
    print("%.2f"%float_product_sum)
    print(int_product_sum)
    print("Float = Int")
else:
    print("%.2f"%float_product_sum)
    print(int_product_sum)
    print("Float < Int")

#print("%.2f"%float_product_sum)
#print(int_product_sum)





