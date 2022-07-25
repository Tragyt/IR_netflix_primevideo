# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:40:15 2022

@author: Vecchi, Ascione
"""

from selenium import webdriver
import time


def inizialize():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\UTENTE\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    return options


def create(options):
    driver = webdriver.Chrome(r'E:\progetto-GestioneInformazione\scraping\chromedriver.exe', options=options)
    return driver


def scroll(driver, n):
    for i in range(n):
        driver.execute_script("scrollBy(0,1000)")
        time.sleep(0.5)


def scrollEnd(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(1)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
