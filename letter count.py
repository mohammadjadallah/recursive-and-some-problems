# These three solutions for help:

# solving number 1:

text = input()

from collections import Counter

c = Counter(text)
print(dict(c))

# solving number 2:

word = input('Enter word: ')
d = dict()

for i in word:
    d[i] = word.count(i)
print(d)

# solving number 3:

word = input('Enter word: ')

print({letter: word.count(letter) for letter in word})
