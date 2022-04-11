"""
HACKERRANK Problem

Output Format

Print the sum of the elements of set  on a single line.

Sample Input

9  ------------------> Number of elements inside the set
1 2 3 4 5 6 7 8 9  --> This will be ths set
10 ------------------> Number of commands
pop              ----> Here and below each line will contain command ⬇⬇⬇⬇
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5


Sample Output   --->  Here will be the output and it is should be sum of elements of set after did the above commands

4

Explanation

After completing these  operations on the set, we get set. Hence, the sum is .

Note:
Convert the elements of set s to integers while you are assigning them. 

"""


# My Solution:

def execute_user_commands():
        n = int(input())
        s = set(map(int, input().split()))
        number_of_commands = int(input())

        all_commands_from_user = []

        for i in range(number_of_commands):
                cmd = input().split()
                if cmd[0] == "remove":
                    s.remove(int(cmd[1]))
                    continue
                elif cmd[0] == 'discard':
                    s.discard(int(cmd[1]))
                    continue
                s.pop()

        print(sum(s))


execute_user_commands()

