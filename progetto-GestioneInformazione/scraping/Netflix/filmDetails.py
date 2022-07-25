import json
from scraping.DriverSettings import inizialize, create
from selenium.webdriver.common.by import By


def searchFilm(code, opt):
    driver = create(opt)
    driver.get("https://www.netflix.com/browse?jbv=" + code)

    film = {}
    try:
        cont = driver.find_element(By.CLASS_NAME, "about-container")
        tags = cont.find_elements(By.CLASS_NAME, "previewModal--tags")

        regia_elems = []
        cast_elems = []
        sceneggiatura_elems = []
        generi_elems = []
        caratteristiche_elems = []

        for tag in tags:
            section = tag.find_element(By.CLASS_NAME, "previewModal--tags-label").text
            if section == "Regia:":
                regia_elems = [direction.text.replace(",", "") for direction in tag.find_elements(By.CLASS_NAME, "tag-item")]
            elif section == "Cast:":
                cast_elems = [cast.text.replace(",", "") for cast in tag.find_elements(By.CLASS_NAME, "tag-item")]
            elif section == "Sceneggiatura:":
                sceneggiatura_elems = [scn.text.replace(",", "") for scn in tag.find_elements(By.CLASS_NAME, "tag-item")]
            elif section == "Generi:":
                generi_elems = [gen.text.replace(",", "") for gen in tag.find_elements(By.CLASS_NAME, "tag-item")]
            elif section == "Caratteristiche:":
                caratteristiche_elems = [crt.text.replace(",", "") for crt in tag.find_elements(By.CLASS_NAME, "tag-item")]

        film = {
            "codice": code,
            "titolo": driver.find_element(By.TAG_NAME, "strong").text,
            "anno": driver.find_element(By.CLASS_NAME, "year").text,
            "durata": driver.find_element(By.CLASS_NAME, "duration").text,
            "descrizione": driver.find_element(By.CLASS_NAME, "previewModal--detailsMetadata").find_element(By.CLASS_NAME, "ptrack-content").text,
            "regia": regia_elems,
            "cast": cast_elems,
            "sceneggiatura": sceneggiatura_elems,
            "generi": generi_elems,
            "caratteristiche": caratteristiche_elems,
            "classificazione": driver.find_element(By.CLASS_NAME, "maturityDescription").text
        }

    finally:
        return film


lst = [line[0:8] for line in open("filmsNetflix.txt", "r")]
options = inizialize()

film = []
for li in lst:
    film.append(searchFilm(li, options))


with open("output.json", "w") as outfile:
    json.dump(film, outfile, indent=4)

