# There are 3 numbers. Print "yes" if the sum of two of the numbers is equal to the third.

a = int(input())
b = int(input())
c = int(input())

if ((a + b) == c) or (b + c == a) or (c + a == b):
    print("yes")
else:
    print("no")