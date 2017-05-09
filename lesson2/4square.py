#coding: utf-8

# 4. Написать функцию square, принимающую 2 аргумента — длину сторон прямогольника, и возвращающую 3 значения:
# периметр, площадь и диагональ прямоугольника.

import math

def square(lenght, width):
    if lenght <= 0 or width <= 0:
        print("Please take correct numbers.")
    else:
        params = {'perimeter' : (lenght + width)*2, 'square' : lenght*width, 'diagonal' : math.sqrt(lenght**2 + width**2)}
        return params

#print(square(2, 8))