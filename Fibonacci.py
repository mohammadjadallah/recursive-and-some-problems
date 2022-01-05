'''
How Fibonacci sequence is work?

That is simple.
Fibonacci must start with 0 and 1 that is mean previous and next
then all that we need to combine the previous with next to find the next number
so this will be the new result and to find the next number in the sequence the previous will equal the next
and the next will equal the result and so on.

to be completely understood:

previous in the first equal 0
next in the first equal 1

to find the next number combine the previous with next

0 + 1 = 1

so the sequence became =>>  0 1 1

now to find the element after the last element

previuos = next so previous was equal zero now become = 1
next = result, next was 1 and the result from prev and next 0 + 1 = 1

Example on Fibonacci sequence:

Enter 10:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

How?

0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
8 + 13 = 21
13 + 21 = 34
21 + 34 = 55

Now practice code:
'''

num = int(input('num = '))
previous, next, count = 0, 1, 0
result = 1

print('Fibonacci sequence is')

print(previous)
while count < num:
    print(result)
    result = previous + next
    previous = next
    next = result
    count += 1
