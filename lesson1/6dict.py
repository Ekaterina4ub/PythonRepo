#coding: utf-8
#6) Пользователь вводит строку.
# Напечатать словарь, ключами которого являются четные символы строки, а значениями нечетные.
# Если последнему ключу не хватает значения, не добавлять его в словарь.

text = raw_input("Введите строку: ")

len = len(text)

for i in range(0, len, 2):
    if (len%2 != 0 and i == len - 1):
        break
    items = [(text[i + 1], text[i])]
    print(dict(items))