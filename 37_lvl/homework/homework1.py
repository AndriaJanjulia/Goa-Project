'''
Create a list named fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".
Print the entire list.
Access and print the first and last items in the list.
Add a new fruit "fig" to the list.
Remove "banana" from the list.
Change the value of the second item to "blueberry".
Print the length of the list.
'''

fruit =[ "apple", "banana", "cherry", "date","elderberry"]
print(fruit)

print(fruit[0],fruit[-1])
fruit.append("fig")
print(fruit)

fruit.remove('banana')
print(fruit)

fruit[1] = 'blueberry'
print(fruit)

print(len(fruit))