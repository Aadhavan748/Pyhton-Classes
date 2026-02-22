# Activity 1 - List

"""empty_list = []
print()

numbers = [1, 2, 3, 4, 5, "hello", 2.8154384, 2]
print(numbers)

triples = [1, 2, 3] * 3
print(triples)

aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList, "\n")"""

# Activity 2 - Word Matching

"""def match_words(words):
    ctr = 0
    list = []

    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            ctr += 1
            list.append(word)

    print("List of words with first and last character being the same\n", list)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having the first and last character the same are:", count)"""

# Activity 3 - Play with list

L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

L. sort
print("The smallest element is: ", L[0])
print("The largest element is:", L[-1])