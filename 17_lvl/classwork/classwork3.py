weight = float(input("enter your weight (kg): "))
height = float(input("enter your heightt (meters): "))

bmi = weight / (height * height)
if bmi < 18.5:
      print("underweight")
if bmi == 18.5 and bmi < 24.9:
      
   print("normal weight")
if bmi == 25 and bmi < 29.9:
     print('overweight')
if bmi >= 38:
     print("obese")