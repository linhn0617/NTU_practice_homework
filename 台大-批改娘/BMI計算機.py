height = int(input())
weight = int(input())
BMI = round(weight/(height/100)**2,2)
print(BMI)
if BMI >= 35:
    print("Obese Class III")
elif BMI >= 30:
    print("Obese Class II")
elif BMI >= 27:
    print("Obese Class I")
elif BMI >= 24:
    print("Overweight")
elif BMI >= 18.5:
    print("Normal")
else:
    print("Underweight")