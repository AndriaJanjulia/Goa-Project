def separate_even_and_odd(numbers):
    evens = []
    odds = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    return evens, odds

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = separate_even_and_odd(numbers_list)

print("Even numbers:", evens)
print("Odd numbers:", odds)