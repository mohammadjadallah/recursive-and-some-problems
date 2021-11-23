# recursion mean function can call itself 
# in our life you can say: thing repeat itself
# so this will generate function which never terminates like (infinity loop). so, we should create condition to stop it.
"""
You can see here how we call the same function inside it:

function():
    ...
    ...
    function()
 
Function which never terminates.
Therefore, use conditions(if else)

So it is divide to two part -> [recursive case, base case]

recursive case = when function call itself
base case = the condition that stop it.

We can use recursive when we divide the code to several parts and each part rely on the previus part.

"""

# Now you know what recursive mean.

# Let us to take famous example the factorial.

def factorial(x):
  if x == 1:
    return 1
  else:
    return x * factorial(x - 1)

 # call the function
factorial(5)  # output >>> 120

"""
How the above code works?

each time the function called itself will check if x == 1 or not

step will take it program to calculate the factorial

1. 5 * factorial(5 - 1)
2. 4 * factorial(4 - 1)
3. 3 * factorial(3 - 1)
4. 2 * factorial(2 - 1)
5. x == 1 yes, so return 1

as you can see every call up to function, it will does it again

when the compiler reach to the factorial(1) and go back to the condition 

if x == 1 will give the value one to factorial 1
now 2 * factorial(1) = 2 * 1 = 2
then we will have all factorial to reach to 5 * factorial(4)

so this will become like this:
     2 * factorial(1) = 2 * 1 = 2
     3 * factorial(2) = 3 * 2 = 6
     4 * factorial(3) = 4 * 6 = 24
     5 * factorial(4) = 5 * 24 = 120

Hence, factorial(5) is 120

"""


