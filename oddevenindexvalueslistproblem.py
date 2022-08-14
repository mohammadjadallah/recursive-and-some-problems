"""
Given two lists, 11 and 12, write a program to create a third list 13 by picking an odd-index elements from the list 11
and even-index elements from the list li2. 

Given:

li1 = [3, 6, 9, 12, 15, 18, 21]
li2 = [4, 8, 12, 16, 20, 24, 28]
 
Expected Output
Element at odd index positions from list one 

[6, l2, 187]

Element at even index positions from list two

[4, 12, 20, 28]

frinting final third list
[6, l2, 187, 4, 12, 20, 28]

"""

li1 = [3, 6, 9, 12, 15, 18, 21]
li2 = [4, 8, 12, 16, 20, 24, 28]
li3 = []
for odd in li1:
    if li1.index(odd) % 2 == 0:
        pass
    else:
        li3.append(odd)
for even in li2:
    if li2.index(even) % 2 == 0:
        li3.append(even)
    else:
        pass
print(li3)
