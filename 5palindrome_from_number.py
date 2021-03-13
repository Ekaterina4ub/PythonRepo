# # The user enters a number N. Create an array of size N,
# which reads equally from left to right and from right to left (palindrome).

n = int(input())
i = 0
j = 0
array = [1]*n

if n%2 == 0:
    middle = n//2 - 1
else:
    middle = n//2

while i < n:
    if i <= middle:
        j += 1
        array[i] = j
    elif i == (middle + 1) and n % 2 == 0:
        array[i] = j
    else:
        j -= 1
        array[i] = j
    i += 1

print(array)
