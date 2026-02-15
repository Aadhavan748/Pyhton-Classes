try:
    age = int(input("Enter your age: "))

    age = int(age)

    if age <= 0 or age > 120:
        raise ValueError("Age must be between 1 and 120.")

    if age % 2 == 0:
        print("The age entered is valid and even.")
    else:
        print("The age entered is valid and odd.")

except ValueError as e:
    print("Invalid input:", e)

finally:
    print("Program finished.")
