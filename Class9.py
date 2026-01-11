# Activity 1

"""medical_cause=input("Do you have a medical cause? Enter Y or N: ")
attendance=int(input("Enter the attendance of the student: "))

if medical_cause == "Y":
    print("You are allowed")
else:
    if attendance>=75:
        print("You are allowed")
    else:
        print("You are not allowed")

# Activity 2

units=int(input("Please enter the number of units you consumed: "))
if(units<50):
    amount = units*2.60
    surcharge=25

elif(units<=100):
    amount = 130 + ((units-50)*3.25)
    surcharge=35

elif(units<=200):
    amount=130+162.50+((units-100)*5.26)
    surcharge=45

else:
    amount=130+162.50+526+((units-200)*8.45)
    surcharge=75
total=amount+surcharge
print("\nElectricity Bill =%.2f"%total)"""

# Activity 3

print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))
if(choice == 1):
    print("What type of bike do you want?")
    print("1. Scooty\n")
    print("2. Scooter\n")


    choice2 = int(input("Enter your choice2: "))
    if choice2 == 1:
        print("You have selected Scooty")
    else:
        print("You have selected Scooter")

elif(choice == 2):
    print("What type of car do you want?")
    print("1. Sedan")
    print("2. XUV")

    choice3 = int(input("Enter your choice3: "))
    if choice3 == 1:
        print("You have selected Sedan")
    else:
        print("You have selected XUV")
else:
    print("Wrong Choice!")