age = int(input("Enter your age: "))
if age <10:
    print("You are not old enough to enter this class.")
elif age>20:
    print("You are too old to enter this class.")
elif age >= 10 and age <= 20:
    print("You are eligible to enter this class.")