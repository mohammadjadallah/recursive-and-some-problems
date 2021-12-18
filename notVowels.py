'''
Given a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u. 

Sample Input
awesome

Sample Output 
['w', 's', 'm']

'''
word = input()
not_vowels = [i for i in word if i not in ['a', 'e', 'i', 'o', 'u']]
print(not_vowels)
