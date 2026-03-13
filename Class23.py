# Activity 1 - Get rid of duplicates

"""student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)

# Activity 2 - Frequency

# Initialize dictionary
test_dict = {"Codingal": 2, "is": 2, "best": 2, "for": 2, "Coding": 1}

# Printing Original Dictionary
print("The original dictionary: " + str(test_dict))

# Initialize Value
k = 2

# Using loop
# Sekective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

# Printing result
print("Frequency of k is: " + str(res))"""

# Activity 3 - Country Code

country_code = {"India": "0091",
                "Australia": "0025",
                "Nepal": "00977"}

# Search dictionary for country code of India
print("Country code for India -")
print(country_code.get("India", "Not found"))

# Search dictionary for country code of Japan
print("Country code for Japan-")
print(country_code.get("Japan", "Not found"))

