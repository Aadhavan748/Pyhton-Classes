# Activity 1 - Map Functions

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

# Using map
nums = [1, 2, 3, 4, 5]
def sq(n):
  return n*n
square = list(map(sq, nums))
print("Square of numbers in list")
print(square)

# Activity 2 - Zip it!

# Zip elements of two lists
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3)

# Zip elements of two lists
# Print elements one by one, but elements of 2nd list will be in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
  print(x,y)

# Zip into dictionary
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))

# Activity 3 - Exit Functions

import sys
for i in range(10):
  if i == 5:
    print(exit)
    sys.exit()
  print(i)