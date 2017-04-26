#coding: utf-8
#4) Пользователь вводит три числа. Написать "yes", если можно взять какие-то два из них и в сумме получить третье.

a = int(input())
b = int(input())
c = int(input())

if ((a + b) == c) or (b + c == a) or (c + a == b):
    print("yes")
else:
    print("no")