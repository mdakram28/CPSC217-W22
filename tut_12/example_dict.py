
frequency = {}
word = input("Enter a word ")
for letter in word:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(frequency)
