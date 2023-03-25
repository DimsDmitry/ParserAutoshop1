from time import *

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def connect(link):
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, "html.parser")
    return soup

def name_search(address):
    block = address.find("div", class_="gr-elem-name")
    return block

link = 'https://gelzer.ru/catalog/rulevye_reyki/rulevaya_reyka_alfa_romeo_145_146_1994_2001_alfa_romeo_155_1992_1997_alfa_romeo_gtv_1995_alfa_r/'
address = connect(link)
result = name_search(address)
print(result)


# if __name__ == '__main__':
#     link = 'https://gelzer.ru/catalog/rulevye_reyki/rulevaya_reyka_alfa_romeo_145_146_1994_2001_alfa_romeo_155_1992_1997_alfa_romeo_gtv_1995_alfa_r/'
#     # stime = time()
#     # # Initialize Firefox/Gecko WebDriver
#     # driver = webdriver.Firefox()
#     # firefox_options = Options()
#     # driver = webdriver.Firefox(executable_path=".\geckodriver.exe", options=firefox_options)
#     # sleep(3)
#     # #Go to brand link
#     # driver.get(link)
#     # sleep(5)
#     marks = driver.find_elements(by=By.CLASS_NAME, value='bx-title')
#     for mark in marks:
#         mark.text
#         print(mark)
#     etime = time()
#     full_time = (etime - stime) / 60
#     print(f'Link collection is complete! Time spent: {full_time} minutes')