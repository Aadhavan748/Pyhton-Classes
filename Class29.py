# Example

"""class dad:
    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive

    def display(self):
        print("Your eye color is", self.eyes)
        print("You are agressive", self.aggressive)

# Child class
class son(dad):
    def __init__(self,name,age,eyes,aggressive):
        self.name = name
        self.age = age

        # Invoking the __init__ of parent class
        # to access its attributes
        dad.__init__(self, eyes, aggressive)

# Object Creation
obj = son("Penguin", 8, "blue", True)

# Calling method display
obj.display()

# Activity 1 - Is this a bus?

class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    pass

School_bus = bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "\nSpeed:", School_bus.max_speed,
"\nMileage:", School_bus.mileage)

# Activity 3 - Employee Inheritance

class person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print("The name is:", self.name)
        print("The id number is:", self.id_number)

class Employee(person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        person.__init__(self, name, id_number)

a = Employee("Rahul", 886012, 200000, "Intern")
a.display()"""

# Activity 3 - Super Penguin

class bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# Child class
class Penguin(bird):
    def _init__(self):
        # Call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Object Creation
peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()