# Problem we have a CSV file which we want to remove the first row from this file.

# use csv library

# solution:

from csv import reader

openfile = open(r'path')

read_file = reader(openfile)
list_of_lists = list(read_file)  # create list of lists, each list inside the outer list considered row.

print(list_of_lists)  # fast look

# now to remove the first row (index 0) 

list_of_lists = list_of_lists[1:]

# print it to make sure

print(list_of_lists)
