# leap year in two line

year = int(input('Enter year: '))
print('is leap' if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 'is not leap')
