#coding: utf-8

# Задача "Почти SimCity"
# NB - Задача про классы, но не про наследование. Пользоваться наследованием можно,
# но не факт, что это приведет к чему-то хорошему.
#
# Написать программу, которая реализует следующие возможности:
# 1) Добавление, удаление сущности "Город". Город характеризуется именем и числом жителей
# 2) В городе можно добавлять и удалять улицы. Улица характеризуется именем и числом жителей
# 3) На улицу можно добавлять и удалять дома. Дом характеризуется именем и числом жителей
#
# При этом нужно реализовать следующую логику: в городе и улице нельзя напрямую изменять число жителей.
# При добавлении дома на улицу должно увеличиваться число жителей на улице и в городе (на число жителей дома).
# При удалении дома с улицы должно уменьшаться число жителей на улице и в городе.
#
# В городе необходимо реализовать поиск по улице, на улице необходимо реазлизовать поиск по дому
# (в функцию передается наименование улицы / номер дома - возвращается соответствующий объект улицы / дома)
#
# Покрыть тестами (pytest) - помните, что лучше делать проверки логики. Например, создается город, в нем улицы,
#  на них дома. Затем все дома удаляются - число жителей в городе должно стать равным нулю.

# доделать текущую работу + написать методы save - который сохраняет созданную структуру городов - домов...
# в файл и метод load - который из файла загружает сохранненные данные и создает необходимые экземпляры классов

import pickle


class House:
    def __init__(self, name, street, population):
        self.name = name
        self.street = street
        self.population = population

    def __str__(self):
        return str(self.street) + ', ' + str(self.name)

    @classmethod
    def load(cls, file_name):
        with open(file_name, 'rb') as f:
            return pickle.load(f)

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

class Street:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.houses = {}

    def __str__(self):
        return str(self.city) + ', ' + str(self.name)

    @property
    def population(self):
        # Популяция дома - сумма популяций улиц
        return sum(house.population for house in self.houses.values())

    def add_house(self, name, population):
        house = House(self, name, population)
        self.houses[name] = house
        return house

class City:
    def __init__(self, name):
        self.name = name
        self.streets = {}

    def __str__(self):
        return self.name

    @property
    def population(self):
        # Популяция дома - сумма популяций улиц
        return sum(street.population for street in self.streets.values())

    def add_street(self, name):
        street = Street(self, name)
        self.streets[name] = street
        return street

    def remove_street(self, name):
        del self.streets[name]

# h = House ('1', 'Vlasova', 500)
# s = Street('Vlasova', 'Moscow')
# c = City('Moscow')
#
# print(h)
# print(s)
# print(c)
#
# print(s.population)
# print(s.add_house('2', 100))
# print(s.population)
#
# print(c.population)
# print(c.add_street('Vlasova'))
# print(c.population)
# print(c.remove_street('Vlasova'))
# print(c.population)