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


if __name__ == '__main__':
    stime = time()
    # Initialize Firefox/Gecko WebDriver
    driver = webdriver.Firefox()
    firefox_options = Options()
    driver = webdriver.Firefox(executable_path=".\geckodriver.exe", options=firefox_options)

    with open('auto_list.txt') as fr:
        text_base = fr.read().split('\n')

    for link in text_base:
        sleep(3)
        #Go to brand link
        driver.get(link)
        sleep(5)
        marks = driver.find_elements(by=By.CLASS_NAME, value='gr-filter-checkbox-wrapper')
        k = 0
        #Check all types of this brand
        for k in range(len(marks)):
            marks[k].click()
            sleep(1)
            address = connect(driver.current_url)
            #Write the link to the product in the file
            for a in address.find_all("a", {"class": "gr-product-item__border-inner"}):
                with open('product_links.txt') as fr:
                    content = fr.read()
                print('Link found:', a['href'])
                new_link = 'https://gelzer.ru' + a['href']
                if new_link in content:
                    print('Already have!')
                    continue
                with open('product_links.txt', 'a') as file:
                    file.write(f'{new_link}\n')
                    print('The link was successfully recorded!')
    etime = time()
    full_time = (etime - stime) / 60
    print(f'Link collection is complete! Time spent: {full_time} minutes')