# coding: utf-8

# 1. заходим на сайт domclick
# 2. переходим на выдачу квартир
# 3. переходим на любую
# 4. получаем со страницы квартиры описание

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 1. заходим на сайт domclick
driver = webdriver.Chrome('../chromedriver_mac')
driver.set_window_size(1120, 550)
driver.get("https://domclick.ru/")

# 2. переходим на выдачу квартир
driver.find_elements_by_css_selector('[href="//realty.domclick.ru"]')[0].click()

# 3. переходим на любую
driver.find_elements_by_css_selector('[href="/prodazha-kvartir/?region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1&price__lte=5000000"]')[0].click()

wait = WebDriverWait(driver, 10)
# переключение курсора в новую вкладку
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ui-lazybg.ui-lazybg--visible')))
driver.find_elements_by_css_selector('.ui-lazybg.ui-lazybg--visible')[0].click()

# 4. получаем со страницы квартиры описание
description = {}

windows = driver.window_handles
driver.switch_to.window(windows[1])

element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.offer__price')))

def add_parameter(parameter, target):
    description[parameter] = driver.find_element_by_css_selector(target).get_attribute('innerText').strip()

add_parameter('title', '[class="offer__title"]')
add_parameter('price', '[class="offer__price"]')
add_parameter('address', '[class="offer__address-link"]')
add_parameter('area', '[data-reactid="105"]')
add_parameter('kitchen', '[data-reactid="113"]')
add_parameter('floor', '[data-reactid="115"]')
add_parameter('living_space', '[data-reactid="109"]')
add_parameter('product', '[class="offer-subline__item"]')
add_parameter('desc', '[data-reactid="186"]')

print(description)