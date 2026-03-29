# Activity 1 - String Uppercase

# Create Class
"""class IOString():

    # Constructor to set default value
    def __init__(self):
        self.str1 = ""

    # Function to get input from user
    def get_String(self):
        self.str1 = input("Enter String: ")

    # Function to print the string in upper case
    def print_String(self):
        print("Result is: ", self.str1.upper())

# Object Creation
str1 = IOString()

# Call functions
str1.get_String()
str1.print_String()

# Activity 2 - Employee In and Out

# Create Class
class Employee:

    # Initializing
    def __init__(self):
        print("Destructor called")

def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function end...")
    return obj

print("Calling Create_obj() function...")
obj = Create_obj()
print("Program end...")

# Activity 3 - Pair of Elements

class pair_elements:
    def twoSum(self, nums, target):
        # Create an empty dictionary
        lookup = {}

        # Iterate through the tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

# Take input of dum from the user
value = int(input("Enter sum for which you want to make this search: "))
print("index1=%d, index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70),value))"""

# Buffer Activity - 

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width
    
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())