num1=int(input("enter your first number: "))
action = str(input("enter your action: "))
num2=int(input("enter your second number: "))
if action == "+" or action == "plus":
   sum = num1 + num2 
elif action == "-" or action == "minus":
   sum = num1 - num2
elif action == "/" or action == "divide":
      sum= num1 / num2 
elif action == "*" or action == "multiply":
   sum = num1 * num2 
else :
   print("Error")
print(sum)
   