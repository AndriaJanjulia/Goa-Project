number = [100, 200, 300, 400, 500, 600]
user_number = int(input("please input number: "))
user_index = int(input("please input index: "))
if 0 <= user_index < len(number):
    number[user_index] = user_number
else:
    print("Error")
print(number)