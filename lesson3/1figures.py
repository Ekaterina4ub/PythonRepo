#coding: utf-8

# 1. Реализовать классы: фигура, круг, прямоугольник, квадрат. Классы должны предоставлять методы:
# - получение центра
# - получение периметра
# - получение площади

import math

class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        s = self.a * self.b
        return s

    def perimeter(self):
        p = 2 * (self.a + self.b)
        return p

    def center(self):
        center = [self.a/2, self.b/2]
        return center

class Rectangle(Figure):
    pass

class Square(Figure):
    pass

class Circle(Figure):

    def __init__(self, r):
        self.r = r

    def area(self):
        s = self.r**2 * math.pi
        return s

    def perimeter(self):
        p = 2 * math.pi * self.r
        return p

    def center(self):
        center = [self.r, self.r]
        return center

# для проверки:
# r = Rectangle(1, 2)
# r1 = Square(3, 3)
# r2 = Circle(5)
#
# print(r.area())
# print(r.perimeter())
# print(r.center())
#
# print(r1.area())
# print(r1.perimeter())
# print(r1.center())
#
# print(r2.area())
# print(r2.perimeter())
# print(r2.center())