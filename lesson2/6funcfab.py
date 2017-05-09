#coding: utf-8

# 6. Написать функцию-фабрику, которая будет возвращать функцию умножения на аргумент
# Пример:
# mult5 = multiple_inner(5)
# print(mult5(7))
# 35

def mult(arg):
    def multiple_inner(number):
        return arg*number
    return multiple_inner

r = mult(4)
print(r)
print(r(7))