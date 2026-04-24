# Activity 1 - Abstract Class

# Import necessary Modules
"""from abc import ABC, abstractmethod

# Create base class
class Abssclass(ABC):

    # Function to print a value
    def print(self,x):
        print("Passed value: ", x)

    # Abstract method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

# Create sub class
class test_class(Abssclass):
    def task(self):
        print("We are inside test_class task")

# Object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

# Activity 2 - Class Animals

# Import necessary packages
from abc import ABC, abstractmethod
# Create a base class
class Animal(ABC):

    # Abstract method
    # Should be implemented by all sub-classes
    def move(self):
        pass

# Sub classes
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

# Driver code
K = Human()
K.move()

K = Snake()
K.move()

K = Dog()
K.move()

K = Lion()
K.move()

# Activity 3 - All About Countries

# Class 1
class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language of India")

    def type(self):
        print("India is a developing country")

# Class 2
class USA():
    def capital(self):
        print("Washington, D.C is the capital of the USA")

    def language(self):
        print("English is the primary language of the USA")

    def type(self):
        print("USA is a developed country")

# Object creation
obj_ind = India()
obj_usa = USA()

# Common Interference
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()"""

# Polymorphism Example

# Class square
class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is: ", self.side**2)

# Class circle
class circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print("My area is: ", 3.14*self.radius*self.radius)

# Class rectangle
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print("My area is: ", self.length*self.breadth)

# Object creation
osquare = square(5)
ocircle = circle(5)
orectangle = rectangle(6, 7)

# Iterating through objects
for shape in (osquare, ocircle, orectangle):
    shape.area()