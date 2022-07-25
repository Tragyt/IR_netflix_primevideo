from scraping.DriverSettings import inizialize, create, scrollEnd
from selenium.webdriver.common.by import By
import time


def categories(opt):
    driver = create(opt)
    driver.get("https://www.primevideo.com/storefront/movie/ref=atv_tc_m")
    scrollEnd(driver)

    rows = driver.find_elements(By.CLASS_NAME, "_1k-t3N")
    links = []
    for row in rows:
        try:
            lnk = row.find_element(By.TAG_NAME, "a").get_attribute("href")
            if lnk is not None:
                links.append(lnk)
        finally:
            continue

    driver.close()
    with open("links.txt", 'a') as file:
        for link in links:
            file.write(link + '\n')


def visitLink(lnk, opt):
    driver = create(opt)
    driver.get(lnk)
    scrollEnd(driver)

    elems = driver.find_elements(By.CLASS_NAME, "av-hover-wrapper")
    lst = []
    for elem in elems:
        lnk_film = elem.find_element(By.TAG_NAME, "a").get_attribute("href")
        if lnk_film not in lst:
            lst.append(lnk_film)

    driver.close()
    return lst


def visitLinks(file, opt):
    lnks = [line for line in open(file, "r")]
    lst = []
    for lnk in lnks:
        ls = visitLink(lnk, opt)
        for l in ls:
            if l not in lst:
                lst.append(l)
    with open("films.txt", 'a') as f:
        for elem in lst:
            f.write(elem + '\n')


options = inizialize()
visitLinks("links.txt", options)

# categories(options)
