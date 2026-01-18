# Activity 1 - Sum of natural numbers

"""n = int(input("Enter the value of terms: "))

sum = 0
i = 1
while i<=n:
    sum = sum+i
    i = i+1
print(sum)

# Activity 2 - Infinity

while True:
    print("My name is Aadhavan")"""

# Activity 3 - Armstrong Number

num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10 # Extracts last digit of the number
    sum += digit ** 3 # Adds the cube of the digit to sum
    temp //= 10 # Revoves the last digit from the input number

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num,"is not an Armstrong number")