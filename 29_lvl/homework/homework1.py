weight =float(input("What is your weight? kg : "))
height =float(input("What is your height? m: "))
bmi =  weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 24.9:
    print("normalweight")
elif 25 <= bmi < 29.9:
    print("overweight")
else:
    print("obese")
