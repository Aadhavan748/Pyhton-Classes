# Activity 1 - Set functions

# Different types of sets in Python
# Set of integers
"""my_set = {1, 2, 3}
print(my_set)

# Set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3), "Hello"}
print(my_set)

# Set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# We can make a set from a list
my_set = set([1, 2, 3, 2])
print(my_set)

# Remove a number from a set

num_set = set([0, 1, 2, 3, 4, 5])
print("Original set:", num_set)
num_set.pop()
print("After removing the first element from the said set:", num_set)

# Activity 2 - Set intersection

setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:", setx,",", sety)

setz = setx.intersection(sety)
print("Intersection of two said sets:", setz)"""

# Activity 3 - Arrays

import array as a

# Create an array
array_num = a.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: " + str(array_num))

# Count number of occurences
print("Number of occurences of the number 3 in the said array: " + str(array_num.count(3)))

# Reverse the array
array_num.reverse()
print("Reverse the order of the items:", str(array_num))