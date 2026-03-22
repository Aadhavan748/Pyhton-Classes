n = int(input("Enter a number: "))

odd_numbers = [x for x in range(n) if x % 2 != 0]

print("Odd numbers under", n, ":", odd_numbers)