#coding: utf-8

import requests
import os
from bs4 import BeautifulSoup

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

def parse_gen()