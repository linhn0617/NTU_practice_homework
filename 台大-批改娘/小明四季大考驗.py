month = int(input())
if month > 12 :
    print("Month doesn't exist!")
elif month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
else:
    print("Winter")