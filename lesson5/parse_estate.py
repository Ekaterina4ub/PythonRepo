# coding: utf-8

# 1. парсим первые N страниц недвижки у domclik, по аналогии с примером который кидался. считаем средню цену на всех страницах
# 2. пишем генератор который парсит первые N страниц и на каждый шаг возврщает среднюю цену на каждой странице

import requests
import os
from bs4 import BeautifulSoup

n = int(input())
price_all_pages = []
base_url = "https://realty.domclick.ru/prodazha-kvartir/?addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&offset=%s&region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1"
offset = 0

def parse_gen(n, offset):
    for i in range(n):
        r = requests.get(base_url % offset)
        html = r.text
        # print(html)

        soup = BeautifulSoup(html, features='html.parser')
        # print(soup.prettify())

        prices = soup.find_all(class_='offer-snippet__title')
        # print(prices)

        res_pr = []
        for pr in prices:
            sp = pr.find('span')
            # удаляем пробелы в цене
            res_pr.append(int(sp.text.replace(' ', '')))
            # print(res_pr)

        # посчитаем среднюю цену на странице
        avg_price = int(sum(res_pr) / len(res_pr))
        print(avg_price)
        yield avg_price
        offset += 30


for j in parse_gen(n, offset):
    price_all_pages.append(j)

print(price_all_pages)
sum(price_all_pages)
sum_price_all_pages = sum(price_all_pages) / len(price_all_pages)
print(sum_price_all_pages)
