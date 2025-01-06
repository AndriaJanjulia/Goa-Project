"""
1. Create a list named temperatures that contains the following values representing daily temperatures: [72, 68, 75, 70, 78, 74, 71].
2. Calculate and print the highest temperature using the max() function.
3. Calculate and print the lowest temperature using the min() function.
4. Calculate and print the average temperature using the sum() function divided by the length of the list.
5. Use a list comprehension to create a new list named above_70 that contains only the temperatures above 70 degrees.
6. Print the above_70 list.
"""
temperatura =[72,68,75,70,78,74,71]
max_temperatura=max(temperatura)
print(max_temperatura)
min_temperatura=min(temperatura)
print(min_temperatura)
print(sum(temperatura)/7)
above_70=[temp for temp in temperatura if temp > 70]
print(above_70)
