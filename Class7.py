# Activity 1

"""x = 5.0
if (type)(x) is int:
    print("True")
else:
    print("False")

x = 20
y = 20
if (x is y):
    print("x and y are the same values")

y = 30
if (x is not y):
    print("x and y have different values")

# Activity 2
numbers = [10,20,30,40]
a = 10
print(a in numbers)
b = 50
print(b in numbers)
word = "Python"
print("a" in word)"""

# Activity 3

m1 = int(input("Enter marks obtained: "))
m2 = int(input("Enter marks obtained: "))
m3 = int(input("Enter marks obtained: "))
m4 = int(input("Enter marks obtained: "))
m5 = int(input("Enter marks obtained: "))

total = m1 + m2 + m3 + m4 + m5
avg = total/5

if avg >= 91 and avg<=100:
    print("Your grade is A1")
elif avg>= 81 and avg<91:
    print("Your grade is A2")
elif avg>= 71 and avg<81:
    print("Your grade is B1")
elif avg>= 61 and avg<71:
    print("Your grade is B2")
elif avg>= 51 and avg<61:
    print("Your grade is C1")
elif avg>= 41 and avg<51:
    print("Your grade is C2")
elif avg>= 31 and avg<41:
    print("Your grade is D")
elif avg>= 21 and avg<31:
    print("Your grade is E1")
elif avg>= 0 and avg<21:
    print("Your grade is E2")
else:
    print("Invalid input")