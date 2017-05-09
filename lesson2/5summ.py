#coding: utf-8

# 5. Написать функцию, которой можно передавать аргументы либо списком/кортежем, либо по одному. Функция производит суммирование всех аргументов

def summ(args):
    s = 0
    if isinstance(args, (list, tuple)):
        s += sum(args)
    elif isinstance(args, int):
        s += args
    return s

# print(summ((12, 13)))
# print(summ([12, 13]))
# print(summ(12))