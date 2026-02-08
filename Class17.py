# Activity 1 - break

"""a = input("Enter a word: ")

for i in a:
    if(i == "a"):
        print("A is found.")
        break
    else:
        print("A is not found.")

# Activity 2 - Pass

a = int(input("Enter the number: "))

if a % 20 == 0:
    print("Number is divisible by 20")

elif a % 15 == 0:
    pass

elif a % 5 == 0:
    print("Number is divisible by 5")

elif a % 3 == 0:
    print("Number is divisible by 3")

else:
    print("The number is not divisible by the numbers.")"""

# Activity 3 - Continue

for i in range(10,0,-1):
    if(i == 5):
        continue
    print(i)