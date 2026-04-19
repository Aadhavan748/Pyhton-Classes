# Activity 1 - Keep it Private

# Class creation
"""class myClass:

    # Private Variable
    __privateVar = 27

    # Private Method
    def __privmeth(self):
        print("I'm inside of class myClass")

    # Function to print value of private variable
    def hello(self):
        print("Private Variable value:", myClass.__privateVar)

foo = myClass()
foo.__privmeth

# Activity 2 - Computer Price

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setmaxprice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# Change the price
c.__maxprice = 1000
c.sell()

# Using setter function
c.setmaxprice(1000)
c.sell()"""

# Activity 3 - Point Function

# Create Class
class point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
# Create Object
p1 = point(2, 3)
print(p1)