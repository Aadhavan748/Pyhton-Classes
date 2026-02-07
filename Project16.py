def shutdown():
    user_input = str(input("Do you want to Shut Down? Type Yes or No: "))

    if user_input == ("Yes"):
        print("Shutting Down")

    elif user_input == ("No"):
        print("Shutdown Cancelled")

    else:
        print("Sorry, only type Yes or No")

shutdown()