from pprint import pprint
sentence = "This is a common interview question"
char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

#pprint(char_frequency, width=1)
print(sorted(char_frequency.items(), key=lambda item: item[1], reverse=True))
