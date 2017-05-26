#coding: utf-8

# 1. Реализовать классы: фигура, круг, прямоугольник, квадрат. Классы должны предоставлять методы:
# - получение центра
# - получение периметра
# - получение площади

import math

class Figures:
    def __init__(self, a, b):
        self.a = a
        self.b = b

#    @staticmethod
    def area(a, b):
        area = a * b
        return area

    def perimeter(a, b):
        perimeter = 2 * (a + b)
        return perimeter

    # def center:
    #     center =
    #     return center

class Rectangle(Figures):
    pass

class Square(Figures):
    pass

class Circle:

    def __init__(self, r):
        # self.a = a
        # self.b = b
        self.r = r

    def area(r):
        area = r**2 * math.pi
        return area

    def perimeter(r):
        perimeter = 2 * math.pi * r
        return perimeter

    # def center:
    #     center =
    #     return center

r = Rectangle(1, 2)
r1 = Square(1, 3)
r2 = Circle(1)

r.area
r1.area
r2.area

print(r.area)
print(r1.area)
print(r2.area)
