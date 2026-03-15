test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print(test_dict)

value = input("Enter the value to check the frequency: ")

if value in test_dict:
    print("Frequency of", value, ":", test_dict[value])
else:
    print("Frequency of", value, ": 0")