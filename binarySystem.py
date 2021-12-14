# binary system
# How to convert number from binary to decimal
# binary is 0 and 1 example -> 101010
# decimal is numbers from 0 to 9 example -> 4

# python has the ability to print the value that express about the binary(0, 1) in decimal(0 to 9)

# for example if you want to know what the 100 in decimal
# you can use print function to print the value in decimal
# first step you will put 0b before write any binary 01010 
# because this will considered it as a binary
# the second step you will put the number in binary system 

# examples:

print(0b100)

# output >>> 4

print(0b100)
print(0b101011)
print(0b0110010)

# 4
# 43
# 50

# another way to convert from binary to decimal with use int() function
# int(x, base) that give us the ability to convert string or any number 
# x = what we want convert like '1' will become 1
# base = to any system we would to convert it 
# in our case we want to convert from binary to decimal(0, 9) so base will be 2

# examples:

print(int('100'), 2)

# output >> 4

# we can make the user input the binary
print(int(input('Enter b = '), 2))

# this function to covert from binary to decimal
def convert_binary_to_decimal(n):
    return int(n, 2) # 2 is the base


while 1:
    print(convert_binary_to_decimal(input('n = ')))
