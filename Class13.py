# Activity 1 - Right Angle Triangle Patterns

"""print("Half Pyramid Patter of Stars (*): ")
n = int(input('Enter the number of rows: '))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

# Activity 2 - Floyd's Triangle

rows = int(input("Please enter the total number of rows: "))
number = 1

print("Floyd's Triangle")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end = ' ')
        num"""

# Activity 3 - Diamond Pattern

rowSize = int(input("Enter the number of rows: "))
if rowSize%2==0:
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1
space = halfDiamRow-1

for i in range(1, halfDiamRow+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num+1
    print()
space = 1

for i in range(1, halfDiamRow):
    for j in range(1, space+1):
        print(end= " ")
    space = space+1
    num = 1
    for j in range(1, 2*(halfDiamRow-i)):
        print(end=str(num))
        num = num+1
    print()