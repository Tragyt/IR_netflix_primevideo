# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:22:58 2022

@author: Vecchi, Ascione
"""

from scraping.DriverSettings import inizialize, create, scroll
from selenium.webdriver.common.by import By
import time


def save(rows):
    with open("filmsNetflix.txt", "a") as file:
        for row in rows:
            films = row.find_elements(By.TAG_NAME, "a")
            for film in films:
                file.write(film.get_attribute("href")[30:38] + "\n")


def a_to_z(opt):
    driver = create(opt)
    driver.get("https://www.netflix.com/browse/genre/34399?so=az")
    scroll(driver, 60)
    rows = driver.find_elements(By.CLASS_NAME, "slider")
    save(rows)
    driver.close()


def z_to_a(opt):
    driver = create(opt)
    driver.get("https://www.netflix.com/browse/genre/34399?so=za")
    scroll(driver, 60)
    rows = driver.find_elements(By.CLASS_NAME, "slider")
    save(rows)
    driver.close()


options = inizialize()

a_to_z(options)
z_to_a(options)
