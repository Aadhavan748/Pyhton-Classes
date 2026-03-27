# Activity 1 - Object-Oriented Programming

"""class student:
    grade = 10
    print("Hi I am a student of grade", grade)

# Create an object
ob = student()

# Activity 2 - Class Vehicle

# Create class
class Vehicle:

    # Create init method
    def __init__(self, max_speed, mileage):
        
        # Bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
model1X = Vehicle(240, 18)

# Access the variables inside init method
print("Model Max Speed:", model1X.max_speed)
print("Model Mileage:", model1X.mileage)"""

# Activity 3 - Class parrot

# Create class
class Parrot:
    
    # Class attribute
    species = "bird"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# Access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# Access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))