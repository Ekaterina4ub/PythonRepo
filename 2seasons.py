# return the season that corresponds the number of the month

month = int(input())
if 1 <= month <= 2 or month == 12:
    print('Winter')
elif 3 <= month <= 5:
    print('Spring')
elif 6<= month <= 8:
    print('Summer')
elif 9<= month <= 11:
    print('Autumn')
else:
    print('The month number does not correspond to a number from 1 to 12, please enter a valid number')