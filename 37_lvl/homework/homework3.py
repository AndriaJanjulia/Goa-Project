"""
1. Create a list named numbers that contains the integers from 1 to 10.
2. Use list slicing to create a new list named first_half that contains the first five elements from numbers.
3. Use list slicing to create another list named second_half that contains the last five elements from numbers.
4. Use a list comprehension to create a new list named squares that contains the squares of each number in the numbers list.
5. Print all three lists: first_half, second_half, and squares.
"""
numbers=[1,2,3,4,5,6,7,8,9,10]
first_half=numbers[:5]
print(first_half)
secomd_half=numbers[5:]
print(secomd_half)
square=[y**2 for y in numbers]
print(square)