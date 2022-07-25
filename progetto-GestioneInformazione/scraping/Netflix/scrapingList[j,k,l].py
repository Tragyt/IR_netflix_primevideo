# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:37:12 2022

@author: Vecchi, Ascione
"""

from scraping.DriverSettings import inizialize, create, scroll
from selenium.webdriver.common.by import By


def uploadFile(elements):
    lst = [line[0:8] for line in open("filmsNetflix.txt", "r")]
    for elem in elements:
        films = elem.find_elements(By.TAG_NAME, "a")
        for film in films:
            f = film.get_attribute("href")[30:38]
            if f not in lst:
                lst.append(f)

    with open("filmsNetflix.txt", "w") as file:
        for item in lst:
            file.write("%s\n" % item)


def search(letter, opt):
    driver = create(opt)
    driver.get("https://www.netflix.com/search?q=" + letter)
    scroll(driver, 30)
    rows = driver.find_elements(By.CLASS_NAME, "slider")
    uploadFile(rows)


options = inizialize()

for ltt in ['i', 'j', 'k', 'l', 'm']:
    search(ltt, options)
