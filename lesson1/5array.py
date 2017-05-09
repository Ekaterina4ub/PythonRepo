#coding: utf-8
#5) Пользователь вводит число N. Создать массив размера N, который одинаково читается как слева направо, так и справа налево.

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
    elif (i == (middle + 1) and n%2 == 0):
        array[i] = j
    else:
        j -= 1
        array[i] = j
    i += 1

#print(array)
