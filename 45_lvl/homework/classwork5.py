def calculate_average(numbers):
    if len(numbers) == 0:
        return "სია ცარიელია."
    return sum(numbers) / len(numbers)

numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)

print("სიის საშუალო:", average)
