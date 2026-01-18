n = int(input("Enter a number: "))
num = 0

while n > 0:
    num = num + 1
    n = n // 10

print(num)