# Activity 1 - Character occurrence

"""string = input('Please enter your own word: ')
char = input("Please enter your own character: ")

i = 0
count = 0

while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("The total number of times", char, "has occurred in", char, "is", count)"""

# Activity 2 - Prime Numbers

lower = int(input("Enter a lower range: "))
upper = int(input("Enter an upper range: "))

print("Prime numbers between", lower, "and", upper, "are: ")

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)