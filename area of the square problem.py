# Problem! you teach children about how to calculate area and perimeter of the square
# and you will solve 20 question about the way to training them.
# but that will consume the time, so you want to write program to reduse from the time
# whan calculate all 20 quest.
# Now try to solve it.
# Hint: perimeter = (x * 4), area = (x ** 2) 

# The first method

def calc(x):
    sideLength = x

    print(f"area = {sideLength ** 2}")
    print(f"perimeter = {sideLength * 4}")

calc(int(input()))

# The second method

calcs = lambda x : (x**2, x*4)
c1, c2 = calcs(int(input())) 
print(f'area = {c1}\nperimeter = {c2}')

# The 3rd method

def calc2(x):
    return (x**2, x*4)

a, b = calcs(int(input()))
print(str(a) + ' is area', str(b) + ' is perimeter')
