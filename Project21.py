start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = [num ** 2 for num in range(start, end + 1)]

even_squares = [s for s in squares if s % 2 == 0]
odd_squares = [s for s in squares if s % 2 != 0]

print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)