# Activity 1 - Random Number Game

"""import random

playing = True
number = int(random.randint(1,6))

print("A number from 1 to 20 will be generated and you have to guess one \ndigit at a time.")
print("The game ends when you get the correct answer")

while playing:
    guess = int(input("Give me your best guess: "))

    if number == guess:
        print("You win the game!")
        print("The number was", number)
        break

    else:
        print("Your guess wasn't quite right, try again.")"""

# Activity 2 - Rock Paper Scissors

import random

while True:
    user_action = input("Enter a choice between rock, paper and scissors: ")
    possible_actions = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action}, computer chose {computer_action}.")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")

        else:
            print("Scissors cuts paper! You lose")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")

        else:
            print("Rock smashes scissors! You lose")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break