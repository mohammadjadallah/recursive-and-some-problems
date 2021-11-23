# Example factorial with use recursive


# Let us to take famous example the factorial.

def factorial(x):
  if x == 1:
    return 1
  else:
    return x * factorial(x - 1)

 # call the function
factorial(5)  # output >>> 120
