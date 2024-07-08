age = int(input("enter your age: "))
payment = int(input("enter your payment: "))

if age >= 60 and payment < 100:
    print("minor discount")
elif age < 60 and payment >=100:
    print("minor discount")

elif age >= 60 and payment >= 100:
    print("major discount")

else:
    ("no discount")