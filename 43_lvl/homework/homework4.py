def average_of_list(num_list):
    if len(num_list) == 0:
        return 0
    return sum(num_list) / len(num_list)

numbers = [10, 20, 30, 40, 50]
average = average_of_list(numbers)
print(average)