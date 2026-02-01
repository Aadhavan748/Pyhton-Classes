# Activity 1 - Well wishes

"""def well_wishes():
    print("Hello")
    print("How are you?")

well_wishes()

# Activity 2 - Weather condition

spring = "autumn"
autumn = spring

def weather_condition():
    print("The weather is pleasant in: ", spring)
    print("The weather is the same in ", autumn)

weather_condition()"""

# Activity 3 - Calculator

def addition(P, Q):
    return P + Q

def subtraction(P, Q):
    return P - Q

def multiplication(P, Q):
    return P * Q

def division(P, Q):
    return P / Q

print("Please select the operation: ")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

choice = input("Please enter the choice: ")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if choice == "a":
    print(addition(num1, num2))

elif choice == "b":
    print(subtraction(num1, num2))

elif choice == "c":
    print(multiplication(num1, num2))

elif choice == "d":
    print(division(num1, num2))

else:
    print("This is an invalid input!")