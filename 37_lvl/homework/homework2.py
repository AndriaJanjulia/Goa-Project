"""
Create a list named numbers that contains the following integers: 10, 20, 30, 40, 50, 60, 70, 80, 90.
Use the append() function to add the number 100 to the end of the list.
Use the insert() function to add the number 5 at the beginning of the list.
Use the remove() function to remove the number 30 from the list.
Use the sort() function to sort the list in ascending order.
Use the reverse() function to reverse the order of the list.
Use the index() function to find the index of the number 50.
Use the count() function to count how many times 20 appears in the list.
"""

numbers=[10, 20, 30, 40, 50, 60, 70, 80, 90 ]
numbers.append(100)
print(numbers)
numbers.insert(0,5)
print(numbers)
numbers.remove(30)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.index(50))
print(numbers.count(20))