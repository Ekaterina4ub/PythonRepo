#coding: utf-8

# 1. Написать функцию, принимаюшую на вход число и возвращаюшую последовательность чисел Фибоначчи до этого числа

n = int(input())

def fib(n):
    f = []
    f.append(0)
    f.append(1)
    i = 3
    while True:
        if (f[i - 2] + f[i - 3]) <= n:
            f.append(f[i-2] + f[i-3])
        else:
            break
        i += 1
    return f

#print(fib(n))