# Activity 1 - Operator Overloading

# Python program to overload equality
# and less than operators

"""class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
        
    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
        
ob1 = A(2)
ob2 = A(3)
print("Passed Values: ", ob1.a, ob2.a)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("Passed Values:", ob3.a, ob4.a)
print(ob3 == ob4)

# Activity 2 - Flashcards

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        # we will return a string
        return self.word + "("+self.meaning+")"
    
flash = []
print("Welcome to the flashcard application")

# The following loop will be repeated until the user
# stops to add the flashcards

while(True):
    word = input("Enter the name you want to add to the flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want to add another flashcard, otherwise enter 1: " ))

    if option:
        break

# Printing all the flashcards
print("\n Your flashcards")
for i in flash:
    print(">", i)"""

# Activity 3 - Fruit Quiz

import random

class FruitQuiz:

    # Create a constructor
    def __init__(self):

        # Create a dictionary of fruits as keys and color as value
        self.fruits = {"Apple": "Red",
                       "Orange": "Orange",
                       "Watermelon": "Green",
                       "Banana": "Yellow"}
        
        self.fruits = {"Apple": "red",
                       "Orange": "orange",
                       "Watermelon": "green",
                       "Banana": "yellow"}
    # Function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            user_answer = input("What is the color of {}: ".format(fruit))

            if(user_answer.lower() == color):
                print("Correct Answer")
            else:
                print("Wrong Answer")

            option = int(input("Enter 0 if you want to play again, otherwise enter 1: "))
            if option:
                break

print("Welcome to the fruit quiz")
fq = FruitQuiz()
fq.quiz()