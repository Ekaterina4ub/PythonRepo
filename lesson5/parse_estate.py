#coding: utf-8

# 1. парсим первые N страниц недвижки у domclik, по аналогии с примером который кидался. считаем средню цену на всех страницах
# 2. пишем генератор который парсит первые N страниц и на каждый шаг возврщает среднюю цену на каждой странице

import requests
import os
from bs4 import BeautifulSoup

n = input()
offset = []

for i in range(n):
    offset.append(i*30)
    print(offset)

res = requests.get('https://realty.domclick.ru/prodazha-kvartir/?with_photo=1&addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5')
html = res.text

soup = BeautifulSoup(html, features='html.parser')
#print(soup.prettify())

prices = soup.find_all(class_='offer-snippet__title')
#print(prices)

res_pr = []
for pr in prices:
    sp = pr.find('span')
    # удаляем пробелы в цене
    res_pr.append(int(sp.text.replace(' ', '')))
#print(res_pr)

# посчитаем среднюю цену на странице
sum(res_pr)
avg_price = sum(res_pr)/len(res_pr)
print(avg_price)



base_url = " https://realty.domclick.ru/prodazha-kvartir/?addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&offset=%s&region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1"
for url in [base_url % i for i in xrange(10)]:
    r = requests.get(url)

# base_url = "http://example.com/something/?page=%s"
# for url in [base_url % i for i in xrange(10)]:
#     r = requests.get(url)


# def parse_gen():
#     for i in range(n):
#         yield a
#
#
# for i in parse_gen():
#     print(i)